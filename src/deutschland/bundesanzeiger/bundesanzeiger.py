import hashlib
import json
from io import BytesIO
from urllib.parse import quote_plus

import dateparser
import numpy as np
import requests
from bs4 import BeautifulSoup

from deutschland.config import Config, module_config


class Report:
    __slots__ = ["date", "name", "content_url", "company", "report", "raw_report"]

    def __init__(self, date, name, content_url, company, report=None, raw_report=None):
        self.date = date
        self.name = name
        self.content_url = content_url
        self.company = company
        self.report = report
        self.raw_report = raw_report

    def to_dict(self):
        return {
            "date": self.date,
            "name": self.name,
            "company": self.company,
            "report": self.report,
            "raw_report": self.raw_report,
        }

    def to_hash(self):
        """MD5 hash of a the report."""

        dhash = hashlib.md5()

        entry = {
            "date": self.date.isoformat(),
            "name": self.name,
            "company": self.company,
            "report": self.report,
        }

        encoded = json.dumps(entry, sort_keys=True).encode("utf-8")
        dhash.update(encoded)

        return dhash.hexdigest()


class Bundesanzeiger:
    __slots__ = ["session", "model", "captcha_callback", "_config"]

    def __init__(self, on_captach_callback=None, config: Config = None):
        if config is None:
            self._config = module_config
        else:
            self._config = config

        self.session = requests.Session()
        if self._config.proxy_config is not None:
            self.session.proxies.update(self._config.proxy_config)
        if on_captach_callback:
            self.callback = on_captach_callback
        else:
            import deutschland.bundesanzeiger.model

            self.model = deutschland.bundesanzeiger.model.load_model()
            self.captcha_callback = self.__solve_captcha

    def __solve_captcha(self, image_data: bytes):
        import deutschland.bundesanzeiger.model

        image = BytesIO(image_data)
        image_arr = deutschland.bundesanzeiger.model.load_image_arr(image)
        image_arr = image_arr.reshape((1, 50, 250, 1)).astype(np.float32)

        prediction = self.model.run(None, {"captcha": image_arr})[0][0]
        prediction_str = deutschland.bundesanzeiger.model.prediction_to_str(prediction)

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

            yield Report(date, entry_name, entry_link, company_name)

    def __generate_result_for_page(self, content: str):
        """iterate trough all results and try to fetch single reports"""
        result = {}
        for element in self.__find_all_entries_on_page(content):
            get_element_response = self.__get_response(element.content_url)

            if self.__is_captcha_needed(get_element_response.text):
                soup = BeautifulSoup(get_element_response.text, "html.parser")
                captcha_image_src = soup.find("div", {"class": "captcha_wrapper"}).find(
                    "img"
                )["src"]
                img_response = self.__get_response(captcha_image_src)
                captcha_result = self.captcha_callback(img_response.content)
                captcha_endpoint_url = soup.find_all("form")[1]["action"]
                get_element_response = self.session.post(
                    captcha_endpoint_url,
                    data={"solution": captcha_result, "confirm-button": "OK"},
                )

            content_soup = BeautifulSoup(get_element_response.text, "html.parser")
            content_element = content_soup.find(
                "div", {"class": "publication_container"}
            )

            if not content_element:
                continue

            element.report = content_element.text
            element.raw_report = content_element.prettify()

            result[element.to_hash()] = element.to_dict()

        return result

    def __get_next_page_link(self, content: str):
        soup = BeautifulSoup(content, "html.parser")
        active_link = soup.select_one("div.page-item a.active")
        if not active_link:
            return None

        active_index = None
        try:
            active_index = int(active_link.text.strip())
        except ValueError:
            return None

        next_index = active_index + 1
        next_link = soup.select_one(f'div.page-item a[title="Zur Seite {next_index}"]')
        if not next_link:
            return None

        return next_link.attrs.get("href")

    def __generate_result(self, url: str, page_limit: int):
        results = dict()
        pages = 0
        while url is not None and pages < page_limit:
            content = self.__get_response(url)
            result_for_page = self.__generate_result_for_page(content.text)
            results.update(**result_for_page)
            url = self.__get_next_page_link(content.text)
            pages += 1
        return results

    def __get_response(self, url: str) -> requests.Response:
        """send a request to a URL and validate the response"""
        response = self.session.get(url)
        if not response.ok:
            raise ConnectionError(
                f"There was an error while connecting to '{response.url}'. Got status code {response.status_code} - {response.reason}"
            )

        return response

    def get_reports(self, company_name: str, *, page_limit=1):
        """
        fetch all reports for this company name
        :param company_name:
        :param page_limit: Maximum number of pages to fetch (default: 1). Normally each page has 20 reports.
            Pass `float('inf')` to fetch all pages (this might take a while).
        :return" : "Dict of all reports
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
        response = self.__get_response("https://www.bundesanzeiger.de")
        # go to the start page
        response = self.__get_response("https://www.bundesanzeiger.de/pub/de/start?0")
        # perform the search
        search_url = f"https://www.bundesanzeiger.de/pub/de/start?0-2.-top%7Econtent%7Epanel-left%7Ecard-form=&fulltext={quote_plus(company_name)}&area_select=&search_button=Suchen"
        return self.__generate_result(search_url, page_limit)


if __name__ == "__main__":
    ba = Bundesanzeiger()
    reports = ba.get_reports("Deutsche Bahn AG")
    print(reports.keys(), len(reports))
