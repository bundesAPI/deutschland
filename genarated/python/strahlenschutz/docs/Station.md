# Station

Spezifikation einer Messstation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ort** | **str** | Ortsname | [optional] 
**kid** | **float** | Messnetzknoten-ID der Station (1 &#x3D; Freiburg, 2 &#x3D; Berlin, 3 &#x3D; München, 4 &#x3D; Bonn, 5 &#x3D; Salzgitter, 6 &#x3D; Rendsburg) | [optional] 
**imis** | **str** | IMIS-ID | [optional] 
**status** | **float** | Zustand der Station (0 &#x3D; defekt, 1 &#x3D; in Betrieb, 128 &#x3D; Testbetrieb, 2048 &#x3D; Wartung) | [optional] 
**hoehe** | **float** | Höhe der Station über NN | [optional] 
**lon** | **float** | Längengrad | [optional] 
**mw** | **float** | Aktueller Messwert in µSv/h | [optional] 
**lat** | **float** | Breitengrad | [optional] 
**plz** | **str** | PLZ | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


