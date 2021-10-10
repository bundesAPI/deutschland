# zoll.DefaultApi

All URIs are relative to *https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kategorien_get**](DefaultApi.md#kategorien_get) | **GET** /kategorien | Produktkategorien
[**kurse_app_kurs_export_txt_get**](DefaultApi.md#kurse_app_kurs_export_txt_get) | **GET** /Kurse/App/KursExport.txt | Währungskurse
[**laender_get**](DefaultApi.md#laender_get) | **GET** /laender | 
[**produkte_get**](DefaultApi.md#produkte_get) | **GET** /produkte | Produkte
[**produkteinheiten_get**](DefaultApi.md#produkteinheiten_get) | **GET** /produkteinheiten | 
[**produktgruppen_get**](DefaultApi.md#produktgruppen_get) | **GET** /produktgruppen | 


# **kategorien_get**
> Categories kategorien_get()

Produktkategorien

Produktkategoriendatenbank

### Example


```python
import time
from deutschland import zoll
from deutschland.zoll.api import default_api
from deutschland.zoll.model.categories import Categories
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve
# See configuration.py for a list of all supported configuration parameters.
configuration = zoll.Configuration(
    host = "https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve"
)


# Enter a context with an instance of the API client
with zoll.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    last_modified_date = "" # str |  (optional) if omitted the server will use the default value of ""

    # example passing only required values which don't have defaults set
    try:
        # Produktkategorien
        api_response = api_instance.kategorien_get()
        pprint(api_response)
    except zoll.ApiException as e:
        print("Exception when calling DefaultApi->kategorien_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Produktkategorien
        api_response = api_instance.kategorien_get(last_modified_date=last_modified_date)
        pprint(api_response)
    except zoll.ApiException as e:
        print("Exception when calling DefaultApi->kategorien_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | **str**|  | defaults to "ZUP"
 **view** | **str**|  | defaults to "renderJson[App]"
 **user_agent** | **str**|  | defaults to "zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0"
 **last_modified_date** | **str**|  | [optional] if omitted the server will use the default value of ""

### Return type

[**Categories**](Categories.md)

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

# **kurse_app_kurs_export_txt_get**
> ExchangeRates kurse_app_kurs_export_txt_get()

Währungskurse

Liste aller Länder mit Risikoeinstufung

### Example


```python
import time
from deutschland import zoll
from deutschland.zoll.api import default_api
from deutschland.zoll.model.exchange_rates import ExchangeRates
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve
# See configuration.py for a list of all supported configuration parameters.
configuration = zoll.Configuration(
    host = "https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve"
)


# Enter a context with an instance of the API client
with zoll.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Währungskurse
        api_response = api_instance.kurse_app_kurs_export_txt_get()
        pprint(api_response)
    except zoll.ApiException as e:
        print("Exception when calling DefaultApi->kurse_app_kurs_export_txt_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**|  | defaults to "jsonexportkurseZOLLWeb"
 **user_agent** | **str**|  | defaults to "zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0"

### Return type

[**ExchangeRates**](ExchangeRates.md)

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

# **laender_get**
> Countries laender_get()



Länder

### Example


```python
import time
from deutschland import zoll
from deutschland.zoll.api import default_api
from deutschland.zoll.model.countries import Countries
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve
# See configuration.py for a list of all supported configuration parameters.
configuration = zoll.Configuration(
    host = "https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve"
)


# Enter a context with an instance of the API client
with zoll.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    last_modified_date = "" # str |  (optional) if omitted the server will use the default value of ""

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.laender_get()
        pprint(api_response)
    except zoll.ApiException as e:
        print("Exception when calling DefaultApi->laender_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.laender_get(last_modified_date=last_modified_date)
        pprint(api_response)
    except zoll.ApiException as e:
        print("Exception when calling DefaultApi->laender_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | **str**|  | defaults to "ZUP"
 **view** | **str**|  | defaults to "renderJson[App]"
 **user_agent** | **str**|  | defaults to "zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0"
 **last_modified_date** | **str**|  | [optional] if omitted the server will use the default value of ""

### Return type

[**Countries**](Countries.md)

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

# **produkte_get**
> Products produkte_get()

Produkte

Produktdatenbank mit Zolltarifen

### Example


```python
import time
from deutschland import zoll
from deutschland.zoll.api import default_api
from deutschland.zoll.model.products import Products
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve
# See configuration.py for a list of all supported configuration parameters.
configuration = zoll.Configuration(
    host = "https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve"
)


# Enter a context with an instance of the API client
with zoll.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    last_modified_date = "" # str |  (optional) if omitted the server will use the default value of ""

    # example passing only required values which don't have defaults set
    try:
        # Produkte
        api_response = api_instance.produkte_get()
        pprint(api_response)
    except zoll.ApiException as e:
        print("Exception when calling DefaultApi->produkte_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Produkte
        api_response = api_instance.produkte_get(last_modified_date=last_modified_date)
        pprint(api_response)
    except zoll.ApiException as e:
        print("Exception when calling DefaultApi->produkte_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | **str**|  | defaults to "ZUP"
 **view** | **str**|  | defaults to "renderJson[App]"
 **user_agent** | **str**|  | defaults to "zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0"
 **last_modified_date** | **str**|  | [optional] if omitted the server will use the default value of ""

### Return type

[**Products**](Products.md)

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

# **produkteinheiten_get**
> ProductUnits produkteinheiten_get()



Produkteinheiten

### Example


```python
import time
from deutschland import zoll
from deutschland.zoll.api import default_api
from deutschland.zoll.model.product_units import ProductUnits
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve
# See configuration.py for a list of all supported configuration parameters.
configuration = zoll.Configuration(
    host = "https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve"
)


# Enter a context with an instance of the API client
with zoll.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    last_modified_date = "" # str |  (optional) if omitted the server will use the default value of ""

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.produkteinheiten_get()
        pprint(api_response)
    except zoll.ApiException as e:
        print("Exception when calling DefaultApi->produkteinheiten_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.produkteinheiten_get(last_modified_date=last_modified_date)
        pprint(api_response)
    except zoll.ApiException as e:
        print("Exception when calling DefaultApi->produkteinheiten_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | **str**|  | defaults to "ZUP"
 **view** | **str**|  | defaults to "renderJson[App]"
 **user_agent** | **str**|  | defaults to "zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0"
 **last_modified_date** | **str**|  | [optional] if omitted the server will use the default value of ""

### Return type

[**ProductUnits**](ProductUnits.md)

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

# **produktgruppen_get**
> ProductGroups produktgruppen_get()



Produktgruppen

### Example


```python
import time
from deutschland import zoll
from deutschland.zoll.api import default_api
from deutschland.zoll.model.product_groups import ProductGroups
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve
# See configuration.py for a list of all supported configuration parameters.
configuration = zoll.Configuration(
    host = "https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve"
)


# Enter a context with an instance of the API client
with zoll.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    last_modified_date = "" # str |  (optional) if omitted the server will use the default value of ""

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.produktgruppen_get()
        pprint(api_response)
    except zoll.ApiException as e:
        print("Exception when calling DefaultApi->produktgruppen_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.produktgruppen_get(last_modified_date=last_modified_date)
        pprint(api_response)
    except zoll.ApiException as e:
        print("Exception when calling DefaultApi->produktgruppen_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | **str**|  | defaults to "ZUP"
 **view** | **str**|  | defaults to "renderJson[App]"
 **user_agent** | **str**|  | defaults to "zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0"
 **last_modified_date** | **str**|  | [optional] if omitted the server will use the default value of ""

### Return type

[**ProductGroups**](ProductGroups.md)

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

