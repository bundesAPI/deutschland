
from deutschland import autobahn
from deutschland.autobahn.api import default_api

from pprint import pprint

autobahn_api_instance = default_api.DefaultApi()

try:
    # Auflistung aller Autobahnen
    api_response = autobahn_api_instance.list_autobahnen()
    pprint(api_response)

    # Details zu einer Ladestation
    station_id = "RUxFQ1RSSUNfQ0hBUkdJTkdfU1RBVElPTl9fMTczMzM="  # str |
    api_response = autobahn_api_instance.get_charging_station(station_id)
    pprint(api_response)

except autobahn.ApiException as e:
    print("Exception when calling DefaultApi->get_charging_station: %s\n" % e)