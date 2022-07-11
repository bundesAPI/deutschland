[![PyPI version deutschland](https://badge.fury.io/py/deutschland.svg)](https://pypi.python.org/pypi/deutschland/)
[![GitHub license](https://img.shields.io/github/license/bundesAPI/deutschland.svg)](https://github.com/bundesAPI/deutschland/blob/main/LICENSE)

[![Lint](https://github.com/bundesAPI/deutschland/actions/workflows/black.yml/badge.svg?branch=main)](https://github.com/bundesAPI/deutschland/actions/workflows/black.yml)
[![Publish Python 🐍 distributions 📦 to PyPI and TestPyPI](https://github.com/bundesAPI/deutschland/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/bundesAPI/deutschland/actions/workflows/publish.yml)
[![Run Python 🐍 tests](https://github.com/bundesAPI/deutschland/actions/workflows/runtests.yml/badge.svg?branch=main)](https://github.com/bundesAPI/deutschland/actions/workflows/runtests.yml)

# Deutschland
A python package that gives you easy access to the most valuable datasets of Germany.

## Installation
```bash
pip install deutschland
```

## Geographic data
Fetch information about streets, house numbers, building outlines, …

```python
from deutschland import Geo
geo = Geo()
# top_right and bottom_left coordinates
data = geo.fetch([52.530116236589244, 13.426532801586827],
                 [52.50876180448243, 13.359631043007212])
print(data.keys())
# dict_keys(['Adresse', 'Barrierenlinie', 'Bauwerksflaeche', 'Bauwerkslinie', 'Bauwerkspunkt', 'Besondere_Flaeche', 'Besondere_Linie', 'Besonderer_Punkt', 'Gebaeudeflaeche', 'Gebaeudepunkt', 'Gewaesserflaeche', 'Gewaesserlinie', 'Grenze_Linie', 'Historischer_Punkt', 'Siedlungsflaeche', 'Vegetationslinie', 'Verkehrsflaeche', 'Verkehrslinie', 'Verkehrspunkt', 'Hintergrund'])

print(data["Adresse"][0])
# {'geometry': {'type': 'Point', 'coordinates': (13.422642946243286, 52.51500157651358)}, 'properties': {'postleitzahl': '10179', 'ort': 'Berlin', 'ortsteil': 'Mitte', 'strasse': 'Holzmarktstraße', 'hausnummer': '55'}, 'id': 0, 'type': 'Feature'}
```
The data is provided by the [AdV SmartMapping](https://adv-smart.de/index_en.html). The team consists of participants from the German state surveying offices, the Federal Agency for Cartography and Geodesy (BKG), the German Federal Armed Forces (Bundeswehr ZGeoBW) and third parties from research and education.



## Company Data

### Bundesanzeiger
Get financial reports for all german companies that are reporting to Bundesanzeiger.

```python
from deutschland import Bundesanzeiger
ba = Bundesanzeiger()
# search term
data = ba.get_reports("Deutsche Bahn AG")
# returns a dictionary with all reports found as fulltext reports
print(data.keys())
# dict_keys(['Jahresabschluss zum Geschäftsjahr vom 01.01.2020 bis zum 31.12.2020', 'Konzernabschluss zum Geschäftsjahr vom 01.01.2020 bis zum 31.12.2020\nErgänzung der Veröffentlichung vom 04.06.2021',
```
*Big thanks to Nico Duldhardt and Friedrich Schöne, who [supported this implementation with their machine learning model](https://av.tib.eu/media/52366).*

### Handelsregister
Fetch general company information about any company in the Handelsregister.

```python
from deutschland import Handelsregister
hr = Handelsregister()
# search by keywords, see documentation for all available params
hr.search(keywords="Deutsche Bahn Aktiengesellschaft")
print(hr)
```


## Consumer Protection Data

### Lebensmittelwarnung
Get current product warnings provided by the german federal portal lebensmittelwarnung.de.

```python
from deutschland import Lebensmittelwarnung
lw = Lebensmittelwarnung()
# search by content type and region, see documetation for all available params
data = lw.get("lebensmittel", "berlin")
print(data)
# [{'id': 19601, 'guid': 'https://www.lebensmittelwarnung.de/bvl-lmw-de/detail/lebensmittel/19601', 'pubDate': 'Fri, 10 Feb 2017 12:28:45 +0000', 'imgSrc': 'https://www.lebensmittelwarnung.de/bvl-lmw-de/opensaga/attachment/979f8cd3-969e-4a6c-9a8e-4bdd61586cd4/data.jpg', 'title': 'Sidroga Bio Säuglings- und Kindertee', 'manufacturer': 'Lebensmittel', 'warning': 'Pyrrolizidinalkaloide', 'affectedStates': ['Baden-Württemberg', '...']}]
```

## Federal Job Openings

### NRW

#### VERENA
Get open substitute teaching positions in NRW from https://www.schulministerium.nrw.de/BiPo/Verena/angebote
```python
from deutschland import Verena
v = Verena()
data = v.get()
print(data)
# a full example data can be found at deutschland/verena/example.md
# [{ "school_id": "99999", "desc": "Eine Schule\nSchule der Sekundarstufe II\ndes Landkreis Schuling\n9999 Schulingen", "replacement_job_title": "Lehrkraft", "subjects": [ "Fach 1", "Fach 2" ], "comments": "Bemerkung zur Stelle: Testbemerkung", "duration": "01.01.2021 - 01.01.2022", ...} ...]
```

## Autobahn

Get data from the Autobahn.

```python
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
```
For the detailed documentation of this API see [here](https://github.com/bundesAPI/deutschland/blob/main/docs/autobahn/README.md)


## Presseportal

For further information see: https://github.com/tcmetzger/pypresseportal

```python
from deutschland.presseportal import PresseportalApi

presseportal = PresseportalApi("YOUR_KEY_HERE")

stories = presseportal.get_stories()
```

## Auto-Generated API-Clients

### bundesrat
For the detailed documentation of this API see [here](https://github.com/bundesAPI/deutschland/blob/main/docs/bundesrat/README.md)
### bundestag
For the detailed documentation of this API see [here](https://github.com/bundesAPI/deutschland/blob/main/docs/bundestag/README.md)
### destatis
For the detailed documentation of this API see [here](https://github.com/bundesAPI/deutschland/blob/main/docs/destatis/README.md)
### dwd
For the detailed documentation of this API see [here](https://github.com/bundesAPI/deutschland/blob/main/docs/dwd/README.md)
### interpol
For the detailed documentation of this API see [here](https://github.com/bundesAPI/deutschland/blob/main/docs/interpol/README.md)
### jobsuche
For the detailed documentation of this API see [here](https://github.com/bundesAPI/deutschland/blob/main/docs/jobsuche/README.md)
### ladestationen
For the detailed documentation of this API see [here](https://github.com/bundesAPI/deutschland/blob/main/docs/ladestationen/README.md)
### mudab
For the detailed documentation of this API see [here](https://github.com/bundesAPI/deutschland/blob/main/docs/mudab/README.md)
### nina
For the detailed documentation of this API see [here](https://github.com/bundesAPI/deutschland/blob/main/docs/nina/README.md)
### polizei_brandenburg
For the detailed documentation of this API see [here](https://github.com/bundesAPI/deutschland/blob/main/docs/polizei_brandenburg/README.md)
### risikogebiete
For the detailed documentation of this API see [here](https://github.com/bundesAPI/deutschland/blob/main/docs/risikogebiete/README.md)
### smard
For the detailed documentation of this API see [here](https://github.com/bundesAPI/deutschland/blob/main/docs/smard/README.md)
### strahlenschutz
For the detailed documentation of this API see [here](https://github.com/bundesAPI/deutschland/blob/main/docs/strahlenschutz/README.md)
### travelwarning
For the detailed documentation of this API see [here](https://github.com/bundesAPI/deutschland/blob/main/docs/travelwarning/README.md)
### zoll
For the detailed documentation of this API see [here](https://github.com/bundesAPI/deutschland/blob/main/docs/zoll/README.md)
