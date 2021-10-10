# autobahn.DefaultApi

All URIs are relative to *https://verkehr.autobahn.de/o/autobahn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_charging_station**](DefaultApi.md#get_charging_station) | **GET** /details/electric_charging_station/{stationId} | Details zu einer Ladestation
[**get_closure**](DefaultApi.md#get_closure) | **GET** /details/closure/{closureId} | Details zu einer Sperrung
[**get_parking_lorry**](DefaultApi.md#get_parking_lorry) | **GET** /details/parking_lorry/{lorryId} | Details eines Rastplatzes
[**get_roadwork**](DefaultApi.md#get_roadwork) | **GET** /details/roadworks/{roadworkId} | Details einer Baustelle
[**get_warning**](DefaultApi.md#get_warning) | **GET** /details/warning/{warningId} | Details zu einer Verkehrsmeldung
[**get_webcam**](DefaultApi.md#get_webcam) | **GET** /details/webcam/{webcamId} | Details einer Webcam
[**list_autobahnen**](DefaultApi.md#list_autobahnen) | **GET** / | Liste verfügbarer Autobahnen
[**list_charging_stations**](DefaultApi.md#list_charging_stations) | **GET** /{roadId}/services/electric_charging_station | Liste aktueller Ladestationen
[**list_closures**](DefaultApi.md#list_closures) | **GET** /{roadId}/services/closure | Liste aktueller Sperrungen
[**list_parking_lorries**](DefaultApi.md#list_parking_lorries) | **GET** /{roadId}/services/parking_lorry | Liste verfügbarer Rastplätze
[**list_roadworks**](DefaultApi.md#list_roadworks) | **GET** /{roadId}/services/roadworks | Liste aktueller Baustellen
[**list_warnings**](DefaultApi.md#list_warnings) | **GET** /{roadId}/services/warning | Liste aktueller Verkehrsmeldungen
[**list_webcams**](DefaultApi.md#list_webcams) | **GET** /{roadId}/services/webcam | Liste verfügbarer Webcams


# **get_charging_station**
> ElectricChargingStation get_charging_station(station_id)

Details zu einer Ladestation

Gibt Details zu einer konkreten Ladestation zurück.

### Example


```python
import time
from deutschland import autobahn
from deutschland.autobahn.api import default_api
from deutschland.autobahn.model.electric_charging_station import ElectricChargingStation
from pprint import pprint
# Defining the host is optional and defaults to https://verkehr.autobahn.de/o/autobahn
# See configuration.py for a list of all supported configuration parameters.
configuration = autobahn.Configuration(
    host = "https://verkehr.autobahn.de/o/autobahn"
)


# Enter a context with an instance of the API client
with autobahn.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    station_id = "RUxFQ1RSSUNfQ0hBUkdJTkdfU1RBVElPTl9fMTczMzM=" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Details zu einer Ladestation
        api_response = api_instance.get_charging_station(station_id)
        pprint(api_response)
    except autobahn.ApiException as e:
        print("Exception when calling DefaultApi->get_charging_station: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**|  |

### Return type

[**ElectricChargingStation**](ElectricChargingStation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Not found. |  -  |
**400** | Internal server error. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_closure**
> Closure get_closure(closure_id)

Details zu einer Sperrung

Gibt Details zu einer konkreten Sperrung zurück.

### Example


```python
import time
from deutschland import autobahn
from deutschland.autobahn.api import default_api
from deutschland.autobahn.model.closure import Closure
from pprint import pprint
# Defining the host is optional and defaults to https://verkehr.autobahn.de/o/autobahn
# See configuration.py for a list of all supported configuration parameters.
configuration = autobahn.Configuration(
    host = "https://verkehr.autobahn.de/o/autobahn"
)


# Enter a context with an instance of the API client
with autobahn.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    closure_id = "Q0xPU1VSRV9fbWRtLnZpel9fTE1TLU5XL3JfVElDLU5SV0JMSy8zOS9OUldCTEsvMTAgMzUgMjEgRCAwOTI0Mi0wMV9EICBOVyBMTVMtTlcuMA==" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Details zu einer Sperrung
        api_response = api_instance.get_closure(closure_id)
        pprint(api_response)
    except autobahn.ApiException as e:
        print("Exception when calling DefaultApi->get_closure: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **closure_id** | **str**|  |

### Return type

[**Closure**](Closure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Not found. |  -  |
**400** | Internal server error. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parking_lorry**
> ParkingLorry get_parking_lorry(lorry_id)

Details eines Rastplatzes

Gibt Details eines konkreten Rastplatzes zurück.

### Example


```python
import time
from deutschland import autobahn
from deutschland.autobahn.api import default_api
from deutschland.autobahn.model.parking_lorry import ParkingLorry
from pprint import pprint
# Defining the host is optional and defaults to https://verkehr.autobahn.de/o/autobahn
# See configuration.py for a list of all supported configuration parameters.
configuration = autobahn.Configuration(
    host = "https://verkehr.autobahn.de/o/autobahn"
)


# Enter a context with an instance of the API client
with autobahn.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    lorry_id = "UEFSS0lOR19fbWRtLmxvcnJ5LnBhcmtpbmdfX0RFLVNILTAwMTEwOA==" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Details eines Rastplatzes
        api_response = api_instance.get_parking_lorry(lorry_id)
        pprint(api_response)
    except autobahn.ApiException as e:
        print("Exception when calling DefaultApi->get_parking_lorry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lorry_id** | **str**|  |

### Return type

[**ParkingLorry**](ParkingLorry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Not found. |  -  |
**400** | Internal server error. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roadwork**
> Roadwork get_roadwork(roadwork_id)

Details einer Baustelle

Gibt Details zu einer konkreten Baustelle zurück.

### Example


```python
import time
from deutschland import autobahn
from deutschland.autobahn.api import default_api
from deutschland.autobahn.model.roadwork import Roadwork
from pprint import pprint
# Defining the host is optional and defaults to https://verkehr.autobahn.de/o/autobahn
# See configuration.py for a list of all supported configuration parameters.
configuration = autobahn.Configuration(
    host = "https://verkehr.autobahn.de/o/autobahn"
)


# Enter a context with an instance of the API client
with autobahn.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    roadwork_id = "Uk9BRFdPUktTX19tZG0ubndfXzAyLTgwMDAwIEQgNzEgMTkgMDkvS0xCV1JO" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Details einer Baustelle
        api_response = api_instance.get_roadwork(roadwork_id)
        pprint(api_response)
    except autobahn.ApiException as e:
        print("Exception when calling DefaultApi->get_roadwork: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roadwork_id** | **str**|  |

### Return type

[**Roadwork**](Roadwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Not found. |  -  |
**400** | Internal server error. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_warning**
> Warning get_warning(warning_id)

Details zu einer Verkehrsmeldung

Gibt Details zu einer konkreten Verkehrsmeldung zurück.

### Example


```python
import time
from deutschland import autobahn
from deutschland.autobahn.api import default_api
from deutschland.autobahn.model.warning import Warning
from pprint import pprint
# Defining the host is optional and defaults to https://verkehr.autobahn.de/o/autobahn
# See configuration.py for a list of all supported configuration parameters.
configuration = autobahn.Configuration(
    host = "https://verkehr.autobahn.de/o/autobahn"
)


# Enter a context with an instance of the API client
with autobahn.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    warning_id = "V0FSTklOR19fbWRtLnZpel9fTE1TLU5XL3JfTE1TLU5XLzMyNDE3OV9EICBOVyBMTVMtTlcuMA==" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Details zu einer Verkehrsmeldung
        api_response = api_instance.get_warning(warning_id)
        pprint(api_response)
    except autobahn.ApiException as e:
        print("Exception when calling DefaultApi->get_warning: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warning_id** | **str**|  |

### Return type

[**Warning**](Warning.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Not found. |  -  |
**400** | Internal server error. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webcam**
> Webcam get_webcam(webcam_id)

Details einer Webcam

Gibt Details einer konkreten Webcam zurück.

### Example


```python
import time
from deutschland import autobahn
from deutschland.autobahn.api import default_api
from deutschland.autobahn.model.webcam import Webcam
from pprint import pprint
# Defining the host is optional and defaults to https://verkehr.autobahn.de/o/autobahn
# See configuration.py for a list of all supported configuration parameters.
configuration = autobahn.Configuration(
    host = "https://verkehr.autobahn.de/o/autobahn"
)


# Enter a context with an instance of the API client
with autobahn.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    webcam_id = "V0VCQ0FNX19OUldfU2lsYS1TaWduYWxiYXVfMTAxMDgxNDE3MjM4ODYzOTk5MTU=" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Details einer Webcam
        api_response = api_instance.get_webcam(webcam_id)
        pprint(api_response)
    except autobahn.ApiException as e:
        print("Exception when calling DefaultApi->get_webcam: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webcam_id** | **str**|  |

### Return type

[**Webcam**](Webcam.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Not found. |  -  |
**400** | Internal server error. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_autobahnen**
> Roads list_autobahnen()

Liste verfügbarer Autobahnen

Gibt eine Liste der verfügbaren Autobahnen zurück.

### Example


```python
import time
from deutschland import autobahn
from deutschland.autobahn.api import default_api
from deutschland.autobahn.model.roads import Roads
from pprint import pprint
# Defining the host is optional and defaults to https://verkehr.autobahn.de/o/autobahn
# See configuration.py for a list of all supported configuration parameters.
configuration = autobahn.Configuration(
    host = "https://verkehr.autobahn.de/o/autobahn"
)


# Enter a context with an instance of the API client
with autobahn.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liste verfügbarer Autobahnen
        api_response = api_instance.list_autobahnen()
        pprint(api_response)
    except autobahn.ApiException as e:
        print("Exception when calling DefaultApi->list_autobahnen: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Roads**](Roads.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_charging_stations**
> ElectricChargingStations list_charging_stations(road_id)

Liste aktueller Ladestationen

Gibt eine Liste der Ladestationen zu einer Autobahn zurück.

### Example


```python
import time
from deutschland import autobahn
from deutschland.autobahn.api import default_api
from deutschland.autobahn.model.electric_charging_stations import ElectricChargingStations
from deutschland.autobahn.model.road_id import RoadId
from pprint import pprint
# Defining the host is optional and defaults to https://verkehr.autobahn.de/o/autobahn
# See configuration.py for a list of all supported configuration parameters.
configuration = autobahn.Configuration(
    host = "https://verkehr.autobahn.de/o/autobahn"
)


# Enter a context with an instance of the API client
with autobahn.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    road_id = RoadId("A1") # RoadId | 

    # example passing only required values which don't have defaults set
    try:
        # Liste aktueller Ladestationen
        api_response = api_instance.list_charging_stations(road_id)
        pprint(api_response)
    except autobahn.ApiException as e:
        print("Exception when calling DefaultApi->list_charging_stations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **road_id** | **RoadId**|  |

### Return type

[**ElectricChargingStations**](ElectricChargingStations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Not found. |  -  |
**400** | Internal server error. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_closures**
> Closures list_closures(road_id)

Liste aktueller Sperrungen

Gibt eine Liste der Sperrungen zu einer Autobahn zurück.

### Example


```python
import time
from deutschland import autobahn
from deutschland.autobahn.api import default_api
from deutschland.autobahn.model.closures import Closures
from deutschland.autobahn.model.road_id import RoadId
from pprint import pprint
# Defining the host is optional and defaults to https://verkehr.autobahn.de/o/autobahn
# See configuration.py for a list of all supported configuration parameters.
configuration = autobahn.Configuration(
    host = "https://verkehr.autobahn.de/o/autobahn"
)


# Enter a context with an instance of the API client
with autobahn.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    road_id = RoadId("A1") # RoadId | 

    # example passing only required values which don't have defaults set
    try:
        # Liste aktueller Sperrungen
        api_response = api_instance.list_closures(road_id)
        pprint(api_response)
    except autobahn.ApiException as e:
        print("Exception when calling DefaultApi->list_closures: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **road_id** | **RoadId**|  |

### Return type

[**Closures**](Closures.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Not found. |  -  |
**400** | Internal server error. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parking_lorries**
> ParkingLorries list_parking_lorries(road_id)

Liste verfügbarer Rastplätze

Gibt eine Liste der Rastplätze zu einer Autobahn zurück.

### Example


```python
import time
from deutschland import autobahn
from deutschland.autobahn.api import default_api
from deutschland.autobahn.model.parking_lorries import ParkingLorries
from deutschland.autobahn.model.road_id import RoadId
from pprint import pprint
# Defining the host is optional and defaults to https://verkehr.autobahn.de/o/autobahn
# See configuration.py for a list of all supported configuration parameters.
configuration = autobahn.Configuration(
    host = "https://verkehr.autobahn.de/o/autobahn"
)


# Enter a context with an instance of the API client
with autobahn.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    road_id = RoadId("A1") # RoadId | 

    # example passing only required values which don't have defaults set
    try:
        # Liste verfügbarer Rastplätze
        api_response = api_instance.list_parking_lorries(road_id)
        pprint(api_response)
    except autobahn.ApiException as e:
        print("Exception when calling DefaultApi->list_parking_lorries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **road_id** | **RoadId**|  |

### Return type

[**ParkingLorries**](ParkingLorries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Not found. |  -  |
**400** | Internal server error. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roadworks**
> Roadworks list_roadworks(road_id)

Liste aktueller Baustellen

Gibt eine Liste der aktuellen Baustellen zu einer Autobahn zurück.

### Example


```python
import time
from deutschland import autobahn
from deutschland.autobahn.api import default_api
from deutschland.autobahn.model.roadworks import Roadworks
from deutschland.autobahn.model.road_id import RoadId
from pprint import pprint
# Defining the host is optional and defaults to https://verkehr.autobahn.de/o/autobahn
# See configuration.py for a list of all supported configuration parameters.
configuration = autobahn.Configuration(
    host = "https://verkehr.autobahn.de/o/autobahn"
)


# Enter a context with an instance of the API client
with autobahn.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    road_id = RoadId("A1") # RoadId | 

    # example passing only required values which don't have defaults set
    try:
        # Liste aktueller Baustellen
        api_response = api_instance.list_roadworks(road_id)
        pprint(api_response)
    except autobahn.ApiException as e:
        print("Exception when calling DefaultApi->list_roadworks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **road_id** | **RoadId**|  |

### Return type

[**Roadworks**](Roadworks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Not found. |  -  |
**400** | Internal server error. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_warnings**
> Warnings list_warnings(road_id)

Liste aktueller Verkehrsmeldungen

Gibt eine Liste der Verkehrsmeldungen zu einer Autobahn zurück.

### Example


```python
import time
from deutschland import autobahn
from deutschland.autobahn.api import default_api
from deutschland.autobahn.model.warnings import Warnings
from deutschland.autobahn.model.road_id import RoadId
from pprint import pprint
# Defining the host is optional and defaults to https://verkehr.autobahn.de/o/autobahn
# See configuration.py for a list of all supported configuration parameters.
configuration = autobahn.Configuration(
    host = "https://verkehr.autobahn.de/o/autobahn"
)


# Enter a context with an instance of the API client
with autobahn.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    road_id = RoadId("A1") # RoadId | 

    # example passing only required values which don't have defaults set
    try:
        # Liste aktueller Verkehrsmeldungen
        api_response = api_instance.list_warnings(road_id)
        pprint(api_response)
    except autobahn.ApiException as e:
        print("Exception when calling DefaultApi->list_warnings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **road_id** | **RoadId**|  |

### Return type

[**Warnings**](Warnings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Not found. |  -  |
**400** | Internal server error. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webcams**
> Webcams list_webcams(road_id)

Liste verfügbarer Webcams

Gibt eine Liste der Webcams zu einer Autobahn zurück.

### Example


```python
import time
from deutschland import autobahn
from deutschland.autobahn.api import default_api
from deutschland.autobahn.model.webcams import Webcams
from deutschland.autobahn.model.road_id import RoadId
from pprint import pprint
# Defining the host is optional and defaults to https://verkehr.autobahn.de/o/autobahn
# See configuration.py for a list of all supported configuration parameters.
configuration = autobahn.Configuration(
    host = "https://verkehr.autobahn.de/o/autobahn"
)


# Enter a context with an instance of the API client
with autobahn.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    road_id = RoadId("A1") # RoadId | 

    # example passing only required values which don't have defaults set
    try:
        # Liste verfügbarer Webcams
        api_response = api_instance.list_webcams(road_id)
        pprint(api_response)
    except autobahn.ApiException as e:
        print("Exception when calling DefaultApi->list_webcams: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **road_id** | **RoadId**|  |

### Return type

[**Webcams**](Webcams.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Not found. |  -  |
**400** | Internal server error. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

