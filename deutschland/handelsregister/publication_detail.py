from datetime import datetime
from typing import Dict

from bs4 import BeautifulSoup
import dateparser
import requests

from deutschland import module_config, Config


class PublicationDetail:
    def __init__(self, config: Config = None):
        if config is None:
            self._config = module_config
        else:
            self._config = config

    DETAIL_URL = "https://www.handelsregisterbekanntmachungen.de/skripte/hrb.php?rb_id={}&land_abk={}"

    REQUEST_HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "de",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "www.handelsregisterbekanntmachungen.de",
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

    def get_detail(
        self, publication_id: str, county_code: str, proxies: Dict[str, str] = None
    ):
        """
        Get the details of a publication with its identifier and county code.

        Parameters
        ----------
        publication_id : str
          The identifier of the publication.
          It is usually a 6 to 7 digit number.

        county_code : str
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
        """

        # parameter has higher priority than member
        if proxies is None:
            if self._config is not None and self._config.proxy_config is not None:
                proxies = self._config.proxy_config

        request_url = self.DETAIL_URL.format(publication_id, county_code)
        response = requests.get(
            request_url, headers=self.REQUEST_HEADERS, proxies=proxies
        )

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        return self.__extract_details(soup)

    def __extract_details(self, soup):
        table = soup.find("table")
        if table is None:
            return None

        trs = table.find_all("tr")

        [
            court,
            reg_type,
            reg_num,
            published_at,
        ] = self.__extract_registration_and_published_info(trs[0])

        pub_type = self.__extract_publication_type(trs[2])
        decided_on = self.__extract_decided_on(trs[3])
        pub_text = self.__extract_publication_text(trs[5])

        return {
            "court": court,
            "registration_type": reg_type,
            "registration_number": reg_num,
            "decided_on": decided_on,
            "published_at": published_at,
            "publication_type": pub_type,
            "publication_text": pub_text,
        }

    def __extract_registration_and_published_info(self, row):
        tds = row.find_all("td")

        [court_info, reg_info] = tds[0].find("u").text.split(" Aktenzeichen: ")
        court = court_info.replace("Amtsgericht ", "")
        [reg_type, reg_num] = reg_info.strip().split(" ")

        published_at_raw = (
            tds[1]
            .find("nobr")
            .text.replace("Bekannt gemacht am: ", "")
            .replace(" Uhr", "")
        )

        published_at = dateparser.parse(
            published_at_raw, date_formats=["%d.%m.%Y %H:%M"]
        )

        return [court, reg_type, reg_num, published_at]

    def __extract_publication_type(self, row):
        [_, pub_type] = row.find("td").contents

        return pub_type

    def __extract_decided_on(self, row):
        [_, decided_on_raw] = row.find("td").contents
        decided_on = dateparser.parse(decided_on_raw, date_formats=["%d.%m.%Y"])

        return decided_on

    def __extract_publication_text(self, row):
        [_, pub_text] = row.find("td").contents

        return pub_text
