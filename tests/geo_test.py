from deutschland.geo import Geo


def test_basic_query():
    geo = Geo()
    # top_right and bottom_left coordinates
    data = geo.fetch(
        [52.530116236589244, 13.426532801586827],
        [52.50876180448243, 13.359631043007212],
    )

    assert len(data.keys()) > 0
