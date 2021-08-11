import requests
import re

from bs4 import BeautifulSoup


class Handelsregister:
    SEARCH_URL = "https://www.handelsregister.de/rp_web/mask.do?Typ=e"

    REQUEST_HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "DNT": "1",
        "Host": "www.handelsregister.de",
        "Origin": "https://www.handelsregister.de",
        "Referer": "https://www.handelsregister.de/rp_web/mask.do?Typ=e",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "sec-gpc": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    }

    DEFAULT_FORM_DATA = {
        "bundeslandBW": "on",
        "bundeslandBY": "on",
        "bundeslandBE": "on",
        "bundeslandBR": "on",
        "bundeslandHB": "on",
        "bundeslandHH": "on",
        "bundeslandHE": "on",
        "bundeslandMV": "on",
        "bundeslandNI": "on",
        "bundeslandNW": "on",
        "bundeslandRP": "on",
        "bundeslandSL": "on",
        "bundeslandSN": "on",
        "bundeslandST": "on",
        "bundeslandSH": "on",
        "bundeslandTH": "on",
        "schlagwoerter": None,
        "schlagwortOptionen": 2,
        "suchOptionenAehnlich": False,
        "niederlassung": None,
        "suchOptionenGeloescht": False,
        "suchOptionenNurZNneuenRechts": False,
        "suchTyp": "e",
        "registerArt": None,
        "registerNummer": None,
        "registergericht": None,
        "rechtsform": None,
        "postleitzahl": None,
        "ort": None,
        "strasse": None,
        "ergebnisseProSeite": "10",
        "btnSuche": "Suchen",
    }

    def search(self, params={}):
        search_params = {**self.DEFAULT_FORM_DATA, **params}
        response = requests.post(
            self.SEARCH_URL, data=search_params, headers=self.REQUEST_HEADERS
        )
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        return self.__find_entries(soup)

    def __find_entries(self, soup):
        table = soup.find("table", class_="RegPortErg")
        if table is None:
            return []

        trs = table.find_all("tr")

        results = []
        next_entry = {}

        # Skip the first row, which is the header row
        for tr in trs[1:]:
            if tr.find("td", class_="RegPortErg_AZ"):
                data = self.__extract_county_court_and_registration(tr)

                # Save the current entry since we reached the next entry
                # demarcated by the .RegPortErg_AZ table cell.
                if next_entry:
                    results.append(next_entry.copy())

                next_entry = data
            elif tr.find("td", class_="RegPortErg_FirmaKopf"):
                data = self.__extract_name_location_and_state(tr)
                next_entry.update(data)

        return results

    def __extract_county_court_and_registration(self, row):
        td = row.find("td", class_="RegPortErg_AZ")
        county = td.contents[2].strip()
        court_and_registration = (
            td.contents[3].text.strip().replace("\n", " ").replace("\t", "").split()
        )
        court = " ".join(court_and_registration[:-2])
        [reg_type, reg_num] = court_and_registration[-2:]

        return {
            "county": county,
            "court": court,
            "registration_type": reg_type,
            "registration_number": reg_num,
        }

    def __extract_name_location_and_state(self, row):
        tds = row.find_all("td")
        name = tds[1].text.strip()
        location = tds[2].text.strip()
        state = tds[3].text.strip()

        return {"company_name": name, "location": location, "state": state}


if __name__ == "__main__":
    hr = Handelsregister()
    foo = hr.search({"ort": "Köln"})
    print(foo)
