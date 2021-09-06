import requests
from bs4 import BeautifulSoup
from typing import List, Dict

class WarningFeedUrl:
    """
    Constructs a warning feed url from $content & $region with create()

    Result format: https://www.lebensmittelwarnung.de/bvl-lmw-de/opensaga/feed/{content}/{region}.rss"
    """
    SOURCE_STRING = "https://www.lebensmittelwarnung.de/bvl-lmw-de/opensaga/feed/{0}/{1}.rss"

    @classmethod
    def create(self, content: str, region: str) -> str:
        return self.SOURCE_STRING.format(content, region)

class WarningFeed:
    """
    Downloads & parses a RSS feed based on a WarningFeedUrl. Url provided at init(), get result with get_output().
    """

    def __init__(self, url: str):
        self.url = url
        self.output = []
        self.__parse()

    def get_output(self) -> List[Dict]:
        return self.output

    def __parse(self) -> None:
        # TODO proper error handling
        rss_soup = BeautifulSoup(self.__download(), 'xml')
        warnings = rss_soup.find_all('item')
        for warning_raw in warnings:
            self.output.append(Warning(warning_raw).get_warning())
            
    def __download(self) -> str:
        # TODO proper error handling
        req = requests.get(self.url)
        return req.text

class Warning:
    """
    Parses a single warning. Raw warning provided at init(), get result with get_warning().
    """

    def __init__(self, warning_raw):
        self.dict = {}
        self.__parse(warning_raw)

    def __parse(self, warning_raw) -> str:
        guid = warning_raw.find('guid').text
        self.dict['id'] = int(guid.split('/')[-1])
        self.dict['guid'] = guid
        self.dict['pubDate'] = warning_raw.find('pubDate').text
        
        cdata_soup = BeautifulSoup(warning_raw.find('content:encoded').text, 'html.parser')
        content_attrs = cdata_soup.find_all('b')
        for attr in content_attrs:
            attr_name = attr.text
            attr_value = str(attr.next_sibling).strip()
            if(attr_name == "Produktbezeichnung:"):
                self.dict['title'] = attr_value
            elif(attr_name == "Typ:"):
                self.dict['manufacturer'] = attr_value
            elif(attr_name == "Grund der Warnung:"):
                self.dict['warning'] = attr_value
            elif(attr_name == "Betroffene Länder:"):
                affected_arr = [x.strip() for x in attr_value.split(',')]
                self.dict['affectedStates'] = affected_arr
    
    def get_warning(self) -> dict:
        return self.dict
    
class Lebensmittelwarnung:
    """
    A tool to scrape the database of product warnings of the german "Bundesamt für Verbraucherschutz und Lebensmittelsicherheit".

    The database can also be found here: https://www.lebensmittelwarnung.de/bvl-lmw-de/
    """

    def get(self, content:str="alle", region:str="alle_bundeslaender") -> List[Dict]:
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
        url = WarningFeedUrl.create(content,region)
        feed = WarningFeed(url)
        return feed.get_output()

if __name__ == "__main__":
    lw = Lebensmittelwarnung()
    # res = hr.search(keywords="Deutsche Bahn Aktiengesellschaft", keyword_match_option=3)
    res = lw.get()
    print(res)

