import hashlib
import json
import logging
import re
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from io import BytesIO
from typing import Optional

import coloredlogs
import dateparser
import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup
from model import Model
from tqdm import tqdm

from deutschland.config import Config, module_config

# Get logger
logger = logging.getLogger(__name__)

# Install coloredlogs
coloredlogs.install(
    level="WARNING",
    logger=logger,
    fmt="%(levelname)s - %(message)s",
)


class Report:
    def __init__(
        self, report_date: datetime, name: str, content_url: str, company: str
    ):
        self.report_date = report_date
        self.name = name
        self.content_url = content_url
        self.company = company
        self.report_content: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "report_date": self.report_date.isoformat(),
            "name": self.name,
            "company": self.company,
            "report_content": self.report_content,
        }

    def to_hash(self) -> str:
        entry = self.to_dict()
        encoded = json.dumps(entry, sort_keys=True).encode("utf-8")
        dhash = hashlib.md5(encoded, usedforsecurity=False)
        return dhash.hexdigest()

    def set_content(self, content: str) -> None:
        self.report_content = content


class Bundesanzeiger:
    __slots__ = ["session", "model", "captcha_callback", "_config"]

    def __init__(self, on_captcha_callback=None, config: Optional[Config] = None):
        self._config = config or module_config
        self.session = requests.Session()
        if self._config.proxy_config is not None:
            self.session.proxies.update(self._config.proxy_config)
        if on_captcha_callback:
            self.captcha_callback = on_captcha_callback
        else:
            self.model = Model().session
            self.captcha_callback = self.__solve_captcha

    def __solve_captcha(self, image_data: bytes):
        image = BytesIO(image_data)
        image_arr = Model.load_image_arr(image)
        image_arr = image_arr.reshape((1, 50, 250, 1)).astype(np.float32)
        prediction = self.model.run(None, {"captcha": image_arr})[0][0]
        prediction_str = Model.prediction_to_str(prediction)
        return prediction_str

    def __is_captcha_needed(self, entry_content: str):
        soup = BeautifulSoup(entry_content, "html.parser")
        return not bool(soup.find("div", {"class": "publication_container"}))

    def __find_all_entries_on_page(self, page_content: str):
        soup = BeautifulSoup(page_content, "html.parser")
        wrapper = soup.find("div", {"class": "result_container"})
        rows = wrapper.find_all("div", {"class": "row"})
        for row in rows:
            info_element = row.find("div", {"class": "info"})
            if not info_element:
                continue

            link_element = info_element.find("a")
            if not link_element:
                continue

            entry_link = link_element.get("href")
            entry_name = link_element.contents[0].strip()

            date_element = row.find("div", {"class": "date"})
            if not date_element:
                continue

            date = dateparser.parse(date_element.contents[0], languages=["de"])

            company_name_element = row.find("div", {"class": "first"})
            if not date_element:
                continue

            company_name = company_name_element.contents[0].strip()

            yield Report(date, entry_name, entry_link, company_name)  # type: ignore

    def __generate_result(
        self,
        content: str,
        company_name: str,
        show_progress_bar: bool,
        disable_manual_input: bool = False,
    ):
        result = {}
        entries = list(self.__find_all_entries_on_page(content))
        found_companies = set()
        for entry in entries:
            found_companies.add(entry.company)

        selected_company_name = company_name
        selected_option = len(found_companies) + 1

        if len(found_companies) > 1 and not disable_manual_input:
            logger.warning(
                f"Found {len(found_companies)} companies for {company_name}:"
            )
            for idx, company in enumerate(found_companies, start=1):
                print(f"{idx}. {company}")
            print(f"{len(found_companies) + 1}. All")

            selected_option = 0
            while selected_option < 1 or selected_option > len(found_companies) + 1:
                try:
                    selected_option = int(
                        input("Please select the correct company (enter the number): ")
                    )
                except ValueError:
                    print("Invalid input. Please enter a number.")

            if selected_option != len(found_companies) + 1:
                selected_company_name = list(found_companies)[selected_option - 1]

        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = []
            for element in entries:
                # Filter entries based on the selected company name
                if (
                    element.company == selected_company_name
                    or selected_option == len(found_companies) + 1
                ):
                    futures.append(executor.submit(self.__process_entry, element))

            for future in tqdm(
                futures,
                desc="Processing entries",
                unit="entry",
                colour="green",
                disable=not show_progress_bar,
            ):
                entry_hash, entry_dict = future.result()
                if entry_hash and entry_dict:
                    result[entry_hash] = entry_dict

        return result

    def __process_entry(self, element: Report):
        get_element_response = self.session.get(element.content_url)

        if self.__is_captcha_needed(get_element_response.text):
            soup = BeautifulSoup(get_element_response.text, "lxml")
            captcha_wrapper = soup.find("div", {"class": "captcha_wrapper"})

            if captcha_wrapper is not None:
                captcha_image_src = captcha_wrapper.find("img")["src"]
                img_response = self.session.get(captcha_image_src)
                captcha_result = self.captcha_callback(img_response.content)
                captcha_endpoint_url = soup.find_all("form")[1]["action"]
                get_element_response = self.session.post(
                    captcha_endpoint_url,
                    data={"solution": captcha_result, "confirm-button": "OK"},
                )

        content_soup = BeautifulSoup(get_element_response.text, "lxml")
        content_element = content_soup.find("div", {"class": "publication_container"})

        if not content_element:
            return None, None

        element.set_content(content_element.text)

        return element.to_hash(), element.to_dict()

    def __deduplicate_reports(self, reports: dict) -> dict:
        """
        Deduplicates financial reports based on report name and company name, keeping the latest report.

        Args:
            reports (dict): A dictionary containing the fetched reports, with their hash as keys and report details as values.

        Returns:
            dict: A dictionary containing the deduplicated reports, with their hash as keys and report details as values.
        """
        unique_reports = {}
        for report_hash, report in reports.items():
            key = (report["name"], report["company"])
            if key not in unique_reports:
                unique_reports[key] = report
            else:
                existing_report = unique_reports[key]
                if dateparser.parse(report["report_date"]) > dateparser.parse(  # type: ignore
                    existing_report["report_date"]
                ):
                    unique_reports[key] = report

        # Convert back to the original format with hash as keys
        deduplicated_reports = {
            hashlib.md5(
                json.dumps(report, sort_keys=True).encode("utf-8"),
                usedforsecurity=False,
            ).hexdigest(): report
            for report in unique_reports.values()
        }
        return deduplicated_reports

    def get_reports(
        self,
        company_name: str,
        deduplicate: bool = False,
        show_progress_bar: bool = True,
        disable_manual_input: bool = False,
    ):
        """
        Fetches financial reports for a given company from the Bundesanzeiger website.

        Args:
            company_name (str): The name of the company for which to fetch reports.
            deduplicate (bool, optional): Whether to deduplicate the reports based on the report_name and report_date, keeping only the most recent report.
                Defaults to False.
            disable_manual_input (bool, optional): Whether to disable manual input for selecting the correct company if multiple companies are found for the given company name.
            show_progress_bar (bool, optional): Whether to display a progress bar during the process. Defaults to True.

        Returns:
            dict: A dictionary containing the fetched reports, with their hash as keys and report details as values.
        """
        self.session.cookies["cc"] = "1628606977-805e172265bfdbde-10"
        self.session.headers.update(
            {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7,et;q=0.6,pl;q=0.5",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "DNT": "1",
                "Host": "www.bundesanzeiger.de",
                "Pragma": "no-cache",
                "Referer": "https://www.bundesanzeiger.de/",
                "sec-ch-ua-mobile": "?0",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            }
        )
        # get the jsessionid cookie
        response = self.session.get("https://www.bundesanzeiger.de")
        # go to the start page
        response = self.session.get("https://www.bundesanzeiger.de/pub/de/start?0")
        # perform the search
        response = self.session.get(
            f"https://www.bundesanzeiger.de/pub/de/start?0-2.-top%7Econtent%7Epanel-left%7Ecard-form=&fulltext={company_name}&area_select=&search_button=Suchen"
        )
        if response.status_code != 200:
            raise Exception("Could not fetch reports")

        if deduplicate:
            return self.__deduplicate_reports(
                self.__generate_result(
                    response.text, company_name, show_progress_bar, disable_manual_input
                )
            )

        return self.__generate_result(
            response.text, company_name, show_progress_bar, disable_manual_input
        )

    def get_reports_by_date_range(
        self,
        company_name: str,
        start_date: str,
        end_date: str,
        deduplicate: bool = False,
        show_progress_bar: bool = True,
        disable_manual_input: bool = False,
    ):
        """
        Fetches financial reports for a given company within a specified date range from the Bundesanzeiger website.

        Args:
            company_name (str): The name of the company for which to fetch reports.
            start_date (str): The start date of the date range in the format 'YYYY-MM-DD'.
            end_date (str): The end date of the date range in the format 'YYYY-MM-DD'.
            show_progress_bar (bool, optional): Whether to display a progress bar during the process. Defaults to True.
            disable_manual_input (bool, optional): Whether to disable manual input for selecting the correct company if multiple companies are found for the given company name.

        Returns:
            dict: A dictionary containing the fetched reports, with their hash as keys and report details as values.
        """
        # Set up session cookies and headers
        self.session.cookies["cc"] = "1628606977-805e172265bfdbde-10"
        self.session.headers.update(
            # ... (headers)
        )
        # Get the jsessionid cookie
        response = self.session.get("https://www.bundesanzeiger.de")
        # Go to the start page
        response = self.session.get("https://www.bundesanzeiger.de/pub/de/start?0")
        # Perform the search within the specified date range
        response = self.session.get(
            f"https://www.bundesanzeiger.de/pub/de/start?0-2.-top%7Econtent%7Epanel-left%7Ecard-form=&fulltext={company_name}&area_select=&search_button=Suchen&date_start={start_date}&date_end={end_date}"
        )
        if response.status_code != 200:
            raise Exception("Could not fetch reports")

        if deduplicate:
            return self.__deduplicate_reports(
                self.__generate_result(
                    response.text, company_name, show_progress_bar, disable_manual_input
                )
            )

        return self.__generate_result(
            response.text, company_name, show_progress_bar, disable_manual_input
        )


