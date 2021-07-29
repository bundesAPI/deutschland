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

### Handelsregister
Get financial reports for all german companies that are reporting to Handelsregister.

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

