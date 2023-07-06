import datetime

from deutschland.bundesnetzagentur import Rufzeichen
from deutschland.bundeswahlleiter import Bundeswahlleiter


def test_callsign():
    rz = Rufzeichen()
    data = rz.get("DL*MIC")
    assert data["klasse"] == "A", "No valid callsign data returned"


def test_bundeswahlleiter():
    bwl = Bundeswahlleiter()
    results1998 = bwl.load_results(1998)
    results2017 = bwl.load_results(2017)
    results2021 = bwl.load_results(2021)
    # results contain rows for each Wahlkreis, Bundesland and the Bund
    assert len(results1998) == 328 + 16 + 1
    assert len(results2017) == 299 + 16 + 1
    assert len(results2021) == 299 + 16 + 1
