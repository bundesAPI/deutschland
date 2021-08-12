from deutschland import Bundesanzeiger
from deutschland import Handelsregister


def test_for_no_data_deutsche_bahn_ag():
    ba = Bundesanzeiger()
    data = ba.get_reports("Deutsche Bahn AG")
    assert len(data.keys()) > 0, "Found no reports for Deutsche Bahn AG"


def test_for_no_data_handelsregister():
    hr = Handelsregister()
    data = hr.search(keywords="foobar", keyword_match_option=3)
    assert (
        len(data) == 0
    ), "Found registered companies for 'foobar' although none were expected."


def test_fetching_handelsregister_data_for_deutsche_bahn_ag():
    hr = Handelsregister()
    data = hr.search(
        keywords="Deutsche Bahn Aktiengesellschaft", keyword_match_option=3
    )
    assert (
        len(data) > 0
    ), "Found no data for 'Deutsche Bahn Aktiengesellschaft' although it should exist."
