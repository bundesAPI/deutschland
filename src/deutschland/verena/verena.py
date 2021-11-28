import json

from deutschland.verena.verenadownloader import VerenaDownloader
from deutschland.verena.verenaextractor import VerenaExtractor


class Verena:
    """
    Downloads and extracts the current job listings from the VERENA portal.
    """

    def get(self):
        """
        Downloads and extracts the current job listings from the VERENA portal.

        Example of the json format can be found at ./example.json
        """
        result = []
        scraped_pages = VerenaDownloader().scrape()
        for idx, page in enumerate(scraped_pages):
            extract = VerenaExtractor(page).extract()
            result = result + extract
        return result


if __name__ == "__main__":
    v = Verena()
    res = v.get()
    print(json.dumps(res))
