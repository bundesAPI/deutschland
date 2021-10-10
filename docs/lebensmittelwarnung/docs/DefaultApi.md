# lebensmittelwarnung.DefaultApi

All URIs are relative to *https://megov.bayern.de/verbraucherschutz/baystmuv-verbraucherinfo/rest/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_warnungen**](DefaultApi.md#list_warnungen) | **POST** /warnings/merged | Liste aller Lebensmittel und Produktwarnungen


# **list_warnungen**
> Response list_warnungen()

Liste aller Lebensmittel und Produktwarnungen

Gibt eine Liste aller Lebensmittel und Produktwarnungen zurück.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import time
from deutschland import lebensmittelwarnung
from deutschland.lebensmittelwarnung.api import default_api
from deutschland.lebensmittelwarnung.model.inline_object import InlineObject
from deutschland.lebensmittelwarnung.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to https://megov.bayern.de/verbraucherschutz/baystmuv-verbraucherinfo/rest/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lebensmittelwarnung.Configuration(
    host = "https://megov.bayern.de/verbraucherschutz/baystmuv-verbraucherinfo/rest/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with lebensmittelwarnung.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    inline_object = InlineObject(
        food=RequestOptions(
            rows=500,
            sort="publishedDate desc, title asc",
            start=11,
            fq=["publishedDate > 1630067654000"],
        ),
        products=RequestOptions(
            rows=500,
            sort="publishedDate desc, title asc",
            start=11,
            fq=["publishedDate > 1630067654000"],
        ),
    ) # InlineObject |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Lebensmittel und Produktwarnungen
        api_response = api_instance.list_warnungen(inline_object=inline_object)
        pprint(api_response)
    except lebensmittelwarnung.ApiException as e:
        print("Exception when calling DefaultApi->list_warnungen: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional]

### Return type

[**Response**](Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

