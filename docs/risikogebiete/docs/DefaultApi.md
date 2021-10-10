# risikogebiete.DefaultApi

All URIs are relative to *https://api.einreiseanmeldung.de/reisendenportal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**risikogebiete_get**](DefaultApi.md#risikogebiete_get) | **GET** /risikogebiete | Liste der Länder


# **risikogebiete_get**
> RiskCountries risikogebiete_get()

Liste der Länder

Liste aller Länder mit Risikoeinstufung

### Example


```python
import time
from deutschland import risikogebiete
from deutschland.risikogebiete.api import default_api
from deutschland.risikogebiete.model.risk_countries import RiskCountries
from pprint import pprint
# Defining the host is optional and defaults to https://api.einreiseanmeldung.de/reisendenportal
# See configuration.py for a list of all supported configuration parameters.
configuration = risikogebiete.Configuration(
    host = "https://api.einreiseanmeldung.de/reisendenportal"
)


# Enter a context with an instance of the API client
with risikogebiete.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liste der Länder
        api_response = api_instance.risikogebiete_get()
        pprint(api_response)
    except risikogebiete.ApiException as e:
        print("Exception when calling DefaultApi->risikogebiete_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RiskCountries**](RiskCountries.md)

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

