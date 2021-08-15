from io import BytesIO
import requests

import dateparser

from bs4 import BeautifulSoup

from deutschland import Config, module_config


class Report:
    __slots__ = ["date", "name", "content_url", "company", "report"]

    def __init__(self, date, name, content_url, company, report=None):
        self.date = date
        self.name = name
        self.content_url = content_url
        self.company = company
        self.report = report

    def to_dict(self):
        return {
            "date": self.date,
            "name": self.name,
            "company": self.company,
            "report": self.report,
        }


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
        image_arr = image_arr.reshape((1, 50, 250, 1))

        prediction = self.model.predict(image_arr)[0]
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

    def __generate_result(self, content: str):
        """iterate trough all results and try to fetch single reports"""
        result = {}
        for element in self.__find_all_entries_on_page(content):
            get_element_response = self.session.get(element.content_url)

            if self.__is_captcha_needed(get_element_response.text):
                soup = BeautifulSoup(get_element_response.text, "html.parser")
                captcha_image_src = soup.find("div", {"class": "captcha_wrapper"}).find(
                    "img"
                )["src"]
                img_response = self.session.get(captcha_image_src)
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
            result[element.name] = element.to_dict()

        return result

    def get_reports(self, company_name: str):
        """
        fetch all reports for this company name
        :param company_name:
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
        response = self.session.get("https://www.bundesanzeiger.de")
        # go to the start page
        response = self.session.get("https://www.bundesanzeiger.de/pub/de/start?0")
        # perform the search
        response = self.session.get(
            f"https://www.bundesanzeiger.de/pub/de/start?0-2.-top%7Econtent%7Epanel-left%7Ecard-form=&fulltext={company_name}&area_select=&search_button=Suchen"
        )
        return self.__generate_result(response.text)


if __name__ == "__main__":
    ba = Bundesanzeiger()
    reports = ba.get_reports("Deutsche Bahn AG")
    print(reports.keys(), len(reports))
