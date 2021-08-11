import requests

from bs4 import BeautifulSoup


class Handelsregister:
    SEARCH_URL = "https://www.handelsregister.de/rp_web/mask.do?Typ=e"

    VALID_COUNTY_CODES = [
        "BW",
        "BY",
        "BE",
        "BR",
        "HB",
        "HH",
        "HE",
        "MV",
        "NI",
        "NW",
        "RP",
        "SL",
        "SN",
        "ST",
        "SH",
        "TH",
    ]

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
        "ergebnisseProSeite": "100",
        "btnSuche": "Suchen",
    }

    def search(self, params, counties=[]):
        """Searches the Handelsregister with a given set of parameters in all given counties (optional).

        Parameters
        ----------
        params : dict
          The parameters for the search. Detailed description below.

        counties : list, optional
          The counties (bundeslaender) in which we should search.
          If not provided, all counties are searched.
          Valid values are:
          BW, BY, BE, BR, HB, HH, HE, MV, NI, NW, RP, SL, SN, ST, SH, TH

        Search Parameters
        -----------------
        schlagwoerter : string
          One or space-separated Keywords like e.g. the company name.

        schlagwortOptionen : int
          Options for the 'schlagwoerter' parameter.
          1 : Match must contain all keywords.
          2 : Match must contain at least one keyword.
          3 : Match's company name must equal the keyword(s).

        suchOptionenAehnlich : bool
          Match can contain similar keywords as specified in 'schlagwoerter'.

        niederlassung : string
          Location of the company.

        suchOptionenGeloescht : bool
          Search also for deleted companies.

        suchOptionenNurZNneuenRechts : bool
          Search only for deleted 'Zweigniederlassungen'.
          More info here: https://www.handelsregister.de/rp_web/help.do?Thema=zweigniederlassungen

        registerArt : string
          Type of company registration.
          Possible values: HRA, HRB, GnR, PR, VR

        registerNummer : string
          The registration number of the company.

        registergericht : string
          The district court where the company is registered.

        rechtsform : int
          The legal form of the company.
          Possible values can be found in 'params.md'.

        postleitzahl : string
          The postal code of the company.

        ort : string
          The city of the company address.

        strasse : string
          The street of the company address.

        ergebnisseProSeite : int
          How many matches to return. Defaults to 100.
        """
        search_params = {**self.DEFAULT_FORM_DATA, **params}

        for code in counties:
            if code not in self.VALID_COUNTY_CODES:
                raise Exception(f"{code} is not a valid county code.")

            search_params[f"bundesland{code}"] = "on"

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
            elif tr.find("td", class_="RegPortErg_HistorieZn"):
                data = self.__extract_history(tr)
                next_entry.setdefault("history", []).append(data)

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

    def __extract_history(self, row):
        tds = row.find_all("td")
        [position, historical_name] = tds[1].text.strip().split(".) ", 1)
        historical_location = tds[2].text.strip().split(".) ", 1)[1]

        return {
            "position": position,
            "historical_name": historical_name,
            "historical_location": historical_location,
        }


if __name__ == "__main__":
    hr = Handelsregister()
    res = hr.search({"ort": "Köln", "ergebnisseProSeite": 10}, ["AB"])
    print(res)
