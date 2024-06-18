import pytest
from bs4 import BeautifulSoup

from deutschland.lebensmittelwarnung import (
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
    correct_url = "https://www.lebensmittelwarnung.de/___LMW-Redaktion/RSSNewsfeed/Functions/RssFeeds/rssnewsfeed_Alle_DE.xml?nn=314268&state=berlin"
    assert url == correct_url, "WarningFeedUrl creation failed (result: " + url + ")"


def test_lebensmittelwarnung_warning_parsing():
    """
    Checks if the Warning parsing works correctly.
    """
    warning_raw_string = "<item><title>Spirit Motors Johnny Bglove Lederhandschuh Kurz</title><link>https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/06_Juni/240614_10_NW_Handschuhe/240614_NW_Handschuhe_Meldung.html</link><pubDate>Fri, 14 Jun 2024 14:12:17 +0200</pubDate><description/><guid>https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/06_Juni/240614_10_NW_Handschuhe/240614_NW_Handschuhe_Meldung.html</guid></item>"
    warning_correct = {
        "guid": "https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/06_Juni/240614_10_NW_Handschuhe/240614_NW_Handschuhe_Meldung.html",
        "pubDate": "Fri, 14 Jun 2024 14:12:17 +0200",
        "title": "Spirit Motors Johnny Bglove Lederhandschuh Kurz",
        "link": "https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/06_Juni/240614_10_NW_Handschuhe/240614_NW_Handschuhe_Meldung.html",
        "description": "",
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
    item_count = 7
    warning_raw_item = """
		<item>
		<title>Spirit Motors Johnny Bglove Lederhandschuh Kurz</title>
		<link>https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/06_Juni/240614_10_NW_Handschuhe/240614_NW_Handschuhe_Meldung.html</link>
		<pubDate>Fri, 14 Jun 2024 14:12:17 +0200</pubDate>
		<description/>
		<guid>https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/06_Juni/240614_10_NW_Handschuhe/240614_NW_Handschuhe_Meldung.html</guid>
		</item>
		<item>
		<title>Hähnchengeschnetzeltes in Champignon – Rahmsauce mit Spiralnudeln 400 Gramm</title>
		<link>https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/06_Juni/240614_12_BY_Haenchengeschnetzeltes/240614_11_BY_Haenchengeschnetzeltes.html</link>
		<pubDate>Fri, 14 Jun 2024 10:23:00 +0200</pubDate>
		<description>27.07.24: K219193; 01.08.24: K219194, K219195; 30.07.24: K226282, K226281, K232681</description>
		<guid>https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/06_Juni/240614_12_BY_Haenchengeschnetzeltes/240614_11_BY_Haenchengeschnetzeltes.html</guid>
		</item>
		<item>
		<title>Alpina Nylon Küchenzubehör</title>
		<link>https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/06_Juni/240610_08_NW_Kuechenzubehoer/240610_NW_Kuechenzubehoer_Meldung.html</link>
		<pubDate>Mon, 10 Jun 2024 16:00:00 +0200</pubDate>
		<description>alle</description>
		<guid>https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/06_Juni/240610_08_NW_Kuechenzubehoer/240610_NW_Kuechenzubehoer_Meldung.html</guid>
		</item>
		<item>
		<title>Diverse Salamiprodukte</title>
		<link>https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/06_Juni/240607_07_SH_diverse_Salamiprodukte/240607_1_SH_diverse_Salamiprodukte.html</link>
		<pubDate>Mon, 10 Jun 2024 07:12:12 +0200</pubDate>
		<description/>
		<guid>https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/06_Juni/240607_07_SH_diverse_Salamiprodukte/240607_1_SH_diverse_Salamiprodukte.html</guid>
		</item>
		<item>
		<title>Gel Mouse Pad</title>
		<link>https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/06_Juni/240606_05_NW_Mousepad/240606_NW_Mousepad_Meldung.html</link>
		<pubDate>Thu, 6 Jun 2024 11:23:00 +0200</pubDate>
		<description/>
		<guid>https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/06_Juni/240606_05_NW_Mousepad/240606_NW_Mousepad_Meldung.html</guid>
		</item>
		<item>
		<title>Thüringer Knacker 4x75g (300g)</title>
		<link>https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/06_Juni/240605_03_TH_Thueringer_Knacker/240605_TH_Thueringer_Knacker.html</link>
		<pubDate>Wed, 5 Jun 2024 10:12:00 +0200</pubDate>
		<description>982203</description>
		<guid>https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/06_Juni/240605_03_TH_Thueringer_Knacker/240605_TH_Thueringer_Knacker.html</guid>
		</item>
		<item>
		<title>Honig Herbal Paste</title>
		<link>https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/05_Mai/240529_6_BW_Honig_Paste/240529_6_BW_Honig_Paste.html</link>
		<pubDate>Wed, 29 May 2024 19:00:00 +0200</pubDate>
		<description>Alle Chargen</description>
		<guid>https://www.lebensmittelwarnung.de/___lebensmittelwarnung.de/Meldungen/2024/05_Mai/240529_6_BW_Honig_Paste/240529_6_BW_Honig_Paste.html</guid>
		</item>
	"""
    warning_raw_pre = "<rss><channel>"
    warning_raw_post = "</channel></rss>"
    warning_raw = warning_raw_pre + (warning_raw_item) + warning_raw_post
    feed = WarningFeed(warning_raw).get_output()
    assert (
        len(feed) == item_count
    ), "WarningFeed parsing failed, it created too few warning dictionaries."
