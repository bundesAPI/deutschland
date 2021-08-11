from deutschland import Bundesanzeiger


def test_for_no_data_deutsche_bahn_ag():
    ba = Bundesanzeiger()
    data = ba.get_reports("Deutsche Bahn AG")
    assert len(data.keys()) > 0, "Found no reports for Deutsche Bahn AG"
