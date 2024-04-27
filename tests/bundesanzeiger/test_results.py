from deutschland.bundesanzeiger import Bundesanzeiger


def test_results_not_empty():
    ba = Bundesanzeiger()
    reports = ba.get_reports("Deutsches Zentrum für Luft- und Raumfahrt")
    assert len(reports) > 0


def test_multiple_pages():
    ba = Bundesanzeiger()
    reports = ba.get_reports("DE000A0TGJ55", page_limit=2)

    assert len(reports) == 40
