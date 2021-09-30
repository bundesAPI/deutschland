import requests
from bs4 import BeautifulSoup


class Rufzeichen(object):
    def get(self, callsign):
        """
        Gibt informationen über den Inhaber sowie Lizenzklasse und Betriebsort
        eines Amateurfunkrufzeichens zurück.
        """
        r = requests.get("https://ans.bundesnetzagentur.de/amateurfunk/Rufzeichen.aspx")
        soup = BeautifulSoup(r.text, "html.parser")

        r = requests.post(
            "https://ans.bundesnetzagentur.de/amateurfunk/Rufzeichen.aspx",
            data={
                "__EVENTTARGET": soup.find("input", {"name": "__EVENTTARGET"})["value"],
                "__VIEWSTATE": soup.find("input", {"name": "__VIEWSTATE"})["value"],
                "__VIEWSTATEGENERATOR": soup.find(
                    "input", {"name": "__VIEWSTATEGENERATOR"}
                )["value"],
                "__EVENTVALIDATION": soup.find("input", {"name": "__EVENTVALIDATION"})[
                    "value"
                ],
                "Text1": callsign,
                "Bt_Suche": "Suche starten",
            },
        )
        soup = BeautifulSoup(r.text, "html.parser")
        try:
            rufzeichen, klasse, _, inhaber, betriebsort = map(
                lambda a: a.text.strip(),
                soup.find("table", {"id": "DG_RZ"}).find_all("tr")[1].find_all("td"),
            )
            return {
                "rufzeichen": rufzeichen,
                "klasse": klasse,
                "inhaber": inhaber,
                "betriebsort": betriebsort,
            }
        except IndexError:
            return None
