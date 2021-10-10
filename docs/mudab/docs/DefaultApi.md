# mudab.DefaultApi

All URIs are relative to *https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_mess_stationen**](DefaultApi.md#list_mess_stationen) | **POST** /STATION_SMALL | Liste aller Messstationen
[**list_parameter**](DefaultApi.md#list_parameter) | **POST** /MV_PARAMETER | Liste aller Parameter
[**list_parameter_values**](DefaultApi.md#list_parameter_values) | **POST** /MV_STATION_MSMNT | Liste aller Messwerte
[**list_parameters_biologie**](DefaultApi.md#list_parameters_biologie) | **POST** /MV_PARAMETER_BIOLOGIE | Liste aller Parameter im Biologie Kompartiment
[**list_parameters_biota**](DefaultApi.md#list_parameters_biota) | **POST** /MV_PARAMETER_BIOTA | Liste aller Parameter im Biota Kompartiment
[**list_parameters_sediment**](DefaultApi.md#list_parameters_sediment) | **POST** /MV_PARAMETER_SEDIMENT | Liste aller Parameter im Sediment Kompartiment
[**list_parameters_wasser**](DefaultApi.md#list_parameters_wasser) | **POST** /MV_PARAMETER_WASSER | Liste aller Parameter im Wasser Kompartiment
[**list_plc_stations**](DefaultApi.md#list_plc_stations) | **POST** /V_PLC_STATION | Liste aller HELCOM PLC Stationen
[**list_projekt_stationen**](DefaultApi.md#list_projekt_stationen) | **POST** /PROJECTSTATION_SMALL | Liste aller Projekt Stationen


# **list_mess_stationen**
> InlineResponse2001 list_mess_stationen()

Liste aller Messstationen

Gibt eine filterbare Liste aller Messtationen in der Datenbank zurück. Filterbare Attribute sind die Felder die aus dem Messstation Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.filter_request import FilterRequest
from deutschland.mudab.model.inline_response2001 import InlineResponse2001
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Messstationen
        api_response = api_instance.list_mess_stationen(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_mess_stationen: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parameter**
> InlineResponse2002 list_parameter()

Liste aller Parameter

Gibt eine filterbare Liste aller Parameter in der Datenbank zurück. Filterbare Attribute sind die Felder die aus dem Parameter Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.inline_response2002 import InlineResponse2002
from deutschland.mudab.model.filter_request import FilterRequest
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Parameter
        api_response = api_instance.list_parameter(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_parameter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parameter_values**
> InlineResponse2003 list_parameter_values()

Liste aller Messwerte

Gibt eine filterbare Liste aller Messwerte in der Datenbank zurück. Filterbare Attribute sind die Felder die aus dem ParameterValue Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.inline_response2003 import InlineResponse2003
from deutschland.mudab.model.filter_request import FilterRequest
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Messwerte
        api_response = api_instance.list_parameter_values(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_parameter_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parameters_biologie**
> InlineResponse2004 list_parameters_biologie()

Liste aller Parameter im Biologie Kompartiment

Gibt eine filterbare Liste aller Parameter in der Datenbank aus dem Kompartiment Biologie zurück. Filterbare Attribute sind die Felder die aus dem Parameter Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.inline_response2004 import InlineResponse2004
from deutschland.mudab.model.filter_request import FilterRequest
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Parameter im Biologie Kompartiment
        api_response = api_instance.list_parameters_biologie(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_parameters_biologie: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parameters_biota**
> InlineResponse2005 list_parameters_biota()

Liste aller Parameter im Biota Kompartiment

Gibt eine filterbare Liste aller Parameter in der Datenbank aus dem Kompartiment Biota zurück. Filterbare Attribute sind die Felder die aus dem Parameter Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.inline_response2005 import InlineResponse2005
from deutschland.mudab.model.filter_request import FilterRequest
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Parameter im Biota Kompartiment
        api_response = api_instance.list_parameters_biota(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_parameters_biota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parameters_sediment**
> InlineResponse2007 list_parameters_sediment()

Liste aller Parameter im Sediment Kompartiment

Gibt eine filterbare Liste aller Parameter in der Datenbank aus dem Kompartiment Sediment zurück. Filterbare Attribute sind die Felder die aus dem Parameter Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.inline_response2007 import InlineResponse2007
from deutschland.mudab.model.filter_request import FilterRequest
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Parameter im Sediment Kompartiment
        api_response = api_instance.list_parameters_sediment(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_parameters_sediment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parameters_wasser**
> InlineResponse2006 list_parameters_wasser()

Liste aller Parameter im Wasser Kompartiment

Gibt eine filterbare Liste aller Parameter in der Datenbank aus dem Kompartiment Wasser zurück. Filterbare Attribute sind die Felder die aus dem Parameter Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.filter_request import FilterRequest
from deutschland.mudab.model.inline_response2006 import InlineResponse2006
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Parameter im Wasser Kompartiment
        api_response = api_instance.list_parameters_wasser(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_parameters_wasser: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_plc_stations**
> InlineResponse2008 list_plc_stations()

Liste aller HELCOM PLC Stationen

Gibt eine filterbare Liste aller HELCOM PLC Stationen in der Datenbank zurück. Filterbare Attribute sind die Felder die aus dem HelcomPLCStation Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.inline_response2008 import InlineResponse2008
from deutschland.mudab.model.filter_request import FilterRequest
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller HELCOM PLC Stationen
        api_response = api_instance.list_plc_stations(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_plc_stations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projekt_stationen**
> InlineResponse200 list_projekt_stationen()

Liste aller Projekt Stationen

Gibt eine filterbare Liste aller Projektstation in der Datenbank zurück. Filterbare Attribute sind die Felder die aus dem ProjectStation Schema kommen. 

### Example


```python
import time
from deutschland import mudab
from deutschland.mudab.api import default_api
from deutschland.mudab.model.filter_request import FilterRequest
from deutschland.mudab.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements
# See configuration.py for a list of all supported configuration parameters.
configuration = mudab.Configuration(
    host = "https://geoportal.bafg.de/MUDABAnwendung/rest/BaseController/FilterElements"
)


# Enter a context with an instance of the API client
with mudab.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter_request = FilterRequest(
        filter=Filter(
            _or=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
            _and=FilterAction(
                col="col_example",
                op="op_example",
                value="value_example",
            ),
        ),
        range=Range(
            _from=1,
            count=1,
        ),
        orderby=Orderby(
            col="col_example",
            dir="asc",
        ),
    ) # FilterRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Liste aller Projekt Stationen
        api_response = api_instance.list_projekt_stationen(filter_request=filter_request)
        pprint(api_response)
    except mudab.ApiException as e:
        print("Exception when calling DefaultApi->list_projekt_stationen: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_request** | [**FilterRequest**](FilterRequest.md)|  | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

