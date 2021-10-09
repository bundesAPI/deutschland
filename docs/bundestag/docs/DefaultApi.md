# bundestag.DefaultApi

All URIs are relative to *https://www.bundestag.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get**](DefaultApi.md#blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get) | **GET** /blueprint/servlet/content/{ARTICLE_ID}/asAppV2NewsarticleXml | Artikel Details
[**iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get**](DefaultApi.md#iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get) | **GET** /iptv/player/macros/_x_s-144277506/bttv/mobile/feed_vod.xml | Abruf eines Videos
[**static_appdata_plenum_v2_conferences_xml_get**](DefaultApi.md#static_appdata_plenum_v2_conferences_xml_get) | **GET** /static/appdata/plenum/v2/conferences.xml | Sitzungstag übersicht
[**static_appdata_plenum_v2_speaker_xml_get**](DefaultApi.md#static_appdata_plenum_v2_speaker_xml_get) | **GET** /static/appdata/plenum/v2/speaker.xml | Aktuelle Sprecher*in
[**xml_v2_ausschuesse_ausschussid_xml_get**](DefaultApi.md#xml_v2_ausschuesse_ausschussid_xml_get) | **GET** /xml/v2/ausschuesse/{AUSSCHUSS_ID}.xml | Übersicht über die Ausschüsse
[**xml_v2_ausschuesse_index_xml_get**](DefaultApi.md#xml_v2_ausschuesse_index_xml_get) | **GET** /xml/v2/ausschuesse/index.xml | Übersicht über die Ausschüsse
[**xml_v2_mdb_biografien_mdbid_xml_get**](DefaultApi.md#xml_v2_mdb_biografien_mdbid_xml_get) | **GET** /xml/v2/mdb/biografien/{MDB_ID}.xml | Abruf Details eines MDBS
[**xml_v2_mdb_index_xml_get**](DefaultApi.md#xml_v2_mdb_index_xml_get) | **GET** /xml/v2/mdb/index.xml | Übersicht über alle MDBS


# **blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get**
> str blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get(article_id)

Artikel Details

### Example


```python
import time
from deutschland import bundestag
from deutschland.bundestag.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag.Configuration(
    host = "https://www.bundestag.de"
)


# Enter a context with an instance of the API client
with bundestag.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    article_id = 849630 # int | ID des Nachrichtenbeitrags

    # example passing only required values which don't have defaults set
    try:
        # Artikel Details
        api_response = api_instance.blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get(article_id)
        pprint(api_response)
    except bundestag.ApiException as e:
        print("Exception when calling DefaultApi->blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| ID des Nachrichtenbeitrags |

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

# **iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get**
> str iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get(content_id)

Abruf eines Videos

### Example


```python
import time
from deutschland import bundestag
from deutschland.bundestag.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag.Configuration(
    host = "https://www.bundestag.de"
)


# Enter a context with an instance of the API client
with bundestag.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    content_id = 7529016 # int | ID des MDB

    # example passing only required values which don't have defaults set
    try:
        # Abruf eines Videos
        api_response = api_instance.iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get(content_id)
        pprint(api_response)
    except bundestag.ApiException as e:
        print("Exception when calling DefaultApi->iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | **int**| ID des MDB |

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

# **static_appdata_plenum_v2_conferences_xml_get**
> str static_appdata_plenum_v2_conferences_xml_get()

Sitzungstag übersicht

### Example


```python
import time
from deutschland import bundestag
from deutschland.bundestag.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag.Configuration(
    host = "https://www.bundestag.de"
)


# Enter a context with an instance of the API client
with bundestag.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Sitzungstag übersicht
        api_response = api_instance.static_appdata_plenum_v2_conferences_xml_get()
        pprint(api_response)
    except bundestag.ApiException as e:
        print("Exception when calling DefaultApi->static_appdata_plenum_v2_conferences_xml_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **static_appdata_plenum_v2_speaker_xml_get**
> str static_appdata_plenum_v2_speaker_xml_get()

Aktuelle Sprecher*in

### Example


```python
import time
from deutschland import bundestag
from deutschland.bundestag.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag.Configuration(
    host = "https://www.bundestag.de"
)


# Enter a context with an instance of the API client
with bundestag.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Aktuelle Sprecher*in
        api_response = api_instance.static_appdata_plenum_v2_speaker_xml_get()
        pprint(api_response)
    except bundestag.ApiException as e:
        print("Exception when calling DefaultApi->static_appdata_plenum_v2_speaker_xml_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **xml_v2_ausschuesse_ausschussid_xml_get**
> str xml_v2_ausschuesse_ausschussid_xml_get(ausschuss_id)

Übersicht über die Ausschüsse

### Example


```python
import time
from deutschland import bundestag
from deutschland.bundestag.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag.Configuration(
    host = "https://www.bundestag.de"
)


# Enter a context with an instance of the API client
with bundestag.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    ausschuss_id = "a11" # str | ID des Ausschusses

    # example passing only required values which don't have defaults set
    try:
        # Übersicht über die Ausschüsse
        api_response = api_instance.xml_v2_ausschuesse_ausschussid_xml_get(ausschuss_id)
        pprint(api_response)
    except bundestag.ApiException as e:
        print("Exception when calling DefaultApi->xml_v2_ausschuesse_ausschussid_xml_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ausschuss_id** | **str**| ID des Ausschusses |

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

# **xml_v2_ausschuesse_index_xml_get**
> str xml_v2_ausschuesse_index_xml_get()

Übersicht über die Ausschüsse

### Example


```python
import time
from deutschland import bundestag
from deutschland.bundestag.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag.Configuration(
    host = "https://www.bundestag.de"
)


# Enter a context with an instance of the API client
with bundestag.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Übersicht über die Ausschüsse
        api_response = api_instance.xml_v2_ausschuesse_index_xml_get()
        pprint(api_response)
    except bundestag.ApiException as e:
        print("Exception when calling DefaultApi->xml_v2_ausschuesse_index_xml_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **xml_v2_mdb_biografien_mdbid_xml_get**
> str xml_v2_mdb_biografien_mdbid_xml_get(mdb_id)

Abruf Details eines MDBS

### Example


```python
import time
from deutschland import bundestag
from deutschland.bundestag.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag.Configuration(
    host = "https://www.bundestag.de"
)


# Enter a context with an instance of the API client
with bundestag.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    mdb_id = 1769 # int | ID des MDB

    # example passing only required values which don't have defaults set
    try:
        # Abruf Details eines MDBS
        api_response = api_instance.xml_v2_mdb_biografien_mdbid_xml_get(mdb_id)
        pprint(api_response)
    except bundestag.ApiException as e:
        print("Exception when calling DefaultApi->xml_v2_mdb_biografien_mdbid_xml_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mdb_id** | **int**| ID des MDB |

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

# **xml_v2_mdb_index_xml_get**
> str xml_v2_mdb_index_xml_get()

Übersicht über alle MDBS

### Example


```python
import time
from deutschland import bundestag
from deutschland.bundestag.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag.Configuration(
    host = "https://www.bundestag.de"
)


# Enter a context with an instance of the API client
with bundestag.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Übersicht über alle MDBS
        api_response = api_instance.xml_v2_mdb_index_xml_get()
        pprint(api_response)
    except bundestag.ApiException as e:
        print("Exception when calling DefaultApi->xml_v2_mdb_index_xml_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

