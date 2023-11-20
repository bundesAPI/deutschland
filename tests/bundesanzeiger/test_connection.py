import pytest
from deutschland.bundesanzeiger import Bundesanzeiger


def test_exception_on_invalid_http_code():
    ba = Bundesanzeiger()
    with pytest.raises(ConnectionError):
        ba._Bundesanzeiger__get_response("https://httpstat.us/500")
        ba._Bundesanzeiger__get_response("https://httpstat.us/503")
        ba._Bundesanzeiger__get_response("https://httpstat.us/404")


def test_get_response():
    ba = Bundesanzeiger()
    assert (
        ba._Bundesanzeiger__get_response("https://httpstat.us/200").status_code == 200
    )
