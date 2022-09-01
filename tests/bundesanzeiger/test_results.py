from deutschland.bundesanzeiger import Bundesanzeiger


def test_results_not_empty():
    ba = Bundesanzeiger()
    reports = ba.get_reports("Deutsches Zentrum für Luft- und Raumfahrt")
    assert len(reports) > 0
