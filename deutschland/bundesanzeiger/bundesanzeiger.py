from io import BytesIO
import requests

import dateparser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from deutschland.bundesanzeiger.model import (
    load_image_arr,
    load_model,
    prediction_to_str,
)
from webdriver_manager.chrome import ChromeDriverManager


class Bundesanzeiger:
    requests_settings = {
        "headers": {
            "Connection": "keep-alive",
            "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Dest": "image",
            "Referer": "https://www.bundesanzeiger.de/",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        },
        "timeout": 1,
    }

    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--single-process")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.model = load_model()

    def __solve_captcha(self, image):
        image = BytesIO(image)
        image_arr = load_image_arr(image)
        image_arr = image_arr.reshape((1, 50, 250, 1))

        prediction = self.model.predict(image_arr)[0]
        prediction_str = prediction_to_str(prediction)
        return prediction_str

    def __get_report(self, itm):
        report = {
            "date": dateparser.parse(
                itm.find_element(By.CLASS_NAME, "date").text, languages=["de"]
            ),
            "name": itm.find_element(By.CLASS_NAME, "info")
            .find_element(By.XPATH, "a[1]")
            .text,
            "company": itm.find_element(By.CLASS_NAME, "first").text,
            "report": None,
        }

        itm.find_element(By.CLASS_NAME, "info").find_element(By.XPATH, "a[1]").click()
        try:
            image_src = self.driver.find_element(
                By.CLASS_NAME, "captcha_wrapper"
            ).get_attribute("innerHTML")
            bs_src = BeautifulSoup(image_src, "html.parser")
            captcha_img_link = bs_src.find(lambda tag: tag.name == "img")["src"]
            cookies = {}
            for cookie in self.driver.get_cookies():
                cookies[cookie["name"]] = cookie["value"]
            captcha_img_resp = requests.get(
                captcha_img_link, cookies=cookies, **self.requests_settings
            )
            captcha = self.__solve_captcha(captcha_img_resp.content)
            # send captcha
            captcha_field = self.driver.find_element(By.XPATH, '//*[@name="solution"]')
            captcha_field.send_keys(captcha)
            captcha_field.send_keys(Keys.ENTER)
        except NoSuchElementException:
            pass

        try:
            # extract html
            report["report"] = self.driver.find_element(
                By.CLASS_NAME, "publication_container"
            ).get_attribute("innerHTML")
        except Exception:
            return None
        self.driver.find_element(
            By.XPATH,
            '//*[@id="content"]/section/div/div/div/div/div[1]/div[2]/div/div[1]/a',
        ).click()
        return report

    def __iterate_trough_search_results(self, found_reports=None):
        """iterate trough all results and try to fetch single reports"""
        if found_reports is None:
            found_reports = {}
        for itm in self.driver.find_elements(
            By.XPATH, '//*[@id="content"]/section[2]/div/div/div/div/div[6]/div'
        ):
            document_name = None
            try:
                document_name = itm.find_element(By.CLASS_NAME, "info").text
            except NoSuchElementException:
                continue

            if document_name and document_name not in found_reports:
                report = self.__get_report(itm)
                if report:
                    found_reports[document_name] = report
                return self.__iterate_trough_search_results(found_reports)
        return found_reports

    def get_reports(self, company_name: str):
        """
        fetch all reports for this company name
        :param company_name:
        :return: Dict of all reports
        """
        self.driver.get("https://www.bundesanzeiger.de/ebanzwww/wexsservlet")
        elem = self.driver.find_element_by_id("cc_all")
        elem.click()
        elem = self.driver.find_element_by_id("id3")
        elem.send_keys(company_name)
        elem.send_keys(Keys.ENTER)
        return self.__iterate_trough_search_results()


if __name__ == "__main__":
    ba = Bundesanzeiger()
    reports = ba.get_reports("Deutsche Bahn AG")
    print(reports.keys())
