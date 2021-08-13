from typing import Dict
from bs4 import BeautifulSoup


import dateparser
import requests


class Publications:
    REQUEST_HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "de",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "dnt": "1",
        "Host": "www.handelsregisterbekanntmachungen.de",
        "Origin": "https://www.handelsregisterbekanntmachungen.de",
        "Referer": "https://www.handelsregisterbekanntmachungen.de/?aktion=suche",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "sec-gpc": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    }

    SEARCH_URL = "https://www.handelsregisterbekanntmachungen.de/?aktion=suche"

    DEFAULT_FORM_DATA = {
        "suchart": "uneingeschr",
        "land": None,
        "gericht": None,
        "gericht_name": None,
        "seite": None,
        "l": None,
        "r": None,
        "all": False,
        "vt": None,
        "vm": None,
        "vj": None,
        "bt": None,
        "bm": None,
        "bj": None,
        "fname": None,
        "fsitz": None,
        "rubrik": None,
        "az": None,
        "gegenstand": 0,
        "order": 4,
        "button": "Suche starten",
    }

    def search_with_raw_params(self, params: Dict[str, str] = {}):
        search_params = {**self.DEFAULT_FORM_DATA, **params}

        response = requests.post(
            self.SEARCH_URL, data=search_params, headers=self.REQUEST_HEADERS
        )
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        return self.__find_entries(soup)

    def __find_entries(self, soup):
        content = soup.find("div", id="inhalt")
        lis = content.find_all("li")

        results = []

        for li in lis:
            a = li.find("a")
            [reg_id, county_code] = self.__extract_reg_id_and_county_code(a)

            ul = a.find("ul")
            [info, _, published_info] = ul.contents

            company_info = self.__extract_company_info(info)
            published_at = self.__extract_published_at(published_info)

            data = {
                **{
                    "registration_id": reg_id,
                    "county_code": county_code,
                    "published_at": published_at,
                },
                **company_info,
            }

            results.append(data)

        return results

    def __extract_reg_id_and_county_code(self, link):
        [reg_id, county] = (
            link["href"]
            .removeprefix("javascript:NeuFenster('rb_id=")
            .removesuffix("')")
            .split("&")
        )
        county_code = county.removeprefix("land_abk=")

        return [reg_id, county_code]

    def __extract_company_info(self, text):
        branch_name = None

        fields = text.split(",")
        if len(fields) == 3:
            [company_name, court, reg_info] = fields
        elif len(fields) == 4:
            [company_name, branch_name, court, reg_info] = fields
        else:
            raise Exception(f"Could not parse publication info: '{text}'.")

        [reg_type, reg_num] = reg_info.strip().split(" ")

        return {
            "company_name": company_name.strip(),
            "court": court.strip(),
            "branch_name": branch_name.strip() if branch_name else None,
            "registration_type": reg_type.strip(),
            "registration_number": reg_num.strip(),
        }

    def __extract_published_at(self, info):
        published_at_raw = info.removeprefix("Bekannt gemacht am: ")
        return dateparser.parse(published_at_raw, date_formats=["%d.%m.%Y"])
