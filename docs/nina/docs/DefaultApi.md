# nina.DefaultApi

All URIs are relative to *https://warnung.bund.de/api31*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appdata_covid_covidrules_deags_json_get**](DefaultApi.md#appdata_covid_covidrules_deags_json_get) | **GET** /appdata/covid/covidrules/DE/{AGS}.json | Corona Regelungen nach AGS
[**biwapp_map_data_json_get**](DefaultApi.md#biwapp_map_data_json_get) | **GET** /biwapp/mapData.json | Biwapp Meldungen
[**dashboard_ags_json_get**](DefaultApi.md#dashboard_ags_json_get) | **GET** /dashboard/{AGS}.json | Meldungsübersicht nach AGS
[**katwarn_map_data_json_get**](DefaultApi.md#katwarn_map_data_json_get) | **GET** /katwarn/mapData.json | Katwarn Meldungen
[**mowas_map_data_json_get**](DefaultApi.md#mowas_map_data_json_get) | **GET** /mowas/mapData.json | Mowas Meldungen


# **appdata_covid_covidrules_deags_json_get**
> AGSCovidRules appdata_covid_covidrules_deags_json_get(ags)

Corona Regelungen nach AGS

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import default_api
from deutschland.nina.model.ags_covid_rules import AGSCovidRules
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    ags = "091620000000" # str | Amtlicher Gebietsschlüssel - kann z.B. von [hier](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) bezogen werden.

    # example passing only required values which don't have defaults set
    try:
        # Corona Regelungen nach AGS
        api_response = api_instance.appdata_covid_covidrules_deags_json_get(ags)
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling DefaultApi->appdata_covid_covidrules_deags_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ags** | **str**| Amtlicher Gebietsschlüssel - kann z.B. von [hier](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) bezogen werden. |

### Return type

[**AGSCovidRules**](AGSCovidRules.md)

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

# **biwapp_map_data_json_get**
> MapWarnings biwapp_map_data_json_get()

Biwapp Meldungen

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import default_api
from deutschland.nina.model.map_warnings import MapWarnings
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Biwapp Meldungen
        api_response = api_instance.biwapp_map_data_json_get()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling DefaultApi->biwapp_map_data_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MapWarnings**](MapWarnings.md)

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

# **dashboard_ags_json_get**
> AGSOverviewResult dashboard_ags_json_get(ags)

Meldungsübersicht nach AGS

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import default_api
from deutschland.nina.model.ags_overview_result import AGSOverviewResult
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    ags = "091620000000" # str | Amtlicher Gebietsschlüssel - kann z.B. von [hier](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) bezogen werden. Die Letzten 7 Stellen müssen dabei mit \"0000000\" ersetzt werden, weil die Daten nur auf [Kreisebene](https://de.wikipedia.org/wiki/Amtlicher_Gemeindeschl%C3%BCssel) bereitgestellt werden.

    # example passing only required values which don't have defaults set
    try:
        # Meldungsübersicht nach AGS
        api_response = api_instance.dashboard_ags_json_get(ags)
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling DefaultApi->dashboard_ags_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ags** | **str**| Amtlicher Gebietsschlüssel - kann z.B. von [hier](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) bezogen werden. Die Letzten 7 Stellen müssen dabei mit \&quot;0000000\&quot; ersetzt werden, weil die Daten nur auf [Kreisebene](https://de.wikipedia.org/wiki/Amtlicher_Gemeindeschl%C3%BCssel) bereitgestellt werden. |

### Return type

[**AGSOverviewResult**](AGSOverviewResult.md)

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

# **katwarn_map_data_json_get**
> MapWarnings katwarn_map_data_json_get()

Katwarn Meldungen

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import default_api
from deutschland.nina.model.map_warnings import MapWarnings
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Katwarn Meldungen
        api_response = api_instance.katwarn_map_data_json_get()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling DefaultApi->katwarn_map_data_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MapWarnings**](MapWarnings.md)

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

# **mowas_map_data_json_get**
> MapWarnings mowas_map_data_json_get()

Mowas Meldungen

### Example


```python
import time
from deutschland import nina
from deutschland.nina.api import default_api
from deutschland.nina.model.map_warnings import MapWarnings
from pprint import pprint
# Defining the host is optional and defaults to https://warnung.bund.de/api31
# See configuration.py for a list of all supported configuration parameters.
configuration = nina.Configuration(
    host = "https://warnung.bund.de/api31"
)


# Enter a context with an instance of the API client
with nina.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Mowas Meldungen
        api_response = api_instance.mowas_map_data_json_get()
        pprint(api_response)
    except nina.ApiException as e:
        print("Exception when calling DefaultApi->mowas_map_data_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MapWarnings**](MapWarnings.md)

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

