import os
from deutschland.bundesanzeiger import Bundesanzeiger


def test_get_next_page_link():
    html_file = os.path.join(os.path.dirname(__file__), "response.html")
    with open(html_file) as file:
        html = file.read()
    ba = Bundesanzeiger()
    link = ba._Bundesanzeiger__get_next_page_link(html)
    expected = "https://www.bundesanzeiger.de/pub/de/suchen2?4-1.-top~nav-pager-navigation-1-pagination~link"
    assert link == expected
