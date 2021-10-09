# strahlenschutz.DefaultApi

All URIs are relative to *https://odlinfo.bfs.de/json*

Method | HTTP request | Description
------------- | ------------- | -------------
[**id_json_get**](DefaultApi.md#id_json_get) | **GET** /{id}.json | Stammdaten und Zeitreihen zu einer bestimmten Messstation.
[**idct_json_get**](DefaultApi.md#idct_json_get) | **GET** /{id}ct.json | Stammdaten und Zeitreihen zu einer bestimmten Messstation inklusive kosmisch-terrestrischer Daten.
[**stamm_json_get**](DefaultApi.md#stamm_json_get) | **GET** /stamm.json | Liste aller verfügbaren Messstationen.
[**stat_json_get**](DefaultApi.md#stat_json_get) | **GET** /stat.json | Statistiken zu den Messstationen.


# **id_json_get**
> InlineResponse2001 id_json_get(id)

Stammdaten und Zeitreihen zu einer bestimmten Messstation.

### Example

* Basic Authentication (basicAuth):

```python
import time
from deutschland import strahlenschutz
from deutschland.strahlenschutz.api import default_api
from deutschland.strahlenschutz.model.inline_response2001 import InlineResponse2001
from pprint import pprint
# Defining the host is optional and defaults to https://odlinfo.bfs.de/json
# See configuration.py for a list of all supported configuration parameters.
configuration = strahlenschutz.Configuration(
    host = "https://odlinfo.bfs.de/json"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = strahlenschutz.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with strahlenschutz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = 97741851 # int | ID der Messstation

    # example passing only required values which don't have defaults set
    try:
        # Stammdaten und Zeitreihen zu einer bestimmten Messstation.
        api_response = api_instance.id_json_get(id)
        pprint(api_response)
    except strahlenschutz.ApiException as e:
        print("Exception when calling DefaultApi->id_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID der Messstation |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreicher Abruf |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **idct_json_get**
> InlineResponse2002 idct_json_get(id)

Stammdaten und Zeitreihen zu einer bestimmten Messstation inklusive kosmisch-terrestrischer Daten.

### Example

* Basic Authentication (basicAuth):

```python
import time
from deutschland import strahlenschutz
from deutschland.strahlenschutz.api import default_api
from deutschland.strahlenschutz.model.inline_response2002 import InlineResponse2002
from pprint import pprint
# Defining the host is optional and defaults to https://odlinfo.bfs.de/json
# See configuration.py for a list of all supported configuration parameters.
configuration = strahlenschutz.Configuration(
    host = "https://odlinfo.bfs.de/json"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = strahlenschutz.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with strahlenschutz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = 97741851 # int | ID der Messstation

    # example passing only required values which don't have defaults set
    try:
        # Stammdaten und Zeitreihen zu einer bestimmten Messstation inklusive kosmisch-terrestrischer Daten.
        api_response = api_instance.idct_json_get(id)
        pprint(api_response)
    except strahlenschutz.ApiException as e:
        print("Exception when calling DefaultApi->idct_json_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID der Messstation |

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreicher Abruf |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stamm_json_get**
> InlineResponse200 stamm_json_get()

Liste aller verfügbaren Messstationen.

### Example

* Basic Authentication (basicAuth):

```python
import time
from deutschland import strahlenschutz
from deutschland.strahlenschutz.api import default_api
from deutschland.strahlenschutz.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to https://odlinfo.bfs.de/json
# See configuration.py for a list of all supported configuration parameters.
configuration = strahlenschutz.Configuration(
    host = "https://odlinfo.bfs.de/json"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = strahlenschutz.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with strahlenschutz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liste aller verfügbaren Messstationen.
        api_response = api_instance.stamm_json_get()
        pprint(api_response)
    except strahlenschutz.ApiException as e:
        print("Exception when calling DefaultApi->stamm_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON-Objekt der verfügbaren Messstationen |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stat_json_get**
> Statistics stat_json_get()

Statistiken zu den Messstationen.

### Example

* Basic Authentication (basicAuth):

```python
import time
from deutschland import strahlenschutz
from deutschland.strahlenschutz.api import default_api
from deutschland.strahlenschutz.model.statistics import Statistics
from pprint import pprint
# Defining the host is optional and defaults to https://odlinfo.bfs.de/json
# See configuration.py for a list of all supported configuration parameters.
configuration = strahlenschutz.Configuration(
    host = "https://odlinfo.bfs.de/json"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = strahlenschutz.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with strahlenschutz.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Statistiken zu den Messstationen.
        api_response = api_instance.stat_json_get()
        pprint(api_response)
    except strahlenschutz.ApiException as e:
        print("Exception when calling DefaultApi->stat_json_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Statistics**](Statistics.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Erfolgreicher Abruf |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

