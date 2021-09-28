from deutschland.verena.verena import Verena


def test_verena():
    v = Verena()
    res = v.get()
    assert (
        len(res) > 0
    ), "Scraping and extracting all pages of the VERENA portal eturned 0 results. It very likely shouldn't."
