# smard.DefaultApi

All URIs are relative to *https://www.smard.de/app/chart_data*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_region_filter_copy_region_copy_resolution_timestamp_json_get**](DefaultApi.md#filter_region_filter_copy_region_copy_resolution_timestamp_json_get) | **GET** /{filter}/{region}/{filterCopy}_{regionCopy}_{resolution}_{timestamp}.json | Zeitreihendaten
[**filter_region_index_resolution_json_get**](DefaultApi.md#filter_region_index_resolution_json_get) | **GET** /{filter}/{region}/index_{resolution}.json | Indizes


# **filter_region_filter_copy_region_copy_resolution_timestamp_json_get**
> TimeSeries filter_region_filter_copy_region_copy_resolution_timestamp_json_get(filter, filter_copy, region_copy, timestamp)

Zeitreihendaten

Zeitreihendaten nach Filter, Region und Auflösung ab Timestamp

### Example


```python
import time
import smard
from smard.api import default_api
from smard.model.time_series import TimeSeries
from pprint import pprint
# Defining the host is optional and defaults to https://www.smard.de/app/chart_data
# See configuration.py for a list of all supported configuration parameters.
configuration = smard.Configuration(
    host = "https://www.smard.de/app/chart_data"
)


# Enter a context with an instance of the API client
with smard.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter = 1223 # int | Mögliche Filter:   * `1223` - Stromerzeugung: Braunkohle   * `1224` - Stromerzeugung: Kernenergie   * `1225` - Stromerzeugung: Wind Offshore   * `1226` - Stromerzeugung: Wasserkraft   * `1227` - Stromerzeugung: Sonstige Konventionelle   * `1228` - Stromerzeugung: Sonstige Erneuerbare   * `4066` - Stromerzeugung: Biomasse   * `4067` - Stromerzeugung: Wind Onshore   * `4068` - Stromerzeugung: Photovoltaik   * `4069` - Stromerzeugung: Steinkohle   * `4070` - Stromerzeugung: Pumpspeicher   * `4071` - Stromerzeugung: Erdgas   * `410` - Stromverbrauch: Gesamt (Netzlast)   * `4359` - Stromverbrauch: Residuallast   * `4387` - Stromverbrauch: Pumpspeicher 
    filter_copy = 1223 # int | Muss dem Wert von \"filter\" entsprechen. (Kaputtes API-Design) 
    region_copy = "DE" # str | Muss dem Wert von \"region\" entsprechen. (Kaputtes API-Design) 
    timestamp = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Zeitreihendaten
        api_response = api_instance.filter_region_filter_copy_region_copy_resolution_timestamp_json_get(filter, filter_copy, region_copy, timestamp)
        pprint(api_response)
    except smard.ApiException as e:
        print("Exception when calling DefaultApi->filter_region_filter_copy_region_copy_resolution_timestamp_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **int**| Mögliche Filter:   * &#x60;1223&#x60; - Stromerzeugung: Braunkohle   * &#x60;1224&#x60; - Stromerzeugung: Kernenergie   * &#x60;1225&#x60; - Stromerzeugung: Wind Offshore   * &#x60;1226&#x60; - Stromerzeugung: Wasserkraft   * &#x60;1227&#x60; - Stromerzeugung: Sonstige Konventionelle   * &#x60;1228&#x60; - Stromerzeugung: Sonstige Erneuerbare   * &#x60;4066&#x60; - Stromerzeugung: Biomasse   * &#x60;4067&#x60; - Stromerzeugung: Wind Onshore   * &#x60;4068&#x60; - Stromerzeugung: Photovoltaik   * &#x60;4069&#x60; - Stromerzeugung: Steinkohle   * &#x60;4070&#x60; - Stromerzeugung: Pumpspeicher   * &#x60;4071&#x60; - Stromerzeugung: Erdgas   * &#x60;410&#x60; - Stromverbrauch: Gesamt (Netzlast)   * &#x60;4359&#x60; - Stromverbrauch: Residuallast   * &#x60;4387&#x60; - Stromverbrauch: Pumpspeicher  |
 **filter_copy** | **int**| Muss dem Wert von \&quot;filter\&quot; entsprechen. (Kaputtes API-Design)  |
 **region_copy** | **str**| Muss dem Wert von \&quot;region\&quot; entsprechen. (Kaputtes API-Design)  |
 **timestamp** | **int**|  |
 **region** | **str**| Land / Regelzone / Marktgebiet:   * &#x60;DE&#x60; - Land: Deutschland   * &#x60;AT&#x60; - Land: Österreich   * &#x60;LU&#x60; - Land: Luxemburg   * &#x60;DE-LU&#x60; - Marktgebiet: DE/LU (ab 01.10.2018)   * &#x60;DE-AT-LU&#x60; - Marktgebiet: DE/AT/LU (bis 30.09.2018)   * &#x60;50Hertz&#x60; - Regelzone (DE): 50Hertz   * &#x60;Amprion&#x60;- Regelzone (DE): Amprion   * &#x60;TenneT&#x60; - Regelzone (DE): TenneT   * &#x60;TransnetBW&#x60; - Regelzone (DE): TransnetBW   * &#x60;APG&#x60; - Regelzone (AT): APG   * &#x60;Creos&#x60; - Regelzone (LU): Creos  | defaults to "DE"
 **resolution** | **str**| Auflösung der Daten:   * &#x60;hour&#x60; - Stündlich   * &#x60;quater_hour&#x60; - Viertelstündlich   * &#x60;day&#x60; - Täglich   * &#x60;week&#x60; - Wöchentlich   * &#x60;month&#x60; - Monatlich   * &#x60;year&#x60; - Jährlich  | defaults to "hour"

### Return type

[**TimeSeries**](TimeSeries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_region_index_resolution_json_get**
> Indices filter_region_index_resolution_json_get(filter, )

Indizes

Verfügbare Timestamps für Filter, Region und Auflösung

### Example


```python
import time
import smard
from smard.api import default_api
from smard.model.indices import Indices
from pprint import pprint
# Defining the host is optional and defaults to https://www.smard.de/app/chart_data
# See configuration.py for a list of all supported configuration parameters.
configuration = smard.Configuration(
    host = "https://www.smard.de/app/chart_data"
)


# Enter a context with an instance of the API client
with smard.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter = 1223 # int | Mögliche Filter:   * `1223` - Stromerzeugung: Braunkohle   * `1224` - Stromerzeugung: Kernenergie   * `1225` - Stromerzeugung: Wind Offshore   * `1226` - Stromerzeugung: Wasserkraft   * `1227` - Stromerzeugung: Sonstige Konventionelle   * `1228` - Stromerzeugung: Sonstige Erneuerbare   * `4066` - Stromerzeugung: Biomasse   * `4067` - Stromerzeugung: Wind Onshore   * `4068` - Stromerzeugung: Photovoltaik   * `4069` - Stromerzeugung: Steinkohle   * `4070` - Stromerzeugung: Pumpspeicher   * `4071` - Stromerzeugung: Erdgas   * `410` - Stromverbrauch: Gesamt (Netzlast)   * `4359` - Stromverbrauch: Residuallast   * `4387` - Stromverbrauch: Pumpspeicher 

    # example passing only required values which don't have defaults set
    try:
        # Indizes
        api_response = api_instance.filter_region_index_resolution_json_get(filter, )
        pprint(api_response)
    except smard.ApiException as e:
        print("Exception when calling DefaultApi->filter_region_index_resolution_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **int**| Mögliche Filter:   * &#x60;1223&#x60; - Stromerzeugung: Braunkohle   * &#x60;1224&#x60; - Stromerzeugung: Kernenergie   * &#x60;1225&#x60; - Stromerzeugung: Wind Offshore   * &#x60;1226&#x60; - Stromerzeugung: Wasserkraft   * &#x60;1227&#x60; - Stromerzeugung: Sonstige Konventionelle   * &#x60;1228&#x60; - Stromerzeugung: Sonstige Erneuerbare   * &#x60;4066&#x60; - Stromerzeugung: Biomasse   * &#x60;4067&#x60; - Stromerzeugung: Wind Onshore   * &#x60;4068&#x60; - Stromerzeugung: Photovoltaik   * &#x60;4069&#x60; - Stromerzeugung: Steinkohle   * &#x60;4070&#x60; - Stromerzeugung: Pumpspeicher   * &#x60;4071&#x60; - Stromerzeugung: Erdgas   * &#x60;410&#x60; - Stromverbrauch: Gesamt (Netzlast)   * &#x60;4359&#x60; - Stromverbrauch: Residuallast   * &#x60;4387&#x60; - Stromverbrauch: Pumpspeicher  |
 **region** | **str**| Land / Regelzone / Marktgebiet:   * &#x60;DE&#x60; - Land: Deutschland   * &#x60;AT&#x60; - Land: Österreich   * &#x60;LU&#x60; - Land: Luxemburg   * &#x60;DE-LU&#x60; - Marktgebiet: DE/LU (ab 01.10.2018)   * &#x60;DE-AT-LU&#x60; - Marktgebiet: DE/AT/LU (bis 30.09.2018)   * &#x60;50Hertz&#x60; - Regelzone (DE): 50Hertz   * &#x60;Amprion&#x60;- Regelzone (DE): Amprion   * &#x60;TenneT&#x60; - Regelzone (DE): TenneT   * &#x60;TransnetBW&#x60; - Regelzone (DE): TransnetBW   * &#x60;APG&#x60; - Regelzone (AT): APG   * &#x60;Creos&#x60; - Regelzone (LU): Creos  | defaults to "DE"
 **resolution** | **str**| Auflösung der Daten:   * &#x60;hour&#x60; - Stündlich   * &#x60;quater_hour&#x60; - Viertelstündlich   * &#x60;day&#x60; - Täglich   * &#x60;week&#x60; - Wöchentlich   * &#x60;month&#x60; - Monatlich   * &#x60;year&#x60; - Jährlich  | defaults to "hour"

### Return type

[**Indices**](Indices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

