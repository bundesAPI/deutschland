from typing import Dict
from bs4 import BeautifulSoup

import dateparser
import requests

from deutschland import module_config, Config


class Publications:
    def __init__(self, config: Config = None):
        if config is None:
            self._config = module_config
        else:
            self._config = config

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

    def search_with_raw_params(
        self, params: Dict[str, str] = {}, proxies: Dict[str, str] = None
    ):
        """
        Searches the Publications of the Handelsregister with a given dict of parameters.

        Parameters
        ----------
        params : dict
          The parameters for the search. Detailed description below.

        Search Parameters
        -----------------
        suchart : string
          Specifies whether the search should be general or detailed.
          Either 'uneingeschr' or 'detail'.

          General searches (e.g. find all publications in all counties and all courts)
          can only include publications from the last 4 weeks.

          Detailed searches can include past publications as well, but require
          the following parameters:
          'county_code', 'court_code', and 'court_name' as well as
          either 'company_name', 'head_office_location'
          or 'registration_type' and 'registration_number'

        land : str
          The code of the county in which to search for publications.

          Valid options are:
          by: Bayern
          be: Berlin
          br: Brandenburg
          hb: Bremen
          hh: Hamburg
          he: Hessen
          mv: Mecklenburg-Vorpommern
          ni: Niedersachsen
          nw: Nordrhein-Westfalen
          rp: Rheinland-Pfalz
          sl: Saarland
          sn: Sachsen
          st: Sachsen-Anhalt
          sh: Schleswig-Holstein
          th: Thüringen

        gericht : str
          The code of the court in which to search for publications.
          Court Code + Court Name combinations can be found in 'params.md'.
          The parameters 'gericht' and 'gericht_name' must both be present.

        gericht_name : str
          The name of the court in which to search for publications.
          Court Code + Court Name combinations can be found in 'params.md'.
          This parameter must be provided together with the 'gericht'-parameter.

        vt: int
          The day of the date after which publications must have been published.

        vm: int
          The month of the date after which publications must have been published.

        vj: int
          The year of the date after which publications must have been published.

        bt: int
          The day of the date before which publications must have been published.

        bm: int
          The month of the date before which publications must have been published.

        bj: int
          The year of the date before which publications must have been published.

        fname: str
          The name of the company. Must be an exact match.

        fsitz: str
          The city where the head office of the company is located.

        rubrik: str
          The type of the company registration.
          Valid types are:
          "A", "B", "G", "V", "P", "AR"

        az: str
          The number of the company registration.

        gegenstand: int
          The type of publication to search for.

          Valid options are:
          0 : All types of publications
          1 : New registrations
          2 : Registration changes
          3 : Registrations deleted by the court
          4 : Deletion announcements
          5 : Deletions
          6 : Granted Permissions
          7 : Other procedures

        order: int
          How to order the publication results.

          Valid options are:
          1 : Registration Number
          2 : Company name
          3 : Order by creation date of publication
          4 : Order by publication date
        """

        # parameter has higher priority than member
        if proxies is None:
            if self._config is not None and self._config.proxy_config is not None:
                proxies = self._config.proxy_config

        search_params = {**self.DEFAULT_FORM_DATA, **params}

        response = requests.post(
            self.SEARCH_URL,
            data=search_params,
            headers=self.REQUEST_HEADERS,
            proxies=proxies,
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
            [pub_id, county_code] = self.__extract_pub_id_and_county_code(a)

            ul = a.find("ul")
            [info, _, published_info] = ul.contents

            company_info = self.__extract_company_info(info)
            published_at = self.__extract_published_at(published_info)

            data = {
                **{
                    "publication_id": pub_id,
                    "county_code": county_code,
                    "published_at": published_at,
                },
                **company_info,
            }

            results.append(data)

        return results

    def __extract_pub_id_and_county_code(self, link):
        [pub_id, county] = (
            link["href"]
            .replace("javascript:NeuFenster('rb_id=", "")
            .replace("')", "")
            .split("&")
        )
        county_code = county.replace("land_abk=", "")

        return [pub_id, county_code]

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
        published_at_raw = info.replace("Bekannt gemacht am: ", "")
        return dateparser.parse(published_at_raw, date_formats=["%d.%m.%Y"])