def extract_kpis(reports: dict) -> dict:
    """
    Extracts Key Performance Indicators (KPIs) from the financial reports.

    Args:
        reports (dict): A dictionary containing the financial reports with their hash as keys and report details as values.

    Returns:
        dict: A dictionary containing the extracted KPIs with their report hash as keys and KPIs as values.
    """

    kpis = {}

    # Define KPI patterns to search for
    kpi_patterns = {
        "revenue": r"(?:revenue|umsatz|erlöse)[:\s]*([\d,.]+[mmb]?)",
        "net_income": r"(?:net income|jahresüberschuss|nettoeinkommen)[:\s]*([\d,.]+[mmb]?)",
        "ebit": r"(?:ebit|operating income)[:\s]*([\d,.]+[mmb]?)",
        "ebitda": r"(?:ebitda)[:\s]*([\d,.]+[mmb]?)",
        "gross_profit": r"(?:gross profit|bruttogewinn)[:\s]*([\d,.]+[mmb]?)",
        "operating_profit": r"(?:operating profit|betriebsgewinn)[:\s]*([\d,.]+[mmb]?)",
        "assets": r"(?:total assets|bilanzsumme)[:\s]*([\d,.]+[mmb]?)",
        "liabilities": r"(?:total liabilities|gesamtverbindlichkeiten)[:\s]*([\d,.]+[mmb]?)",
        "equity": r"(?:shareholders'? equity|eigenkapital)[:\s]*([\d,.]+[mmb]?)",
        "current_assets": r"(?:current assets|umlaufvermögen)[:\s]*([\d,.]+[mmb]?)",
        "current_liabilities": r"(?:current liabilities|kurzfristige verbindlichkeiten)[:\s]*([\d,.]+[mmb]?)",
        "long_term_debt": r"(?:long[-\s]?term debt|langfristige verbindlichkeiten)[:\s]*([\d,.]+[mmb]?)",
        "short_term_debt": r"(?:short[-\s]?term debt|kurzfristige verbindlichkeiten)[:\s]*([\d,.]+[mmb]?)",
        "cash_and_cash_equivalents": r"(?:cash (?:and cash equivalents)?|barmittel)[:\s]*([\d,.]+[mmb]?)",
        "dividends": r"(?:dividends?|dividende)[:\s]*([\d,.]+[mmb]?)",
        "cash_flow": r"(?:cash flow|cashflow|cash flow from operating activities)[:\s]*([\d,.]+[mmb]?)",
    }

    for report_hash, report in reports.items():
        report_kpis = {}
        report_content = report["report_content"]

        for kpi, pattern in kpi_patterns.items():
            match = re.search(pattern, report_content, flags=re.IGNORECASE | re.UNICODE)
            if match:
                value = match.group(1)

                # Clean and validate the extracted number
                try:
                    if not value:  # Check if value is empty
                        cleaned_value = None
                    else:
                        multiplier = 1
                        if value[-1].lower() == "m":
                            value = value[:-1]
                            multiplier = 1_000_000
                        elif value[-1].lower() == "b":
                            value = value[:-1]
                            multiplier = 1_000_000_000

                        # Remove commas after checking for multipliers
                        value = value.replace(".", "").replace(",", ".").strip()
                        cleaned_value = float(value) * multiplier
                except ValueError:
                    cleaned_value = None

                if cleaned_value is not None:
                    report_kpis[kpi] = cleaned_value

        kpis[report_hash] = report_kpis

    return kpis


