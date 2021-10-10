# travelwarning.DefaultApi

All URIs are relative to *https://www.auswaertiges-amt.de/opendata*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_healthcare**](DefaultApi.md#get_healthcare) | **GET** /healthcare | Gibt die Merkblätter des Gesundheitsdienstes zurück
[**get_representatives_country**](DefaultApi.md#get_representatives_country) | **GET** /representativesInCountry | Gibt eine Liste der deutschen Vertretungen im Ausland zurück
[**get_representatives_germany**](DefaultApi.md#get_representatives_germany) | **GET** /representativesInGermany | Gibt eine Liste der ausländischen Vertretungen in Deutschland zurück
[**get_single_travelwarning**](DefaultApi.md#get_single_travelwarning) | **GET** /travelwarning/{contentId} | Gibt einen Reise- und Sicherheitshinweis zurück
[**get_state_names**](DefaultApi.md#get_state_names) | **GET** /stateNames | Gibt das Verzeichnis der Staatennamen zurück
[**get_travelwarning**](DefaultApi.md#get_travelwarning) | **GET** /travelwarning | Gibt alle Reise- und Sicherheitshinweise zurück


# **get_healthcare**
> ResponseDownload get_healthcare()

Gibt die Merkblätter des Gesundheitsdienstes zurück

Merkblätter des Gesundheitsdienstes als Link auf ein PDF

### Example


```python
import time
from deutschland import travelwarning
from deutschland.travelwarning.api import default_api
from deutschland.travelwarning.model.response_download import ResponseDownload
from pprint import pprint
# Defining the host is optional and defaults to https://www.auswaertiges-amt.de/opendata
# See configuration.py for a list of all supported configuration parameters.
configuration = travelwarning.Configuration(
    host = "https://www.auswaertiges-amt.de/opendata"
)


# Enter a context with an instance of the API client
with travelwarning.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Gibt die Merkblätter des Gesundheitsdienstes zurück
        api_response = api_instance.get_healthcare()
        pprint(api_response)
    except travelwarning.ApiException as e:
        print("Exception when calling DefaultApi->get_healthcare: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseDownload**](ResponseDownload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreich |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_representatives_country**
> ResponseAddress get_representatives_country()

Gibt eine Liste der deutschen Vertretungen im Ausland zurück

### Example


```python
import time
from deutschland import travelwarning
from deutschland.travelwarning.api import default_api
from deutschland.travelwarning.model.response_address import ResponseAddress
from pprint import pprint
# Defining the host is optional and defaults to https://www.auswaertiges-amt.de/opendata
# See configuration.py for a list of all supported configuration parameters.
configuration = travelwarning.Configuration(
    host = "https://www.auswaertiges-amt.de/opendata"
)


# Enter a context with an instance of the API client
with travelwarning.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Gibt eine Liste der deutschen Vertretungen im Ausland zurück
        api_response = api_instance.get_representatives_country()
        pprint(api_response)
    except travelwarning.ApiException as e:
        print("Exception when calling DefaultApi->get_representatives_country: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseAddress**](ResponseAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreich |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_representatives_germany**
> ResponseAddress get_representatives_germany()

Gibt eine Liste der ausländischen Vertretungen in Deutschland zurück

### Example


```python
import time
from deutschland import travelwarning
from deutschland.travelwarning.api import default_api
from deutschland.travelwarning.model.response_address import ResponseAddress
from pprint import pprint
# Defining the host is optional and defaults to https://www.auswaertiges-amt.de/opendata
# See configuration.py for a list of all supported configuration parameters.
configuration = travelwarning.Configuration(
    host = "https://www.auswaertiges-amt.de/opendata"
)


# Enter a context with an instance of the API client
with travelwarning.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Gibt eine Liste der ausländischen Vertretungen in Deutschland zurück
        api_response = api_instance.get_representatives_germany()
        pprint(api_response)
    except travelwarning.ApiException as e:
        print("Exception when calling DefaultApi->get_representatives_germany: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseAddress**](ResponseAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreich |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_travelwarning**
> ResponseWarning get_single_travelwarning(content_id)

Gibt einen Reise- und Sicherheitshinweis zurück

Gibt den vollständigen Datensatz eines Reise- und Sicherheitshinweises zurück. Benötigt die jeweilige ID siehe /travelwarning

### Example


```python
import time
from deutschland import travelwarning
from deutschland.travelwarning.api import default_api
from deutschland.travelwarning.model.response_warning import ResponseWarning
from pprint import pprint
# Defining the host is optional and defaults to https://www.auswaertiges-amt.de/opendata
# See configuration.py for a list of all supported configuration parameters.
configuration = travelwarning.Configuration(
    host = "https://www.auswaertiges-amt.de/opendata"
)


# Enter a context with an instance of the API client
with travelwarning.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    content_id = 1 # int | Die ID des Reise- und Sicherheitshinweises, IDs siehe /travelwarning

    # example passing only required values which don't have defaults set
    try:
        # Gibt einen Reise- und Sicherheitshinweis zurück
        api_response = api_instance.get_single_travelwarning(content_id)
        pprint(api_response)
    except travelwarning.ApiException as e:
        print("Exception when calling DefaultApi->get_single_travelwarning: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | **int**| Die ID des Reise- und Sicherheitshinweises, IDs siehe /travelwarning |

### Return type

[**ResponseWarning**](ResponseWarning.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreich |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_names**
> ResponseDownload get_state_names()

Gibt das Verzeichnis der Staatennamen zurück

Verzeichnis der Staatennamen als Link auf eine XML- oder CSV-Datei. Eine PDF-Datei mit Nutzungshinweisen wird ebenfalls zurückgegeben.

### Example


```python
import time
from deutschland import travelwarning
from deutschland.travelwarning.api import default_api
from deutschland.travelwarning.model.response_download import ResponseDownload
from pprint import pprint
# Defining the host is optional and defaults to https://www.auswaertiges-amt.de/opendata
# See configuration.py for a list of all supported configuration parameters.
configuration = travelwarning.Configuration(
    host = "https://www.auswaertiges-amt.de/opendata"
)


# Enter a context with an instance of the API client
with travelwarning.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Gibt das Verzeichnis der Staatennamen zurück
        api_response = api_instance.get_state_names()
        pprint(api_response)
    except travelwarning.ApiException as e:
        print("Exception when calling DefaultApi->get_state_names: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseDownload**](ResponseDownload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreich |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_travelwarning**
> ResponseWarnings get_travelwarning()

Gibt alle Reise- und Sicherheitshinweise zurück

### Example


```python
import time
from deutschland import travelwarning
from deutschland.travelwarning.api import default_api
from deutschland.travelwarning.model.response_warnings import ResponseWarnings
from pprint import pprint
# Defining the host is optional and defaults to https://www.auswaertiges-amt.de/opendata
# See configuration.py for a list of all supported configuration parameters.
configuration = travelwarning.Configuration(
    host = "https://www.auswaertiges-amt.de/opendata"
)


# Enter a context with an instance of the API client
with travelwarning.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Gibt alle Reise- und Sicherheitshinweise zurück
        api_response = api_instance.get_travelwarning()
        pprint(api_response)
    except travelwarning.ApiException as e:
        print("Exception when calling DefaultApi->get_travelwarning: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseWarnings**](ResponseWarnings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreich |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

