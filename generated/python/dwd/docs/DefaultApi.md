# dwd.DefaultApi

All URIs are relative to *https://app-prod-ws.warnwetter.de/v30*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alpen_forecast_text_dwms_json_get**](DefaultApi.md#alpen_forecast_text_dwms_json_get) | **GET** /alpen_forecast_text_dwms.json | Alpen Wettervorhersage als Text
[**crowd_meldungen_overview_v2_json_get**](DefaultApi.md#crowd_meldungen_overview_v2_json_get) | **GET** /crowd_meldungen_overview_v2.json | DWD Crowdwettermeldungen
[**gemeinde_warnings_v2_en_json_get**](DefaultApi.md#gemeinde_warnings_v2_en_json_get) | **GET** /gemeinde_warnings_v2_en.json | Gemeinde Unwetterwarnungen
[**sea_warning_text_json_get**](DefaultApi.md#sea_warning_text_json_get) | **GET** /sea_warning_text.json | Hochsee Unwetterwarnungen als Text
[**station_overview_extended_get**](DefaultApi.md#station_overview_extended_get) | **GET** /stationOverviewExtended | Wetterstation Daten
[**warnings_coast_en_json_get**](DefaultApi.md#warnings_coast_en_json_get) | **GET** /warnings_coast_en.json | Küsten Unwetterwarnungen (englisch)
[**warnings_coast_json_get**](DefaultApi.md#warnings_coast_json_get) | **GET** /warnings_coast.json | Küsten Unwetterwarnungen (deutsch)
[**warnings_lawine_json_get**](DefaultApi.md#warnings_lawine_json_get) | **GET** /warnings_lawine.json | Alpen Wettervorhersage als Text
[**warnings_nowcast_en_json_get**](DefaultApi.md#warnings_nowcast_en_json_get) | **GET** /warnings_nowcast_en.json | Nowcast Warnungen (englisch)
[**warnings_nowcast_json_get**](DefaultApi.md#warnings_nowcast_json_get) | **GET** /warnings_nowcast.json | Nowcast Warnungen (deutsch)


# **alpen_forecast_text_dwms_json_get**
> str alpen_forecast_text_dwms_json_get()

Alpen Wettervorhersage als Text

### Example


```python
import time
import dwd
from dwd.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://app-prod-ws.warnwetter.de/v30
# See configuration.py for a list of all supported configuration parameters.
configuration = dwd.Configuration(
    host = "https://app-prod-ws.warnwetter.de/v30"
)


# Enter a context with an instance of the API client
with dwd.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Alpen Wettervorhersage als Text
        api_response = api_instance.alpen_forecast_text_dwms_json_get()
        pprint(api_response)
    except dwd.ApiException as e:
        print("Exception when calling DefaultApi->alpen_forecast_text_dwms_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/text


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crowd_meldungen_overview_v2_json_get**
> CROWDMeldung crowd_meldungen_overview_v2_json_get()

DWD Crowdwettermeldungen

Der DWD erlaubt Usern das aktuelle Wetter zu melden. In der Response befinden sich alle aktuellen Meldungen

### Example


```python
import time
import dwd
from dwd.api import default_api
from dwd.model.crowd_meldung import CROWDMeldung
from pprint import pprint
# Defining the host is optional and defaults to https://app-prod-ws.warnwetter.de/v30
# See configuration.py for a list of all supported configuration parameters.
configuration = dwd.Configuration(
    host = "https://app-prod-ws.warnwetter.de/v30"
)


# Enter a context with an instance of the API client
with dwd.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # DWD Crowdwettermeldungen
        api_response = api_instance.crowd_meldungen_overview_v2_json_get()
        pprint(api_response)
    except dwd.ApiException as e:
        print("Exception when calling DefaultApi->crowd_meldungen_overview_v2_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CROWDMeldung**](CROWDMeldung.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gemeinde_warnings_v2_en_json_get**
> GemeindeWarnings gemeinde_warnings_v2_en_json_get()

Gemeinde Unwetterwarnungen

### Example


```python
import time
import dwd
from dwd.api import default_api
from dwd.model.gemeinde_warnings import GemeindeWarnings
from pprint import pprint
# Defining the host is optional and defaults to https://app-prod-ws.warnwetter.de/v30
# See configuration.py for a list of all supported configuration parameters.
configuration = dwd.Configuration(
    host = "https://app-prod-ws.warnwetter.de/v30"
)


# Enter a context with an instance of the API client
with dwd.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Gemeinde Unwetterwarnungen
        api_response = api_instance.gemeinde_warnings_v2_en_json_get()
        pprint(api_response)
    except dwd.ApiException as e:
        print("Exception when calling DefaultApi->gemeinde_warnings_v2_en_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GemeindeWarnings**](GemeindeWarnings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sea_warning_text_json_get**
> str sea_warning_text_json_get()

Hochsee Unwetterwarnungen als Text

### Example


```python
import time
import dwd
from dwd.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://app-prod-ws.warnwetter.de/v30
# See configuration.py for a list of all supported configuration parameters.
configuration = dwd.Configuration(
    host = "https://app-prod-ws.warnwetter.de/v30"
)


# Enter a context with an instance of the API client
with dwd.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Hochsee Unwetterwarnungen als Text
        api_response = api_instance.sea_warning_text_json_get()
        pprint(api_response)
    except dwd.ApiException as e:
        print("Exception when calling DefaultApi->sea_warning_text_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/text


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **station_overview_extended_get**
> StationOverview station_overview_extended_get()

Wetterstation Daten

Query für eine oder mehrere Wetterstationen

### Example


```python
import time
import dwd
from dwd.api import default_api
from dwd.model.station_overview import StationOverview
from dwd.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://app-prod-ws.warnwetter.de/v30
# See configuration.py for a list of all supported configuration parameters.
configuration = dwd.Configuration(
    host = "https://app-prod-ws.warnwetter.de/v30"
)


# Enter a context with an instance of the API client
with dwd.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    station_ids = [10865,"G005"] # [dict] | StationsIDs könen z.B. [hier](https://www.dwd.de/DE/leistungen/klimadatendeutschland/stationsliste.html) eingesehen werden (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Wetterstation Daten
        api_response = api_instance.station_overview_extended_get(station_ids=station_ids)
        pprint(api_response)
    except dwd.ApiException as e:
        print("Exception when calling DefaultApi->station_overview_extended_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_ids** | **[dict]**| StationsIDs könen z.B. [hier](https://www.dwd.de/DE/leistungen/klimadatendeutschland/stationsliste.html) eingesehen werden | [optional]

### Return type

[**StationOverview**](StationOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**400** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warnings_coast_en_json_get**
> WarningCoast warnings_coast_en_json_get()

Küsten Unwetterwarnungen (englisch)

### Example


```python
import time
import dwd
from dwd.api import default_api
from dwd.model.warning_coast import WarningCoast
from pprint import pprint
# Defining the host is optional and defaults to https://app-prod-ws.warnwetter.de/v30
# See configuration.py for a list of all supported configuration parameters.
configuration = dwd.Configuration(
    host = "https://app-prod-ws.warnwetter.de/v30"
)


# Enter a context with an instance of the API client
with dwd.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Küsten Unwetterwarnungen (englisch)
        api_response = api_instance.warnings_coast_en_json_get()
        pprint(api_response)
    except dwd.ApiException as e:
        print("Exception when calling DefaultApi->warnings_coast_en_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**WarningCoast**](WarningCoast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warnings_coast_json_get**
> WarningCoast warnings_coast_json_get()

Küsten Unwetterwarnungen (deutsch)

### Example


```python
import time
import dwd
from dwd.api import default_api
from dwd.model.warning_coast import WarningCoast
from pprint import pprint
# Defining the host is optional and defaults to https://app-prod-ws.warnwetter.de/v30
# See configuration.py for a list of all supported configuration parameters.
configuration = dwd.Configuration(
    host = "https://app-prod-ws.warnwetter.de/v30"
)


# Enter a context with an instance of the API client
with dwd.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Küsten Unwetterwarnungen (deutsch)
        api_response = api_instance.warnings_coast_json_get()
        pprint(api_response)
    except dwd.ApiException as e:
        print("Exception when calling DefaultApi->warnings_coast_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**WarningCoast**](WarningCoast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warnings_lawine_json_get**
> str warnings_lawine_json_get()

Alpen Wettervorhersage als Text

### Example


```python
import time
import dwd
from dwd.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://app-prod-ws.warnwetter.de/v30
# See configuration.py for a list of all supported configuration parameters.
configuration = dwd.Configuration(
    host = "https://app-prod-ws.warnwetter.de/v30"
)


# Enter a context with an instance of the API client
with dwd.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Alpen Wettervorhersage als Text
        api_response = api_instance.warnings_lawine_json_get()
        pprint(api_response)
    except dwd.ApiException as e:
        print("Exception when calling DefaultApi->warnings_lawine_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warnings_nowcast_en_json_get**
> WarningNowcast warnings_nowcast_en_json_get()

Nowcast Warnungen (englisch)

### Example


```python
import time
import dwd
from dwd.api import default_api
from dwd.model.warning_nowcast import WarningNowcast
from pprint import pprint
# Defining the host is optional and defaults to https://app-prod-ws.warnwetter.de/v30
# See configuration.py for a list of all supported configuration parameters.
configuration = dwd.Configuration(
    host = "https://app-prod-ws.warnwetter.de/v30"
)


# Enter a context with an instance of the API client
with dwd.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Nowcast Warnungen (englisch)
        api_response = api_instance.warnings_nowcast_en_json_get()
        pprint(api_response)
    except dwd.ApiException as e:
        print("Exception when calling DefaultApi->warnings_nowcast_en_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**WarningNowcast**](WarningNowcast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warnings_nowcast_json_get**
> WarningNowcast warnings_nowcast_json_get()

Nowcast Warnungen (deutsch)

### Example


```python
import time
import dwd
from dwd.api import default_api
from dwd.model.warning_nowcast import WarningNowcast
from pprint import pprint
# Defining the host is optional and defaults to https://app-prod-ws.warnwetter.de/v30
# See configuration.py for a list of all supported configuration parameters.
configuration = dwd.Configuration(
    host = "https://app-prod-ws.warnwetter.de/v30"
)


# Enter a context with an instance of the API client
with dwd.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Nowcast Warnungen (deutsch)
        api_response = api_instance.warnings_nowcast_json_get()
        pprint(api_response)
    except dwd.ApiException as e:
        print("Exception when calling DefaultApi->warnings_nowcast_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**WarningNowcast**](WarningNowcast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

