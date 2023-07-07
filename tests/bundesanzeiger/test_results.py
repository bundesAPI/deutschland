from deutschland.bundesanzeiger import Bundesanzeiger


def test_results_not_empty():
    ba = Bundesanzeiger()
    reports = ba.get_reports(
        "Deutsches Zentrum für Luft- und Raumfahrt", disable_manual_input=True
    )
    assert len(reports) > 0


def test_multiple_entries():
    ba = Bundesanzeiger()
    reports = ba.get_reports("DE000A0TGJ55", disable_manual_input=True)

    assert len(reports) > 1