def visualize_kpis(kpis: dict, reports: dict):
    """
    Visualizes the extracted KPIs using bar charts.

    Args:
        kpis (dict): A dictionary containing the extracted KPIs with their report hash as keys and KPIs as values.
        reports (dict): A dictionary containing the financial reports with their hash as keys and Report objects as values.
    """

    kpi_data: dict = {}
    for report_hash, report_kpis in kpis.items():
        report = reports[report_hash]
        report_title = report["name"]

        for kpi, value in report_kpis.items():
            if kpi not in kpi_data:
                kpi_data[kpi] = {"titles": [], "values": []}

            kpi_data[kpi]["titles"].append(report_title)
            kpi_data[kpi]["values"].append(value)

    # Create bar charts for each KPI
    for kpi, data in kpi_data.items():
        plt.figure()
        plt.bar(data["titles"], data["values"])
        plt.title(f"{kpi.capitalize()} over Time")
        plt.ylabel(kpi.capitalize())
        plt.xticks(rotation=90)
        plt.gcf().autofmt_xdate()
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    ba = Bundesanzeiger()
    start_time = time.time()
    reports = ba.get_reports(
        "Siemke & Co. Brücken- und Ingenieurbau GmbH",
        deduplicate=True,
        show_progress_bar=True,
        disable_manual_input=True,
    )
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken to fetch reports: {elapsed_time:.2f} seconds")
    print(f"Found {len(reports)} reports")
    print()

    kpis = extract_kpis(reports)

    for i in reports.keys():
        report = reports[i]
        kpi = kpis[i]
        print(f"Report name: {report['name']}")
        report_date = datetime.strptime(report["report_date"], "%Y-%m-%dT%H:%M:%S")
        print(
            f"Company name: {report['company']} (date: {report_date.strftime('%d.%m.%Y')})"
        )
        print(f"KPIs: {kpi}")
        print()
    visualize_kpis(kpis, {hash_: report for hash_, report in reports.items()})
