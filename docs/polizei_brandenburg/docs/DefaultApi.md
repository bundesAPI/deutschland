# polizei_brandenburg.DefaultApi

All URIs are relative to *https://polizei.brandenburg.de/ipa_api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**news_version1_get**](DefaultApi.md#news_version1_get) | **GET** /news/version/1 | Nachrichten, Suchmeldungen der Polzei Brandenburg
[**pegel_version1_get**](DefaultApi.md#pegel_version1_get) | **GET** /pegel/version/1 | Pegelstände
[**reviere_version1_get**](DefaultApi.md#reviere_version1_get) | **GET** /reviere/version/1 | Liste aller Reviere der Polzei Brandenburg
[**vwd_version1_get**](DefaultApi.md#vwd_version1_get) | **GET** /vwd/version/1 | Verkehrswarnungen der Polzei Brandenburg
[**waldbrand_version1_get**](DefaultApi.md#waldbrand_version1_get) | **GET** /waldbrand/version/1 | Waldbrandwarnungen Brandenburg


# **news_version1_get**
> News news_version1_get()

Nachrichten, Suchmeldungen der Polzei Brandenburg

### Example


```python
import time
from deutschland import polizei_brandenburg
from deutschland.polizei_brandenburg.api import default_api
from deutschland.polizei_brandenburg.model.news import News
from pprint import pprint
# Defining the host is optional and defaults to https://polizei.brandenburg.de/ipa_api
# See configuration.py for a list of all supported configuration parameters.
configuration = polizei_brandenburg.Configuration(
    host = "https://polizei.brandenburg.de/ipa_api"
)


# Enter a context with an instance of the API client
with polizei_brandenburg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    count = 5000 # int | Number of results (optional)
    category = 8 # int | category id (optional)
    district = 500 # int | district id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Nachrichten, Suchmeldungen der Polzei Brandenburg
        api_response = api_instance.news_version1_get(count=count, category=category, district=district)
        pprint(api_response)
    except polizei_brandenburg.ApiException as e:
        print("Exception when calling DefaultApi->news_version1_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Number of results | [optional]
 **category** | **int**| category id | [optional]
 **district** | **int**| district id | [optional]

### Return type

[**News**](News.md)

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

# **pegel_version1_get**
> Pegel pegel_version1_get()

Pegelstände

### Example


```python
import time
from deutschland import polizei_brandenburg
from deutschland.polizei_brandenburg.api import default_api
from deutschland.polizei_brandenburg.model.pegel import Pegel
from pprint import pprint
# Defining the host is optional and defaults to https://polizei.brandenburg.de/ipa_api
# See configuration.py for a list of all supported configuration parameters.
configuration = polizei_brandenburg.Configuration(
    host = "https://polizei.brandenburg.de/ipa_api"
)


# Enter a context with an instance of the API client
with polizei_brandenburg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Pegelstände
        api_response = api_instance.pegel_version1_get()
        pprint(api_response)
    except polizei_brandenburg.ApiException as e:
        print("Exception when calling DefaultApi->pegel_version1_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Pegel**](Pegel.md)

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

# **reviere_version1_get**
> Reviere reviere_version1_get()

Liste aller Reviere der Polzei Brandenburg

### Example


```python
import time
from deutschland import polizei_brandenburg
from deutschland.polizei_brandenburg.api import default_api
from deutschland.polizei_brandenburg.model.reviere import Reviere
from pprint import pprint
# Defining the host is optional and defaults to https://polizei.brandenburg.de/ipa_api
# See configuration.py for a list of all supported configuration parameters.
configuration = polizei_brandenburg.Configuration(
    host = "https://polizei.brandenburg.de/ipa_api"
)


# Enter a context with an instance of the API client
with polizei_brandenburg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liste aller Reviere der Polzei Brandenburg
        api_response = api_instance.reviere_version1_get()
        pprint(api_response)
    except polizei_brandenburg.ApiException as e:
        print("Exception when calling DefaultApi->reviere_version1_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Reviere**](Reviere.md)

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

# **vwd_version1_get**
> Verkehr vwd_version1_get()

Verkehrswarnungen der Polzei Brandenburg

### Example


```python
import time
from deutschland import polizei_brandenburg
from deutschland.polizei_brandenburg.api import default_api
from deutschland.polizei_brandenburg.model.verkehr import Verkehr
from pprint import pprint
# Defining the host is optional and defaults to https://polizei.brandenburg.de/ipa_api
# See configuration.py for a list of all supported configuration parameters.
configuration = polizei_brandenburg.Configuration(
    host = "https://polizei.brandenburg.de/ipa_api"
)


# Enter a context with an instance of the API client
with polizei_brandenburg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Verkehrswarnungen der Polzei Brandenburg
        api_response = api_instance.vwd_version1_get()
        pprint(api_response)
    except polizei_brandenburg.ApiException as e:
        print("Exception when calling DefaultApi->vwd_version1_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Verkehr**](Verkehr.md)

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

# **waldbrand_version1_get**
> Waldbrand waldbrand_version1_get()

Waldbrandwarnungen Brandenburg

### Example


```python
import time
from deutschland import polizei_brandenburg
from deutschland.polizei_brandenburg.api import default_api
from deutschland.polizei_brandenburg.model.waldbrand import Waldbrand
from pprint import pprint
# Defining the host is optional and defaults to https://polizei.brandenburg.de/ipa_api
# See configuration.py for a list of all supported configuration parameters.
configuration = polizei_brandenburg.Configuration(
    host = "https://polizei.brandenburg.de/ipa_api"
)


# Enter a context with an instance of the API client
with polizei_brandenburg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Waldbrandwarnungen Brandenburg
        api_response = api_instance.waldbrand_version1_get()
        pprint(api_response)
    except polizei_brandenburg.ApiException as e:
        print("Exception when calling DefaultApi->waldbrand_version1_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Waldbrand**](Waldbrand.md)

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

