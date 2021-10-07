from deutschland.verena.verenadownloader import VerenaDownloader


def test_downloader_page_count():
    vd = VerenaDownloader()
    res = vd.scrape()
    assert (
        len(res) > 0
    ), "Scraping all pages of the VERENA portal (block size 100) returned 0 pages. It very likely shouldn't."


def test_downloader_page_content():
    vd = VerenaDownloader()
    res = vd.scrape()
    any_empty = False
    for x in res:
        if len(x) == 0:
            any_empty = True
    assert (
        not any_empty
    ), "Scraping all pages of the Verena portal returned a empty page len(sourcecode) == 0."


def test_downloader__generate_all_listing_urls_content():
    vd = VerenaDownloader()
    valid_url = "https://www.schulministerium.nrw.de/BiPo/Verena/angebote?action=999.999999&seite=a1&suchid=12345"
    action_id = "999.999999"
    search_id = "12345"
    opening_count = 10
    urls = vd._VerenaDownloader__generate_all_listing_urls(
        action_id, search_id, opening_count
    )
    assert (
        urls[0] == valid_url
    ), "Generating the urls used to request all listing pages failed. Listing urls are malformed."


def test_downloader__generate_all_list_urls_count():
    vd = VerenaDownloader()
    action_id = "999.999999"
    search_id = "12345"
    opening_count = 650
    urls = vd._VerenaDownloader__generate_all_listing_urls(
        action_id, search_id, opening_count
    )
    assert len(urls) == 7, (
        "Generating the urls used to request all listing pages failed. There are to few or too many urls generated. Expected: 7, Generated:  "
        + int(len(urls))
    )
