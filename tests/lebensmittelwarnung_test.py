import pytest
from bs4 import BeautifulSoup

from deutschland.lebensmittelwarnung.lebensmittelwarnung import (
    Lebensmittelwarnung,
    Warning,
    WarningFeed,
    WarningFeedUrl,
)


def test_lebensmittelwarnung_all_content_types_all_regions():
    """
    Checks if any results are returned without search limitations. (There probably should be.)
    """
    lw = Lebensmittelwarnung()
    data = lw.get()
    assert (
        len(data) > 0
    ), "Found no data in the Lebensmittelwarnung DB without search limitations, although there (probably) should be."


def test_lebensmittelwarnung_invalid_content_type_invalid_region():
    """
    Checks if the selector input validation is working.
    """
    lw = Lebensmittelwarnung()
    with pytest.raises(ValueError):
        data = lw.get("wrong", "selector")


def test_lebensmittelwarnung_warningfeed_with_invalid_content_invalid_region():
    """
    Checks if an Error is raised of the response status code is not 400.
    To simulate this, input validation is skipped by using WarningFeed() directly.
    """
    wrong_url = (
        "https://www.lebensmittelwarnung.de/bvl-lmw-de/opensaga/feed/abc/xyz.rss"
    )
    with pytest.raises(ConnectionError):
        feed = WarningFeed._WarningFeed__download(wrong_url)


def test_lebensmittelwarnung_warningfeedurl_create():
    """
    Checks if the WarningFeedUrl() works correctly.
    """
    url = WarningFeedUrl("alle", "berlin").get_url()
    correct_url = (
        "https://www.lebensmittelwarnung.de/bvl-lmw-de/opensaga/feed/alle/berlin.rss"
    )
    assert url == correct_url, "WarningFeedUrl creation failed (result: " + url + ")"


def test_lebensmittelwarnung_warning_parsing():
    """
    Checks if the Warning parsing works correctly.
    """
    warning_raw_string = '<item> <title>TITLE</title> <link>https://www.lebensmittelwarnung.de/bvl-lmw-de/detail/lebensmittel/1</link> <description><![CDATA[<img src="IMG_URL" width="100" /><br/> <b>Produktbezeichnung:</b> TITLE<br/> <b>Typ:</b> TYPE<br/> <b>Hersteller (Inverkehrbringer):</b> MANUFACTURER<br/> <b>Grund der Warnung:</b> WARNING<br/> <b>Betroffene Länder:</b> STATE A, STATE B<br/> ]]></description> <content:encoded><![CDATA[<img src="IMG_URL" width="100" /><br/> <b>Produktbezeichnung:</b> TITLE<br/> <b>Typ:</b> TYPE<br/> <b>Hersteller (Inverkehrbringer):</b> MANUFACTURER<br/> <b>Grund der Warnung:</b> WARNING<br/> <b>Betroffene Länder:</b> STATE A, STATE B<br/> ]]></content:encoded> <pubDate>Wed, 08 Sep 2021 10:00:00 +0000</pubDate> <guid>https://www.lebensmittelwarnung.de/bvl-lmw-de/detail/lebensmittel/1</guid> </item>'
    warning_correct = {
        "id": 1,
        "guid": "https://www.lebensmittelwarnung.de/bvl-lmw-de/detail/lebensmittel/1",
        "pubDate": "Wed, 08 Sep 2021 10:00:00 +0000",
        "imgSrc": "IMG_URL",
        "title": "TITLE",
        "type": "TYPE",
        "manufacturer": "MANUFACTURER",
        "warning": "WARNING",
        "affectedStates": ["STATE A", "STATE B"],
    }
    warning_raw = BeautifulSoup(warning_raw_string, "xml").find("item")
    warning = Warning(warning_raw).get_warning()
    assert warning_correct == warning, (
        "Warning parsing failed (result: " + str(warning) + ")"
    )


def test_lebensmittelwarnung_warningfeed_parsing():
    """
    Checks if the WarningFeed parsing works correctly.
    """
    item_count = 5
    warning_raw_item = '<item> <title>TITLE</title> <link>https://www.lebensmittelwarnung.de/bvl-lmw-de/detail/lebensmittel/1</link> <description><![CDATA[<img src="IMG_URL" width="100" /><br/> <b>Produktbezeichnung:</b> TITLE<br/> <b>Typ:</b> TYPE<br/> <b>Hersteller (Inverkehrbringer):</b> MANUFACTURER<br/> <b>Grund der Warnung:</b> WARNING<br/> <b>Betroffene Länder:</b> STATE A, STATE B<br/> ]]></description> <content:encoded><![CDATA[<img src="IMG_URL" width="100" /><br/> <b>Produktbezeichnung:</b> TITLE<br/> <b>Typ:</b> TYPE<br/> <b>Hersteller (Inverkehrbringer):</b> MANUFACTURER<br/> <b>Grund der Warnung:</b> WARNING<br/> <b>Betroffene Länder:</b> STATE A, STATE B<br/> ]]></content:encoded> <pubDate>Wed, 08 Sep 2021 10:00:00 +0000</pubDate> <guid>https://www.lebensmittelwarnung.de/bvl-lmw-de/detail/lebensmittel/1</guid> </item>'
    warning_raw_pre = "<rss><channel>"
    warning_raw_post = "</channel></rss>"
    warning_raw = warning_raw_pre + (warning_raw_item * item_count) + warning_raw_post
    print(warning_raw)
    feed = WarningFeed(warning_raw).get_output()
    assert (
        len(feed) == item_count
    ), "WarningFeed parsing failed, it created too few warning dictionaries."
