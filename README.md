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
data = geo.fetch([52.50876180448243, 13.359631043007212], 
                 [52.530116236589244, 13.426532801586827])
print(data.keys())
# dict_keys(['Adresse', 'Barrierenlinie', 'Bauwerksflaeche', 'Bauwerkslinie', 'Bauwerkspunkt', 'Besondere_Flaeche', 'Besondere_Linie', 'Besonderer_Punkt', 'Gebaeudeflaeche', 'Gebaeudepunkt', 'Gewaesserflaeche', 'Gewaesserlinie', 'Grenze_Linie', 'Historischer_Punkt', 'Siedlungsflaeche', 'Vegetationslinie', 'Verkehrsflaeche', 'Verkehrslinie', 'Verkehrspunkt', 'Hintergrund'])

print(data["Adresse"][0])
# {'geometry': {'type': 'Point', 'coordinates': (13.422642946243286, 52.51500157651358)}, 'properties': {'postleitzahl': '10179', 'ort': 'Berlin', 'ortsteil': 'Mitte', 'strasse': 'Holzmarktstraße', 'hausnummer': '55'}, 'id': 0, 'type': 'Feature'}
```




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