# bundesrat.DefaultApi

All URIs are relative to *https://www.bundesrat.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**i_os_shared_docs2_mitglieder_mitglieder_table_xml_get**](DefaultApi.md#i_os_shared_docs2_mitglieder_mitglieder_table_xml_get) | **GET** /iOS/SharedDocs/2_Mitglieder/mitglieder_table.xml | Mitglieder
[**i_os_shared_docs3_plenum_plenum_aktuelle_sitzung_table_xml_get**](DefaultApi.md#i_os_shared_docs3_plenum_plenum_aktuelle_sitzung_table_xml_get) | **GET** /iOS/SharedDocs/3_Plenum/plenum_aktuelleSitzung_table.xml | Plenum aktuelle Sitzung
[**i_os_shared_docs3_plenum_plenum_naechste_sitzungen_xml_get**](DefaultApi.md#i_os_shared_docs3_plenum_plenum_naechste_sitzungen_xml_get) | **GET** /iOS/SharedDocs/3_Plenum/plenum_naechsteSitzungen.xml | Plenum nächste Sitzung
[**i_os_shared_docs3_plenum_plenum_to_chronologisch_table_xml_get**](DefaultApi.md#i_os_shared_docs3_plenum_plenum_to_chronologisch_table_xml_get) | **GET** /iOS/SharedDocs/3_Plenum/plenum_toChronologisch_table.xml | Plenum Chronologisch
[**i_osv301_aktuelles_aktuelles_table_xml_get**](DefaultApi.md#i_osv301_aktuelles_aktuelles_table_xml_get) | **GET** /iOS/v3/01_Aktuelles/aktuelles_table.xml | Aktuelles
[**i_osv302_termine_termine_table_xml_get**](DefaultApi.md#i_osv302_termine_termine_table_xml_get) | **GET** /iOS/v3/02_Termine/termine_table.xml | Termine
[**i_osv303_plenum_plenum_kompakt_table_xml_get**](DefaultApi.md#i_osv303_plenum_plenum_kompakt_table_xml_get) | **GET** /iOS/v3/03_Plenum/plenum_kompakt_table.xml | Plenum Kompakt
[**i_osv305_bundesrat_praesidium_bundesrat_praesidium_xml_get**](DefaultApi.md#i_osv305_bundesrat_praesidium_bundesrat_praesidium_xml_get) | **GET** /iOS/v3/05_Bundesrat/Praesidium/bundesrat_praesidium.xml | Präsidium
[**i_osv306_stimmen_stimmverteilung_xml_get**](DefaultApi.md#i_osv306_stimmen_stimmverteilung_xml_get) | **GET** /iOS/v3/06_Stimmen/stimmverteilung.xml | Stimmverteilung
[**i_osv3_startlist_table_xml_get**](DefaultApi.md#i_osv3_startlist_table_xml_get) | **GET** /iOS/v3/startlist_table.xml | Übersicht API Endpunkte


# **i_os_shared_docs2_mitglieder_mitglieder_table_xml_get**
> str i_os_shared_docs2_mitglieder_mitglieder_table_xml_get(view)

Mitglieder

### Example


```python
import time
from deutschland import bundesrat
from deutschland.bundesrat.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundesrat.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundesrat.Configuration(
    host = "https://www.bundesrat.de"
)


# Enter a context with an instance of the API client
with bundesrat.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    view = "renderXml" # str | Xml Ausabe

    # example passing only required values which don't have defaults set
    try:
        # Mitglieder
        api_response = api_instance.i_os_shared_docs2_mitglieder_mitglieder_table_xml_get(view)
        pprint(api_response)
    except bundesrat.ApiException as e:
        print("Exception when calling DefaultApi->i_os_shared_docs2_mitglieder_mitglieder_table_xml_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| Xml Ausabe |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_os_shared_docs3_plenum_plenum_aktuelle_sitzung_table_xml_get**
> str i_os_shared_docs3_plenum_plenum_aktuelle_sitzung_table_xml_get(view)

Plenum aktuelle Sitzung

### Example


```python
import time
from deutschland import bundesrat
from deutschland.bundesrat.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundesrat.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundesrat.Configuration(
    host = "https://www.bundesrat.de"
)


# Enter a context with an instance of the API client
with bundesrat.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    view = "renderXml" # str | Xml Ausabe

    # example passing only required values which don't have defaults set
    try:
        # Plenum aktuelle Sitzung
        api_response = api_instance.i_os_shared_docs3_plenum_plenum_aktuelle_sitzung_table_xml_get(view)
        pprint(api_response)
    except bundesrat.ApiException as e:
        print("Exception when calling DefaultApi->i_os_shared_docs3_plenum_plenum_aktuelle_sitzung_table_xml_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| Xml Ausabe |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_os_shared_docs3_plenum_plenum_naechste_sitzungen_xml_get**
> str i_os_shared_docs3_plenum_plenum_naechste_sitzungen_xml_get(view)

Plenum nächste Sitzung

### Example


```python
import time
from deutschland import bundesrat
from deutschland.bundesrat.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundesrat.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundesrat.Configuration(
    host = "https://www.bundesrat.de"
)


# Enter a context with an instance of the API client
with bundesrat.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    view = "renderXml" # str | Xml Ausabe

    # example passing only required values which don't have defaults set
    try:
        # Plenum nächste Sitzung
        api_response = api_instance.i_os_shared_docs3_plenum_plenum_naechste_sitzungen_xml_get(view)
        pprint(api_response)
    except bundesrat.ApiException as e:
        print("Exception when calling DefaultApi->i_os_shared_docs3_plenum_plenum_naechste_sitzungen_xml_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| Xml Ausabe |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_os_shared_docs3_plenum_plenum_to_chronologisch_table_xml_get**
> str i_os_shared_docs3_plenum_plenum_to_chronologisch_table_xml_get(view)

Plenum Chronologisch

### Example


```python
import time
from deutschland import bundesrat
from deutschland.bundesrat.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundesrat.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundesrat.Configuration(
    host = "https://www.bundesrat.de"
)


# Enter a context with an instance of the API client
with bundesrat.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    view = "renderXml" # str | Xml Ausabe

    # example passing only required values which don't have defaults set
    try:
        # Plenum Chronologisch
        api_response = api_instance.i_os_shared_docs3_plenum_plenum_to_chronologisch_table_xml_get(view)
        pprint(api_response)
    except bundesrat.ApiException as e:
        print("Exception when calling DefaultApi->i_os_shared_docs3_plenum_plenum_to_chronologisch_table_xml_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| Xml Ausabe |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_osv301_aktuelles_aktuelles_table_xml_get**
> str i_osv301_aktuelles_aktuelles_table_xml_get(view)

Aktuelles

### Example


```python
import time
from deutschland import bundesrat
from deutschland.bundesrat.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundesrat.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundesrat.Configuration(
    host = "https://www.bundesrat.de"
)


# Enter a context with an instance of the API client
with bundesrat.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    view = "renderXml" # str | Xml Ausabe

    # example passing only required values which don't have defaults set
    try:
        # Aktuelles
        api_response = api_instance.i_osv301_aktuelles_aktuelles_table_xml_get(view)
        pprint(api_response)
    except bundesrat.ApiException as e:
        print("Exception when calling DefaultApi->i_osv301_aktuelles_aktuelles_table_xml_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| Xml Ausabe |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_osv302_termine_termine_table_xml_get**
> str i_osv302_termine_termine_table_xml_get(view)

Termine

### Example


```python
import time
from deutschland import bundesrat
from deutschland.bundesrat.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundesrat.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundesrat.Configuration(
    host = "https://www.bundesrat.de"
)


# Enter a context with an instance of the API client
with bundesrat.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    view = "renderXml" # str | Xml Ausabe

    # example passing only required values which don't have defaults set
    try:
        # Termine
        api_response = api_instance.i_osv302_termine_termine_table_xml_get(view)
        pprint(api_response)
    except bundesrat.ApiException as e:
        print("Exception when calling DefaultApi->i_osv302_termine_termine_table_xml_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| Xml Ausabe |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_osv303_plenum_plenum_kompakt_table_xml_get**
> str i_osv303_plenum_plenum_kompakt_table_xml_get(view)

Plenum Kompakt

### Example


```python
import time
from deutschland import bundesrat
from deutschland.bundesrat.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundesrat.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundesrat.Configuration(
    host = "https://www.bundesrat.de"
)


# Enter a context with an instance of the API client
with bundesrat.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    view = "renderXml" # str | Xml Ausabe

    # example passing only required values which don't have defaults set
    try:
        # Plenum Kompakt
        api_response = api_instance.i_osv303_plenum_plenum_kompakt_table_xml_get(view)
        pprint(api_response)
    except bundesrat.ApiException as e:
        print("Exception when calling DefaultApi->i_osv303_plenum_plenum_kompakt_table_xml_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| Xml Ausabe |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_osv305_bundesrat_praesidium_bundesrat_praesidium_xml_get**
> str i_osv305_bundesrat_praesidium_bundesrat_praesidium_xml_get(view)

Präsidium

### Example


```python
import time
from deutschland import bundesrat
from deutschland.bundesrat.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundesrat.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundesrat.Configuration(
    host = "https://www.bundesrat.de"
)


# Enter a context with an instance of the API client
with bundesrat.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    view = "renderXml" # str | Xml Ausabe

    # example passing only required values which don't have defaults set
    try:
        # Präsidium
        api_response = api_instance.i_osv305_bundesrat_praesidium_bundesrat_praesidium_xml_get(view)
        pprint(api_response)
    except bundesrat.ApiException as e:
        print("Exception when calling DefaultApi->i_osv305_bundesrat_praesidium_bundesrat_praesidium_xml_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| Xml Ausabe |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_osv306_stimmen_stimmverteilung_xml_get**
> str i_osv306_stimmen_stimmverteilung_xml_get(view)

Stimmverteilung

### Example


```python
import time
from deutschland import bundesrat
from deutschland.bundesrat.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundesrat.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundesrat.Configuration(
    host = "https://www.bundesrat.de"
)


# Enter a context with an instance of the API client
with bundesrat.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    view = "renderXml" # str | Xml Ausabe

    # example passing only required values which don't have defaults set
    try:
        # Stimmverteilung
        api_response = api_instance.i_osv306_stimmen_stimmverteilung_xml_get(view)
        pprint(api_response)
    except bundesrat.ApiException as e:
        print("Exception when calling DefaultApi->i_osv306_stimmen_stimmverteilung_xml_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| Xml Ausabe |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_osv3_startlist_table_xml_get**
> str i_osv3_startlist_table_xml_get(view)

Übersicht API Endpunkte

### Example


```python
import time
from deutschland import bundesrat
from deutschland.bundesrat.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundesrat.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundesrat.Configuration(
    host = "https://www.bundesrat.de"
)


# Enter a context with an instance of the API client
with bundesrat.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    view = "renderXml" # str | Xml Ausabe

    # example passing only required values which don't have defaults set
    try:
        # Übersicht API Endpunkte
        api_response = api_instance.i_osv3_startlist_table_xml_get(view)
        pprint(api_response)
    except bundesrat.ApiException as e:
        print("Exception when calling DefaultApi->i_osv3_startlist_table_xml_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| Xml Ausabe |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

