from typing import Dict, List

import requests
from bs4 import BeautifulSoup
from bs4.element import PageElement


class WarningFeedUrl:
    """
    Constructs a warning feed url from $content & $region with create()

    Result format: https://www.lebensmittelwarnung.de/bvl-lmw-de/opensaga/feed/{content}/{region}.rss"
    """

    VALID_CONTENT_SELECTORS = [
        "alle",
        "lebensmittel",
        "kosmetischemittel",
        "bedarfsgegenstaende",
        "mittelzumtaetowieren",
        "babyundkinderprodukte",
    ]

    VALID_REGION_SELECTORS = [
        "alle_bundeslaender",
        "badenwuerttemberg",
        "bayern",
        "berlin",
        "brandenburg",
        "bremen",
        "hamburg",
        "hessen",
        "mecklenburgvorpommern",
        "niedersachsen",
        "nordrheinwestfalen",
        "rheinlandpfalz",
        "saarland",
        "sachsen",
        "sachsenanhalt",
        "schleswigholstein",
        "thueringen",
    ]

    SOURCE_STRING = "https://www.lebensmittelwarnung.de/___LMW-Redaktion/RSSNewsfeed/Functions/RssFeeds/rssnewsfeed_Alle_DE.xml?nn=314268{0}{1}"

    def __init__(self, content: str, region: str):
        if (
            content in self.VALID_CONTENT_SELECTORS
            and region in self.VALID_REGION_SELECTORS
        ):
            if content == "alle":
                content = ""
            else:
                content = f"&type={content}"

            if region == "alle_bundeslaender":
                region = ""
            else:
                region = f"&state={region}"

            self.url = self.SOURCE_STRING.format(content, region)
        else:
            raise ValueError(
                'Provided argument for content "'
                + content
                + '" or region "'
                + region
                + '" was not a valid selector. Please refer to the documentation for a list of valid selectors.'
            )

    def get_url(self):
        return self.url


class WarningFeed:
    """
    Parses a RSS feed based on a WarningFeedUrl.
    If url is provided at init_from_url(), feed str is downloaded.
    If str is provided at __init__, str is used.
    Get result with get_output().
    """

    @classmethod
    def init_from_url(cls, url: WarningFeedUrl):
        feed = cls.__download(url.get_url())
        return cls(feed)

    def __init__(self, feed: str):
        self.output = []
        self.__parse(feed)

    def get_output(self) -> List[Dict]:
        return self.output

    def __parse(self, feed: str) -> None:
        rss_soup = BeautifulSoup(feed, "xml")
        warnings = rss_soup.find_all("item")
        for warning_raw in warnings:
            self.output.append(Warning(warning_raw).get_warning())

    @staticmethod
    def __download(url) -> str:
        req = requests.get(url)
        if req.status_code == 200:
            return req.text
        else:
            # otherwise, the error message's html will be parsed, leading to empty result set.
            raise ConnectionError(
                "The request to with url "
                + req.url
                + " returned with status code and content:"
                + str(req.status_code)
                + " -> "
                + req.text
            )


class Warning:
    """
    Parses a single warning. Raw warning provided at init(), get result with get_warning().
    """

    def __init__(self, warning_raw: PageElement):
        self.dict = {}
        self.__parse(warning_raw)

    def __parse(self, warning_raw: PageElement) -> str:
        guid = warning_raw.find("guid").text
        self.dict["guid"] = guid
        self.dict["pubDate"] = warning_raw.find("pubDate").text
        self.dict["description"] = warning_raw.find("description").text
        self.dict["link"] = guid
        self.dict["title"] = warning_raw.find("title").text

    def get_warning(self) -> dict:
        return self.dict


class Lebensmittelwarnung:
    """
    A tool to scrape the database of product warnings of the german "Bundesamt für Verbraucherschutz und Lebensmittelsicherheit".

    The database can also be found here: https://www.lebensmittelwarnung.de/bvl-lmw-de/
    """

    def get(
        self, content: str = "alle", region: str = "alle_bundeslaender"
    ) -> List[Dict]:
        """
        content : str
            Selector for what type of product warning (food, cosmetics, ...)
            default: "alle" (all)
        region : str
            Selector for the region the product warning has been released for
            default: "alle_bundeslaender" (all)

        Returns all matching product warnings as List[Dict].

        All valid selector values can be found at ./params.md
        """
        url = WarningFeedUrl(content, region)
        feed = WarningFeed.init_from_url(url)
        return feed.get_output()


if __name__ == "__main__":
    lw = Lebensmittelwarnung()
    res = lw.get()
    print(res)
