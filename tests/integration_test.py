import datetime
from deutschland.bundesnetzagentur import Rufzeichen
from deutschland.bundeswahlleiter import Bundeswahlleiter
from deutschland.handelsregister import Handelsregister


def test_fetching_publications_for_deutsche_bank():
    hr = Handelsregister()
    data = hr.search_publications(
        company_name="Deutsche Bank",
        county_code="he",
        court_code="M1201",
        court_name="Frankfurt am Main",
        detailed_search=True,
    )
    assert len(data) > 0, "Found no data for 'Deutsche Bank' although it should exist."


def test_fetching_publication_detail():
    hr = Handelsregister()
    data = hr.get_publication_detail(publication_id="896236", county_code="bw")
    assert data, "Found no publication detail data although it should exist."
    assert data["court"] == "Freiburg"
    assert data["registration_type"] == "HRB"
    assert data["registration_number"] == "719927"
    assert data["decided_on"] == datetime.datetime(2021, 8, 6, 0, 0)
    assert data["published_at"] == datetime.datetime(2021, 8, 6, 9, 45)
    assert data["publication_type"] == "Löschungen"
    assert data["publication_text"].startswith("HRB 719927:")


def test_no_data_for_publication_detail():
    hr = Handelsregister()
    data = hr.get_publication_detail(publication_id="9999999999999", county_code="bw")
    assert data is None


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
