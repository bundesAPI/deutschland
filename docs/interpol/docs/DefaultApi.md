# interpol.DefaultApi

All URIs are relative to *https://ws-public.interpol.int*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notices_v1_red_get**](DefaultApi.md#notices_v1_red_get) | **GET** /notices/v1/red | Get Red Notices
[**notices_v1_red_notice_id_get**](DefaultApi.md#notices_v1_red_notice_id_get) | **GET** /notices/v1/red/{noticeID} | Get Red Notice Details
[**notices_v1_red_notice_id_images_get**](DefaultApi.md#notices_v1_red_notice_id_images_get) | **GET** /notices/v1/red/{noticeID}/images | Get Red Notice Images


# **notices_v1_red_get**
> RedNotices notices_v1_red_get()

Get Red Notices

### Example


```python
import time
from deutschland import interpol
from deutschland.interpol.api import default_api
from deutschland.interpol.model.red_notices import RedNotices
from pprint import pprint
# Defining the host is optional and defaults to https://ws-public.interpol.int
# See configuration.py for a list of all supported configuration parameters.
configuration = interpol.Configuration(
    host = "https://ws-public.interpol.int"
)


# Enter a context with an instance of the API client
with interpol.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    forename = "DANIELA" # str | First name (optional)
    name = "Klette" # str | Last name (optional)
    nationality = "DE" # str | Two digit country code (optional)
    age_max = 120 # int | maximum age (optional)
    age_min = 18 # int | minimum age (optional)
    free_text = "" # str | Free text query (optional)
    sex_id = "F" # str | Free text query (optional)
    arrest_warrant_country_id = "DE" # str | Two digit country code (optional)
    page = 1 # int | pagination - starts with 1 (optional)
    result_per_page = 200 # int | resultPerPage (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Red Notices
        api_response = api_instance.notices_v1_red_get(forename=forename, name=name, nationality=nationality, age_max=age_max, age_min=age_min, free_text=free_text, sex_id=sex_id, arrest_warrant_country_id=arrest_warrant_country_id, page=page, result_per_page=result_per_page)
        pprint(api_response)
    except interpol.ApiException as e:
        print("Exception when calling DefaultApi->notices_v1_red_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forename** | **str**| First name | [optional]
 **name** | **str**| Last name | [optional]
 **nationality** | **str**| Two digit country code | [optional]
 **age_max** | **int**| maximum age | [optional]
 **age_min** | **int**| minimum age | [optional]
 **free_text** | **str**| Free text query | [optional]
 **sex_id** | **str**| Free text query | [optional]
 **arrest_warrant_country_id** | **str**| Two digit country code | [optional]
 **page** | **int**| pagination - starts with 1 | [optional]
 **result_per_page** | **int**| resultPerPage | [optional]

### Return type

[**RedNotices**](RedNotices.md)

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

# **notices_v1_red_notice_id_get**
> RedNoticeDetail notices_v1_red_notice_id_get(notice_id)

Get Red Notice Details

### Example


```python
import time
from deutschland import interpol
from deutschland.interpol.api import default_api
from deutschland.interpol.model.red_notice_detail import RedNoticeDetail
from pprint import pprint
# Defining the host is optional and defaults to https://ws-public.interpol.int
# See configuration.py for a list of all supported configuration parameters.
configuration = interpol.Configuration(
    host = "https://ws-public.interpol.int"
)


# Enter a context with an instance of the API client
with interpol.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    notice_id = "1993-27493" # str | Notice ID

    # example passing only required values which don't have defaults set
    try:
        # Get Red Notice Details
        api_response = api_instance.notices_v1_red_notice_id_get(notice_id)
        pprint(api_response)
    except interpol.ApiException as e:
        print("Exception when calling DefaultApi->notices_v1_red_notice_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notice_id** | **str**| Notice ID |

### Return type

[**RedNoticeDetail**](RedNoticeDetail.md)

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

# **notices_v1_red_notice_id_images_get**
> RedNoticeDetailImages notices_v1_red_notice_id_images_get(notice_id)

Get Red Notice Images

### Example


```python
import time
from deutschland import interpol
from deutschland.interpol.api import default_api
from deutschland.interpol.model.red_notice_detail_images import RedNoticeDetailImages
from pprint import pprint
# Defining the host is optional and defaults to https://ws-public.interpol.int
# See configuration.py for a list of all supported configuration parameters.
configuration = interpol.Configuration(
    host = "https://ws-public.interpol.int"
)


# Enter a context with an instance of the API client
with interpol.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    notice_id = "1993-27493" # str | Notice ID

    # example passing only required values which don't have defaults set
    try:
        # Get Red Notice Images
        api_response = api_instance.notices_v1_red_notice_id_images_get(notice_id)
        pprint(api_response)
    except interpol.ApiException as e:
        print("Exception when calling DefaultApi->notices_v1_red_notice_id_images_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notice_id** | **str**| Notice ID |

### Return type

[**RedNoticeDetailImages**](RedNoticeDetailImages.md)

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

