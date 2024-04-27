from deutschland.bundesanzeiger import Bundesanzeiger


def test_get_next_page_link():
    with open('response.html') as file:
        ba = Bundesanzeiger()
        html = file.read()
        link = ba._Bundesanzeiger__get_next_page_link(html)
        assert link == 'https://www.bundesanzeiger.de/pub/de/suchen2?4-1.-top~nav-pager-navigation-1-pagination~link'
