# destatis.DefaultApi

All URIs are relative to *https://www-genesis.destatis.de/genesisWS/rest/2020*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chart2result**](DefaultApi.md#chart2result) | **GET** /data/chart2result | 
[**chart2table**](DefaultApi.md#chart2table) | **GET** /data/chart2table | 
[**chart2timeseries**](DefaultApi.md#chart2timeseries) | **GET** /data/chart2timeseries | 
[**cube**](DefaultApi.md#cube) | **GET** /data/cube | 
[**cube_meta**](DefaultApi.md#cube_meta) | **GET** /metadata/cube | 
[**cubefile**](DefaultApi.md#cubefile) | **GET** /data/cubefile | 
[**cubes**](DefaultApi.md#cubes) | **GET** /catalogue/cubes | 
[**cubes2statistic**](DefaultApi.md#cubes2statistic) | **GET** /catalogue/cubes2statistic | 
[**cubes2variable**](DefaultApi.md#cubes2variable) | **GET** /catalogue/cubes2variable | 
[**find**](DefaultApi.md#find) | **GET** /find/find | 
[**jobs**](DefaultApi.md#jobs) | **GET** /catalogue/jobs | 
[**logincheck**](DefaultApi.md#logincheck) | **GET** /helloworld/logincheck | 
[**map2result**](DefaultApi.md#map2result) | **GET** /data/map2result | 
[**map2table**](DefaultApi.md#map2table) | **GET** /data/map2table | 
[**map2timeseries**](DefaultApi.md#map2timeseries) | **GET** /data/map2timeseries | 
[**modifieddata**](DefaultApi.md#modifieddata) | **GET** /catalogue/modifieddata | 
[**password**](DefaultApi.md#password) | **GET** /profile/password | 
[**qualitysigns**](DefaultApi.md#qualitysigns) | **GET** /catalogue/qualitysigns | 
[**remove_result**](DefaultApi.md#remove_result) | **GET** /profile/removeResult | 
[**result**](DefaultApi.md#result) | **GET** /data/result | 
[**resultfile**](DefaultApi.md#resultfile) | **GET** /data/resultfile | 
[**results**](DefaultApi.md#results) | **GET** /catalogue/results | 
[**statistic**](DefaultApi.md#statistic) | **GET** /metadata/statistic | 
[**statistics**](DefaultApi.md#statistics) | **GET** /catalogue/statistics | 
[**statistics2variable**](DefaultApi.md#statistics2variable) | **GET** /catalogue/statistics2variable | 
[**table**](DefaultApi.md#table) | **GET** /data/table | 
[**table_meta**](DefaultApi.md#table_meta) | **GET** /metadata/table | 
[**tablefile**](DefaultApi.md#tablefile) | **GET** /data/tablefile | 
[**tables**](DefaultApi.md#tables) | **GET** /catalogue/tables | 
[**tables2statistic**](DefaultApi.md#tables2statistic) | **GET** /catalogue/tables2statistic | 
[**tables2variable**](DefaultApi.md#tables2variable) | **GET** /catalogue/tables2variable | 
[**terms**](DefaultApi.md#terms) | **GET** /catalogue/terms | 
[**timeseries**](DefaultApi.md#timeseries) | **GET** /catalogue/timeseries | 
[**timeseries2statistic**](DefaultApi.md#timeseries2statistic) | **GET** /catalogue/timeseries2statistic | 
[**timeseries2variable**](DefaultApi.md#timeseries2variable) | **GET** /catalogue/timeseries2variable | 
[**timeseries_data**](DefaultApi.md#timeseries_data) | **GET** /data/timeseries | 
[**timeseries_meta**](DefaultApi.md#timeseries_meta) | **GET** /metadata/timeseries | 
[**timeseriesfile**](DefaultApi.md#timeseriesfile) | **GET** /data/timeseriesfile | 
[**value**](DefaultApi.md#value) | **GET** /metadata/value | 
[**values**](DefaultApi.md#values) | **GET** /catalogue/values | 
[**values2variable**](DefaultApi.md#values2variable) | **GET** /catalogue/values2variable | 
[**variable**](DefaultApi.md#variable) | **GET** /metadata/variable | 
[**variables**](DefaultApi.md#variables) | **GET** /catalogue/variables | 
[**variables2statistic**](DefaultApi.md#variables2statistic) | **GET** /catalogue/variables2statistic | 
[**whoami**](DefaultApi.md#whoami) | **GET** /helloworld/whoami | 


# **chart2result**
> chart2result()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    charttype = "0" # str |  (optional) if omitted the server will use the default value of "0"
    drawpoints = "false" # str |  (optional) if omitted the server will use the default value of "false"
    zoom = "2" # str |  (optional) if omitted the server will use the default value of "2"
    focus = "false" # str |  (optional) if omitted the server will use the default value of "false"
    tops = "false" # str |  (optional) if omitted the server will use the default value of "false"
    format = "png" # str |  (optional) if omitted the server will use the default value of "png"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.chart2result(username=username, password=password, name=name, area=area, charttype=charttype, drawpoints=drawpoints, zoom=zoom, focus=focus, tops=tops, format=format, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->chart2result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **charttype** | **str**|  | [optional] if omitted the server will use the default value of "0"
 **drawpoints** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **zoom** | **str**|  | [optional] if omitted the server will use the default value of "2"
 **focus** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **tops** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **format** | **str**|  | [optional] if omitted the server will use the default value of "png"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chart2table**
> chart2table()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    charttype = "0" # str |  (optional) if omitted the server will use the default value of "0"
    drawpoints = "false" # str |  (optional) if omitted the server will use the default value of "false"
    zoom = "2" # str |  (optional) if omitted the server will use the default value of "2"
    focus = "false" # str |  (optional) if omitted the server will use the default value of "false"
    tops = "false" # str |  (optional) if omitted the server will use the default value of "false"
    startyear = "startyear_example" # str |  (optional)
    endyear = "endyear_example" # str |  (optional)
    timeslices = "timeslices_example" # str |  (optional)
    regionalvariable = "regionalvariable_example" # str |  (optional)
    regionalkey = "regionalkey_example" # str |  (optional)
    classifyingvariable1 = "classifyingvariable1_example" # str |  (optional)
    classifyingkey1 = "classifyingkey1_example" # str |  (optional)
    classifyingvariable2 = "classifyingvariable2_example" # str |  (optional)
    classifyingkey2 = "classifyingkey2_example" # str |  (optional)
    classifyingvariable3 = "classifyingvariable3_example" # str |  (optional)
    classifyingkey3 = "classifyingkey3_example" # str |  (optional)
    format = "png" # str |  (optional) if omitted the server will use the default value of "png"
    stand = "01.01.1970 01:00" # str |  (optional) if omitted the server will use the default value of "01.01.1970 01:00"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.chart2table(username=username, password=password, name=name, area=area, charttype=charttype, drawpoints=drawpoints, zoom=zoom, focus=focus, tops=tops, startyear=startyear, endyear=endyear, timeslices=timeslices, regionalvariable=regionalvariable, regionalkey=regionalkey, classifyingvariable1=classifyingvariable1, classifyingkey1=classifyingkey1, classifyingvariable2=classifyingvariable2, classifyingkey2=classifyingkey2, classifyingvariable3=classifyingvariable3, classifyingkey3=classifyingkey3, format=format, stand=stand, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->chart2table: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **charttype** | **str**|  | [optional] if omitted the server will use the default value of "0"
 **drawpoints** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **zoom** | **str**|  | [optional] if omitted the server will use the default value of "2"
 **focus** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **tops** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **startyear** | **str**|  | [optional]
 **endyear** | **str**|  | [optional]
 **timeslices** | **str**|  | [optional]
 **regionalvariable** | **str**|  | [optional]
 **regionalkey** | **str**|  | [optional]
 **classifyingvariable1** | **str**|  | [optional]
 **classifyingkey1** | **str**|  | [optional]
 **classifyingvariable2** | **str**|  | [optional]
 **classifyingkey2** | **str**|  | [optional]
 **classifyingvariable3** | **str**|  | [optional]
 **classifyingkey3** | **str**|  | [optional]
 **format** | **str**|  | [optional] if omitted the server will use the default value of "png"
 **stand** | **str**|  | [optional] if omitted the server will use the default value of "01.01.1970 01:00"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chart2timeseries**
> chart2timeseries()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    charttype = "0" # str |  (optional) if omitted the server will use the default value of "0"
    drawpoints = "false" # str |  (optional) if omitted the server will use the default value of "false"
    zoom = "2" # str |  (optional) if omitted the server will use the default value of "2"
    focus = "false" # str |  (optional) if omitted the server will use the default value of "false"
    tops = "false" # str |  (optional) if omitted the server will use the default value of "false"
    contents = "contents_example" # str |  (optional)
    startyear = "startyear_example" # str |  (optional)
    endyear = "endyear_example" # str |  (optional)
    timeslices = "timeslices_example" # str |  (optional)
    regionalvariable = "regionalvariable_example" # str |  (optional)
    regionalkey = "regionalkey_example" # str |  (optional)
    classifyingvariable1 = "classifyingvariable1_example" # str |  (optional)
    classifyingkey1 = "classifyingkey1_example" # str |  (optional)
    classifyingvariable2 = "classifyingvariable2_example" # str |  (optional)
    classifyingkey2 = "classifyingkey2_example" # str |  (optional)
    classifyingvariable3 = "classifyingvariable3_example" # str |  (optional)
    classifyingkey3 = "classifyingkey3_example" # str |  (optional)
    format = "png" # str |  (optional) if omitted the server will use the default value of "png"
    stand = "01.01.1970 01:00" # str |  (optional) if omitted the server will use the default value of "01.01.1970 01:00"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.chart2timeseries(username=username, password=password, name=name, area=area, charttype=charttype, drawpoints=drawpoints, zoom=zoom, focus=focus, tops=tops, contents=contents, startyear=startyear, endyear=endyear, timeslices=timeslices, regionalvariable=regionalvariable, regionalkey=regionalkey, classifyingvariable1=classifyingvariable1, classifyingkey1=classifyingkey1, classifyingvariable2=classifyingvariable2, classifyingkey2=classifyingkey2, classifyingvariable3=classifyingvariable3, classifyingkey3=classifyingkey3, format=format, stand=stand, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->chart2timeseries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **charttype** | **str**|  | [optional] if omitted the server will use the default value of "0"
 **drawpoints** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **zoom** | **str**|  | [optional] if omitted the server will use the default value of "2"
 **focus** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **tops** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **contents** | **str**|  | [optional]
 **startyear** | **str**|  | [optional]
 **endyear** | **str**|  | [optional]
 **timeslices** | **str**|  | [optional]
 **regionalvariable** | **str**|  | [optional]
 **regionalkey** | **str**|  | [optional]
 **classifyingvariable1** | **str**|  | [optional]
 **classifyingkey1** | **str**|  | [optional]
 **classifyingvariable2** | **str**|  | [optional]
 **classifyingkey2** | **str**|  | [optional]
 **classifyingvariable3** | **str**|  | [optional]
 **classifyingkey3** | **str**|  | [optional]
 **format** | **str**|  | [optional] if omitted the server will use the default value of "png"
 **stand** | **str**|  | [optional] if omitted the server will use the default value of "01.01.1970 01:00"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cube**
> cube()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    values = "true" # str |  (optional) if omitted the server will use the default value of "true"
    metadata = "false" # str |  (optional) if omitted the server will use the default value of "false"
    additionals = "false" # str |  (optional) if omitted the server will use the default value of "false"
    contents = "contents_example" # str |  (optional)
    startyear = "startyear_example" # str |  (optional)
    endyear = "endyear_example" # str |  (optional)
    timeslices = "timeslices_example" # str |  (optional)
    regionalvariable = "regionalvariable_example" # str |  (optional)
    regionalkey = "regionalkey_example" # str |  (optional)
    classifyingvariable1 = "classifyingvariable1_example" # str |  (optional)
    classifyingkey1 = "classifyingkey1_example" # str |  (optional)
    classifyingvariable2 = "classifyingvariable2_example" # str |  (optional)
    classifyingkey2 = "classifyingkey2_example" # str |  (optional)
    classifyingvariable3 = "classifyingvariable3_example" # str |  (optional)
    classifyingkey3 = "classifyingkey3_example" # str |  (optional)
    format = "csv" # str |  (optional) if omitted the server will use the default value of "csv"
    stand = "01.01.1970 01:00" # str |  (optional) if omitted the server will use the default value of "01.01.1970 01:00"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.cube(username=username, password=password, name=name, area=area, values=values, metadata=metadata, additionals=additionals, contents=contents, startyear=startyear, endyear=endyear, timeslices=timeslices, regionalvariable=regionalvariable, regionalkey=regionalkey, classifyingvariable1=classifyingvariable1, classifyingkey1=classifyingkey1, classifyingvariable2=classifyingvariable2, classifyingkey2=classifyingkey2, classifyingvariable3=classifyingvariable3, classifyingkey3=classifyingkey3, format=format, stand=stand, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->cube: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **values** | **str**|  | [optional] if omitted the server will use the default value of "true"
 **metadata** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **additionals** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **contents** | **str**|  | [optional]
 **startyear** | **str**|  | [optional]
 **endyear** | **str**|  | [optional]
 **timeslices** | **str**|  | [optional]
 **regionalvariable** | **str**|  | [optional]
 **regionalkey** | **str**|  | [optional]
 **classifyingvariable1** | **str**|  | [optional]
 **classifyingkey1** | **str**|  | [optional]
 **classifyingvariable2** | **str**|  | [optional]
 **classifyingkey2** | **str**|  | [optional]
 **classifyingvariable3** | **str**|  | [optional]
 **classifyingkey3** | **str**|  | [optional]
 **format** | **str**|  | [optional] if omitted the server will use the default value of "csv"
 **stand** | **str**|  | [optional] if omitted the server will use the default value of "01.01.1970 01:00"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cube_meta**
> cube_meta()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.cube_meta(username=username, password=password, name=name, area=area, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->cube_meta: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cubefile**
> cubefile()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    values = "true" # str |  (optional) if omitted the server will use the default value of "true"
    metadata = "false" # str |  (optional) if omitted the server will use the default value of "false"
    additionals = "false" # str |  (optional) if omitted the server will use the default value of "false"
    contents = "contents_example" # str |  (optional)
    startyear = "startyear_example" # str |  (optional)
    endyear = "endyear_example" # str |  (optional)
    timeslices = "timeslices_example" # str |  (optional)
    regionalvariable = "regionalvariable_example" # str |  (optional)
    regionalkey = "regionalkey_example" # str |  (optional)
    classifyingvariable1 = "classifyingvariable1_example" # str |  (optional)
    classifyingkey1 = "classifyingkey1_example" # str |  (optional)
    classifyingvariable2 = "classifyingvariable2_example" # str |  (optional)
    classifyingkey2 = "classifyingkey2_example" # str |  (optional)
    classifyingvariable3 = "classifyingvariable3_example" # str |  (optional)
    classifyingkey3 = "classifyingkey3_example" # str |  (optional)
    format = "csv" # str |  (optional) if omitted the server will use the default value of "csv"
    stand = "01.01.1970 01:00" # str |  (optional) if omitted the server will use the default value of "01.01.1970 01:00"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.cubefile(username=username, password=password, name=name, area=area, values=values, metadata=metadata, additionals=additionals, contents=contents, startyear=startyear, endyear=endyear, timeslices=timeslices, regionalvariable=regionalvariable, regionalkey=regionalkey, classifyingvariable1=classifyingvariable1, classifyingkey1=classifyingkey1, classifyingvariable2=classifyingvariable2, classifyingkey2=classifyingkey2, classifyingvariable3=classifyingvariable3, classifyingkey3=classifyingkey3, format=format, stand=stand, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->cubefile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **values** | **str**|  | [optional] if omitted the server will use the default value of "true"
 **metadata** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **additionals** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **contents** | **str**|  | [optional]
 **startyear** | **str**|  | [optional]
 **endyear** | **str**|  | [optional]
 **timeslices** | **str**|  | [optional]
 **regionalvariable** | **str**|  | [optional]
 **regionalkey** | **str**|  | [optional]
 **classifyingvariable1** | **str**|  | [optional]
 **classifyingkey1** | **str**|  | [optional]
 **classifyingvariable2** | **str**|  | [optional]
 **classifyingkey2** | **str**|  | [optional]
 **classifyingvariable3** | **str**|  | [optional]
 **classifyingkey3** | **str**|  | [optional]
 **format** | **str**|  | [optional] if omitted the server will use the default value of "csv"
 **stand** | **str**|  | [optional] if omitted the server will use the default value of "01.01.1970 01:00"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cubes**
> cubes()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    selection = "selection_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.cubes(username=username, password=password, selection=selection, area=area, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->cubes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **selection** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cubes2statistic**
> cubes2statistic()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    selection = "selection_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.cubes2statistic(username=username, password=password, name=name, selection=selection, area=area, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->cubes2statistic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **selection** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cubes2variable**
> cubes2variable()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    selection = "selection_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.cubes2variable(username=username, password=password, name=name, selection=selection, area=area, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->cubes2variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **selection** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find**
> find()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    term = "term_example" # str |  (optional)
    category = "all" # str |  (optional) if omitted the server will use the default value of "all"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.find(username=username, password=password, term=term, category=category, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->find: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **term** | **str**|  | [optional]
 **category** | **str**|  | [optional] if omitted the server will use the default value of "all"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs**
> jobs()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    selection = "selection_example" # str |  (optional)
    searchcriterion = "Code" # str |  (optional) if omitted the server will use the default value of "Code"
    sortcriterion = "Name" # str |  (optional) if omitted the server will use the default value of "Name"
    type = "Alle" # str |  (optional) if omitted the server will use the default value of "Alle"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.jobs(username=username, password=password, selection=selection, searchcriterion=searchcriterion, sortcriterion=sortcriterion, type=type, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->jobs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **selection** | **str**|  | [optional]
 **searchcriterion** | **str**|  | [optional] if omitted the server will use the default value of "Code"
 **sortcriterion** | **str**|  | [optional] if omitted the server will use the default value of "Name"
 **type** | **str**|  | [optional] if omitted the server will use the default value of "Alle"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logincheck**
> logincheck()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "username_example" # str |  (optional)
    password = "password_example" # str |  (optional)
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.logincheck(username=username, password=password, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->logincheck: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional]
 **password** | **str**|  | [optional]
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map2result**
> map2result()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    maptype = "0" # str |  (optional) if omitted the server will use the default value of "0"
    classes = "5" # str |  (optional) if omitted the server will use the default value of "5"
    classification = "0" # str |  (optional) if omitted the server will use the default value of "0"
    zoom = "2" # str |  (optional) if omitted the server will use the default value of "2"
    format = "png" # str |  (optional) if omitted the server will use the default value of "png"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.map2result(username=username, password=password, name=name, area=area, maptype=maptype, classes=classes, classification=classification, zoom=zoom, format=format, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->map2result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **maptype** | **str**|  | [optional] if omitted the server will use the default value of "0"
 **classes** | **str**|  | [optional] if omitted the server will use the default value of "5"
 **classification** | **str**|  | [optional] if omitted the server will use the default value of "0"
 **zoom** | **str**|  | [optional] if omitted the server will use the default value of "2"
 **format** | **str**|  | [optional] if omitted the server will use the default value of "png"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map2table**
> map2table()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    maptype = "0" # str |  (optional) if omitted the server will use the default value of "0"
    classes = "5" # str |  (optional) if omitted the server will use the default value of "5"
    classification = "0" # str |  (optional) if omitted the server will use the default value of "0"
    zoom = "2" # str |  (optional) if omitted the server will use the default value of "2"
    startyear = "startyear_example" # str |  (optional)
    endyear = "endyear_example" # str |  (optional)
    timeslices = "timeslices_example" # str |  (optional)
    regionalvariable = "regionalvariable_example" # str |  (optional)
    regionalkey = "regionalkey_example" # str |  (optional)
    classifyingvariable1 = "classifyingvariable1_example" # str |  (optional)
    classifyingkey1 = "classifyingkey1_example" # str |  (optional)
    classifyingvariable2 = "classifyingvariable2_example" # str |  (optional)
    classifyingkey2 = "classifyingkey2_example" # str |  (optional)
    classifyingvariable3 = "classifyingvariable3_example" # str |  (optional)
    classifyingkey3 = "classifyingkey3_example" # str |  (optional)
    format = "png" # str |  (optional) if omitted the server will use the default value of "png"
    stand = "01.01.1970 01:00" # str |  (optional) if omitted the server will use the default value of "01.01.1970 01:00"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.map2table(username=username, password=password, name=name, area=area, maptype=maptype, classes=classes, classification=classification, zoom=zoom, startyear=startyear, endyear=endyear, timeslices=timeslices, regionalvariable=regionalvariable, regionalkey=regionalkey, classifyingvariable1=classifyingvariable1, classifyingkey1=classifyingkey1, classifyingvariable2=classifyingvariable2, classifyingkey2=classifyingkey2, classifyingvariable3=classifyingvariable3, classifyingkey3=classifyingkey3, format=format, stand=stand, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->map2table: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **maptype** | **str**|  | [optional] if omitted the server will use the default value of "0"
 **classes** | **str**|  | [optional] if omitted the server will use the default value of "5"
 **classification** | **str**|  | [optional] if omitted the server will use the default value of "0"
 **zoom** | **str**|  | [optional] if omitted the server will use the default value of "2"
 **startyear** | **str**|  | [optional]
 **endyear** | **str**|  | [optional]
 **timeslices** | **str**|  | [optional]
 **regionalvariable** | **str**|  | [optional]
 **regionalkey** | **str**|  | [optional]
 **classifyingvariable1** | **str**|  | [optional]
 **classifyingkey1** | **str**|  | [optional]
 **classifyingvariable2** | **str**|  | [optional]
 **classifyingkey2** | **str**|  | [optional]
 **classifyingvariable3** | **str**|  | [optional]
 **classifyingkey3** | **str**|  | [optional]
 **format** | **str**|  | [optional] if omitted the server will use the default value of "png"
 **stand** | **str**|  | [optional] if omitted the server will use the default value of "01.01.1970 01:00"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map2timeseries**
> map2timeseries()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    maptype = "0" # str |  (optional) if omitted the server will use the default value of "0"
    classes = "5" # str |  (optional) if omitted the server will use the default value of "5"
    classification = "0" # str |  (optional) if omitted the server will use the default value of "0"
    zoom = "2" # str |  (optional) if omitted the server will use the default value of "2"
    contents = "contents_example" # str |  (optional)
    startyear = "startyear_example" # str |  (optional)
    endyear = "endyear_example" # str |  (optional)
    timeslices = "timeslices_example" # str |  (optional)
    regionalvariable = "regionalvariable_example" # str |  (optional)
    regionalkey = "regionalkey_example" # str |  (optional)
    classifyingvariable1 = "classifyingvariable1_example" # str |  (optional)
    classifyingkey1 = "classifyingkey1_example" # str |  (optional)
    classifyingvariable2 = "classifyingvariable2_example" # str |  (optional)
    classifyingkey2 = "classifyingkey2_example" # str |  (optional)
    classifyingvariable3 = "classifyingvariable3_example" # str |  (optional)
    classifyingkey3 = "classifyingkey3_example" # str |  (optional)
    format = "png" # str |  (optional) if omitted the server will use the default value of "png"
    stand = "01.01.1970 01:00" # str |  (optional) if omitted the server will use the default value of "01.01.1970 01:00"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.map2timeseries(username=username, password=password, name=name, area=area, maptype=maptype, classes=classes, classification=classification, zoom=zoom, contents=contents, startyear=startyear, endyear=endyear, timeslices=timeslices, regionalvariable=regionalvariable, regionalkey=regionalkey, classifyingvariable1=classifyingvariable1, classifyingkey1=classifyingkey1, classifyingvariable2=classifyingvariable2, classifyingkey2=classifyingkey2, classifyingvariable3=classifyingvariable3, classifyingkey3=classifyingkey3, format=format, stand=stand, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->map2timeseries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **maptype** | **str**|  | [optional] if omitted the server will use the default value of "0"
 **classes** | **str**|  | [optional] if omitted the server will use the default value of "5"
 **classification** | **str**|  | [optional] if omitted the server will use the default value of "0"
 **zoom** | **str**|  | [optional] if omitted the server will use the default value of "2"
 **contents** | **str**|  | [optional]
 **startyear** | **str**|  | [optional]
 **endyear** | **str**|  | [optional]
 **timeslices** | **str**|  | [optional]
 **regionalvariable** | **str**|  | [optional]
 **regionalkey** | **str**|  | [optional]
 **classifyingvariable1** | **str**|  | [optional]
 **classifyingkey1** | **str**|  | [optional]
 **classifyingvariable2** | **str**|  | [optional]
 **classifyingkey2** | **str**|  | [optional]
 **classifyingvariable3** | **str**|  | [optional]
 **classifyingkey3** | **str**|  | [optional]
 **format** | **str**|  | [optional] if omitted the server will use the default value of "png"
 **stand** | **str**|  | [optional] if omitted the server will use the default value of "01.01.1970 01:00"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modifieddata**
> modifieddata()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    selection = "selection_example" # str |  (optional)
    type = "Alle" # str |  (optional) if omitted the server will use the default value of "Alle"
    date = "01.01.1970 01:00" # str |  (optional) if omitted the server will use the default value of "01.01.1970 01:00"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.modifieddata(username=username, password=password, selection=selection, type=type, date=date, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->modifieddata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **selection** | **str**|  | [optional]
 **type** | **str**|  | [optional] if omitted the server will use the default value of "Alle"
 **date** | **str**|  | [optional] if omitted the server will use the default value of "01.01.1970 01:00"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password**
> password()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "username_example" # str |  (optional)
    password = "password_example" # str |  (optional)
    new = "new_example" # str |  (optional)
    repeat = "repeat_example" # str |  (optional)
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.password(username=username, password=password, new=new, repeat=repeat, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional]
 **password** | **str**|  | [optional]
 **new** | **str**|  | [optional]
 **repeat** | **str**|  | [optional]
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **qualitysigns**
> qualitysigns()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.qualitysigns(language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->qualitysigns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_result**
> remove_result()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.remove_result(username=username, password=password, name=name, area=area, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->remove_result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **result**
> result()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    compress = "false" # str |  (optional) if omitted the server will use the default value of "false"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.result(username=username, password=password, name=name, area=area, compress=compress, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **compress** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resultfile**
> resultfile()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    compress = "false" # str |  (optional) if omitted the server will use the default value of "false"
    format = "csv" # str |  (optional) if omitted the server will use the default value of "csv"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.resultfile(username=username, password=password, name=name, area=area, compress=compress, format=format, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->resultfile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **compress** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **format** | **str**|  | [optional] if omitted the server will use the default value of "csv"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **results**
> results()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    selection = "selection_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.results(username=username, password=password, selection=selection, area=area, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->results: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **selection** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistic**
> statistic()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.statistic(username=username, password=password, name=name, area=area, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->statistic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics**
> statistics()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    selection = "selection_example" # str |  (optional)
    searchcriterion = "Code" # str |  (optional) if omitted the server will use the default value of "Code"
    sortcriterion = "Name" # str |  (optional) if omitted the server will use the default value of "Name"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.statistics(username=username, password=password, selection=selection, searchcriterion=searchcriterion, sortcriterion=sortcriterion, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **selection** | **str**|  | [optional]
 **searchcriterion** | **str**|  | [optional] if omitted the server will use the default value of "Code"
 **sortcriterion** | **str**|  | [optional] if omitted the server will use the default value of "Name"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics2variable**
> statistics2variable()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    selection = "selection_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    searchcriterion = "Code" # str |  (optional) if omitted the server will use the default value of "Code"
    sortcriterion = "Name" # str |  (optional) if omitted the server will use the default value of "Name"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.statistics2variable(username=username, password=password, name=name, selection=selection, area=area, searchcriterion=searchcriterion, sortcriterion=sortcriterion, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->statistics2variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **selection** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **searchcriterion** | **str**|  | [optional] if omitted the server will use the default value of "Code"
 **sortcriterion** | **str**|  | [optional] if omitted the server will use the default value of "Name"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table**
> table()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    compress = "false" # str |  (optional) if omitted the server will use the default value of "false"
    transpose = "false" # str |  (optional) if omitted the server will use the default value of "false"
    startyear = "startyear_example" # str |  (optional)
    endyear = "endyear_example" # str |  (optional)
    timeslices = "timeslices_example" # str |  (optional)
    regionalvariable = "regionalvariable_example" # str |  (optional)
    regionalkey = "regionalkey_example" # str |  (optional)
    classifyingvariable1 = "classifyingvariable1_example" # str |  (optional)
    classifyingkey1 = "classifyingkey1_example" # str |  (optional)
    classifyingvariable2 = "classifyingvariable2_example" # str |  (optional)
    classifyingkey2 = "classifyingkey2_example" # str |  (optional)
    classifyingvariable3 = "classifyingvariable3_example" # str |  (optional)
    classifyingkey3 = "classifyingkey3_example" # str |  (optional)
    job = "false" # str |  (optional) if omitted the server will use the default value of "false"
    stand = "01.01.1970 01:00" # str |  (optional) if omitted the server will use the default value of "01.01.1970 01:00"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.table(username=username, password=password, name=name, area=area, compress=compress, transpose=transpose, startyear=startyear, endyear=endyear, timeslices=timeslices, regionalvariable=regionalvariable, regionalkey=regionalkey, classifyingvariable1=classifyingvariable1, classifyingkey1=classifyingkey1, classifyingvariable2=classifyingvariable2, classifyingkey2=classifyingkey2, classifyingvariable3=classifyingvariable3, classifyingkey3=classifyingkey3, job=job, stand=stand, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->table: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **compress** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **transpose** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **startyear** | **str**|  | [optional]
 **endyear** | **str**|  | [optional]
 **timeslices** | **str**|  | [optional]
 **regionalvariable** | **str**|  | [optional]
 **regionalkey** | **str**|  | [optional]
 **classifyingvariable1** | **str**|  | [optional]
 **classifyingkey1** | **str**|  | [optional]
 **classifyingvariable2** | **str**|  | [optional]
 **classifyingkey2** | **str**|  | [optional]
 **classifyingvariable3** | **str**|  | [optional]
 **classifyingkey3** | **str**|  | [optional]
 **job** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **stand** | **str**|  | [optional] if omitted the server will use the default value of "01.01.1970 01:00"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **table_meta**
> table_meta()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.table_meta(username=username, password=password, name=name, area=area, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->table_meta: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tablefile**
> tablefile()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    compress = "false" # str |  (optional) if omitted the server will use the default value of "false"
    transpose = "false" # str |  (optional) if omitted the server will use the default value of "false"
    startyear = "startyear_example" # str |  (optional)
    endyear = "endyear_example" # str |  (optional)
    timeslices = "timeslices_example" # str |  (optional)
    regionalvariable = "regionalvariable_example" # str |  (optional)
    regionalkey = "regionalkey_example" # str |  (optional)
    classifyingvariable1 = "classifyingvariable1_example" # str |  (optional)
    classifyingkey1 = "classifyingkey1_example" # str |  (optional)
    classifyingvariable2 = "classifyingvariable2_example" # str |  (optional)
    classifyingkey2 = "classifyingkey2_example" # str |  (optional)
    classifyingvariable3 = "classifyingvariable3_example" # str |  (optional)
    classifyingkey3 = "classifyingkey3_example" # str |  (optional)
    format = "csv" # str |  (optional) if omitted the server will use the default value of "csv"
    job = "false" # str |  (optional) if omitted the server will use the default value of "false"
    stand = "01.01.1970 01:00" # str |  (optional) if omitted the server will use the default value of "01.01.1970 01:00"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.tablefile(username=username, password=password, name=name, area=area, compress=compress, transpose=transpose, startyear=startyear, endyear=endyear, timeslices=timeslices, regionalvariable=regionalvariable, regionalkey=regionalkey, classifyingvariable1=classifyingvariable1, classifyingkey1=classifyingkey1, classifyingvariable2=classifyingvariable2, classifyingkey2=classifyingkey2, classifyingvariable3=classifyingvariable3, classifyingkey3=classifyingkey3, format=format, job=job, stand=stand, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->tablefile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **compress** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **transpose** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **startyear** | **str**|  | [optional]
 **endyear** | **str**|  | [optional]
 **timeslices** | **str**|  | [optional]
 **regionalvariable** | **str**|  | [optional]
 **regionalkey** | **str**|  | [optional]
 **classifyingvariable1** | **str**|  | [optional]
 **classifyingkey1** | **str**|  | [optional]
 **classifyingvariable2** | **str**|  | [optional]
 **classifyingkey2** | **str**|  | [optional]
 **classifyingvariable3** | **str**|  | [optional]
 **classifyingkey3** | **str**|  | [optional]
 **format** | **str**|  | [optional] if omitted the server will use the default value of "csv"
 **job** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **stand** | **str**|  | [optional] if omitted the server will use the default value of "01.01.1970 01:00"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tables**
> tables()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    selection = "selection_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    searchcriterion = "Code" # str |  (optional) if omitted the server will use the default value of "Code"
    sortcriterion = "Code" # str |  (optional) if omitted the server will use the default value of "Code"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.tables(username=username, password=password, selection=selection, area=area, searchcriterion=searchcriterion, sortcriterion=sortcriterion, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->tables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **selection** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **searchcriterion** | **str**|  | [optional] if omitted the server will use the default value of "Code"
 **sortcriterion** | **str**|  | [optional] if omitted the server will use the default value of "Code"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tables2statistic**
> tables2statistic()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    selection = "selection_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.tables2statistic(username=username, password=password, name=name, selection=selection, area=area, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->tables2statistic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **selection** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tables2variable**
> tables2variable()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    selection = "selection_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.tables2variable(username=username, password=password, name=name, selection=selection, area=area, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->tables2variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **selection** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms**
> terms()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    selection = "selection_example" # str |  (optional)
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.terms(username=username, password=password, selection=selection, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->terms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **selection** | **str**|  | [optional]
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeseries**
> timeseries()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    selection = "selection_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.timeseries(username=username, password=password, selection=selection, area=area, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->timeseries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **selection** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeseries2statistic**
> timeseries2statistic()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    selection = "selection_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.timeseries2statistic(username=username, password=password, name=name, selection=selection, area=area, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->timeseries2statistic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **selection** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeseries2variable**
> timeseries2variable()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    selection = "selection_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.timeseries2variable(username=username, password=password, name=name, selection=selection, area=area, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->timeseries2variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **selection** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeseries_data**
> timeseries_data()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    compress = "false" # str |  (optional) if omitted the server will use the default value of "false"
    transpose = "false" # str |  (optional) if omitted the server will use the default value of "false"
    contents = "contents_example" # str |  (optional)
    startyear = "startyear_example" # str |  (optional)
    endyear = "endyear_example" # str |  (optional)
    timeslices = "timeslices_example" # str |  (optional)
    regionalvariable = "regionalvariable_example" # str |  (optional)
    regionalkey = "regionalkey_example" # str |  (optional)
    regionalkeycode = "regionalkeycode_example" # str |  (optional)
    classifyingvariable1 = "classifyingvariable1_example" # str |  (optional)
    classifyingkey1 = "classifyingkey1_example" # str |  (optional)
    classifyingkeycode1 = "classifyingkeycode1_example" # str |  (optional)
    classifyingvariable2 = "classifyingvariable2_example" # str |  (optional)
    classifyingkey2 = "classifyingkey2_example" # str |  (optional)
    classifyingkeycode2 = "classifyingkeycode2_example" # str |  (optional)
    classifyingvariable3 = "classifyingvariable3_example" # str |  (optional)
    classifyingkey3 = "classifyingkey3_example" # str |  (optional)
    classifyingkeycode3 = "classifyingkeycode3_example" # str |  (optional)
    job = "false" # str |  (optional) if omitted the server will use the default value of "false"
    stand = "01.01.1970 01:00" # str |  (optional) if omitted the server will use the default value of "01.01.1970 01:00"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.timeseries_data(username=username, password=password, name=name, area=area, compress=compress, transpose=transpose, contents=contents, startyear=startyear, endyear=endyear, timeslices=timeslices, regionalvariable=regionalvariable, regionalkey=regionalkey, regionalkeycode=regionalkeycode, classifyingvariable1=classifyingvariable1, classifyingkey1=classifyingkey1, classifyingkeycode1=classifyingkeycode1, classifyingvariable2=classifyingvariable2, classifyingkey2=classifyingkey2, classifyingkeycode2=classifyingkeycode2, classifyingvariable3=classifyingvariable3, classifyingkey3=classifyingkey3, classifyingkeycode3=classifyingkeycode3, job=job, stand=stand, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->timeseries_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **compress** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **transpose** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **contents** | **str**|  | [optional]
 **startyear** | **str**|  | [optional]
 **endyear** | **str**|  | [optional]
 **timeslices** | **str**|  | [optional]
 **regionalvariable** | **str**|  | [optional]
 **regionalkey** | **str**|  | [optional]
 **regionalkeycode** | **str**|  | [optional]
 **classifyingvariable1** | **str**|  | [optional]
 **classifyingkey1** | **str**|  | [optional]
 **classifyingkeycode1** | **str**|  | [optional]
 **classifyingvariable2** | **str**|  | [optional]
 **classifyingkey2** | **str**|  | [optional]
 **classifyingkeycode2** | **str**|  | [optional]
 **classifyingvariable3** | **str**|  | [optional]
 **classifyingkey3** | **str**|  | [optional]
 **classifyingkeycode3** | **str**|  | [optional]
 **job** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **stand** | **str**|  | [optional] if omitted the server will use the default value of "01.01.1970 01:00"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeseries_meta**
> timeseries_meta()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.timeseries_meta(username=username, password=password, name=name, area=area, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->timeseries_meta: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeseriesfile**
> timeseriesfile()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    compress = "false" # str |  (optional) if omitted the server will use the default value of "false"
    transpose = "false" # str |  (optional) if omitted the server will use the default value of "false"
    contents = "contents_example" # str |  (optional)
    startyear = "startyear_example" # str |  (optional)
    endyear = "endyear_example" # str |  (optional)
    timeslices = "timeslices_example" # str |  (optional)
    regionalvariable = "regionalvariable_example" # str |  (optional)
    regionalkey = "regionalkey_example" # str |  (optional)
    regionalkeycode = "regionalkeycode_example" # str |  (optional)
    classifyingvariable1 = "classifyingvariable1_example" # str |  (optional)
    classifyingkey1 = "classifyingkey1_example" # str |  (optional)
    classifyingkeycode1 = "classifyingkeycode1_example" # str |  (optional)
    classifyingvariable2 = "classifyingvariable2_example" # str |  (optional)
    classifyingkey2 = "classifyingkey2_example" # str |  (optional)
    classifyingkeycode2 = "classifyingkeycode2_example" # str |  (optional)
    classifyingvariable3 = "classifyingvariable3_example" # str |  (optional)
    classifyingkey3 = "classifyingkey3_example" # str |  (optional)
    classifyingkeycode3 = "classifyingkeycode3_example" # str |  (optional)
    format = "csv" # str |  (optional) if omitted the server will use the default value of "csv"
    job = "false" # str |  (optional) if omitted the server will use the default value of "false"
    stand = "01.01.1970 01:00" # str |  (optional) if omitted the server will use the default value of "01.01.1970 01:00"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.timeseriesfile(username=username, password=password, name=name, area=area, compress=compress, transpose=transpose, contents=contents, startyear=startyear, endyear=endyear, timeslices=timeslices, regionalvariable=regionalvariable, regionalkey=regionalkey, regionalkeycode=regionalkeycode, classifyingvariable1=classifyingvariable1, classifyingkey1=classifyingkey1, classifyingkeycode1=classifyingkeycode1, classifyingvariable2=classifyingvariable2, classifyingkey2=classifyingkey2, classifyingkeycode2=classifyingkeycode2, classifyingvariable3=classifyingvariable3, classifyingkey3=classifyingkey3, classifyingkeycode3=classifyingkeycode3, format=format, job=job, stand=stand, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->timeseriesfile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **compress** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **transpose** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **contents** | **str**|  | [optional]
 **startyear** | **str**|  | [optional]
 **endyear** | **str**|  | [optional]
 **timeslices** | **str**|  | [optional]
 **regionalvariable** | **str**|  | [optional]
 **regionalkey** | **str**|  | [optional]
 **regionalkeycode** | **str**|  | [optional]
 **classifyingvariable1** | **str**|  | [optional]
 **classifyingkey1** | **str**|  | [optional]
 **classifyingkeycode1** | **str**|  | [optional]
 **classifyingvariable2** | **str**|  | [optional]
 **classifyingkey2** | **str**|  | [optional]
 **classifyingkeycode2** | **str**|  | [optional]
 **classifyingvariable3** | **str**|  | [optional]
 **classifyingkey3** | **str**|  | [optional]
 **classifyingkeycode3** | **str**|  | [optional]
 **format** | **str**|  | [optional] if omitted the server will use the default value of "csv"
 **job** | **str**|  | [optional] if omitted the server will use the default value of "false"
 **stand** | **str**|  | [optional] if omitted the server will use the default value of "01.01.1970 01:00"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **value**
> value()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.value(username=username, password=password, name=name, area=area, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->value: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **values**
> values()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    selection = "selection_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    searchcriterion = "Code" # str |  (optional) if omitted the server will use the default value of "Code"
    sortcriterion = "Name" # str |  (optional) if omitted the server will use the default value of "Name"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.values(username=username, password=password, selection=selection, area=area, searchcriterion=searchcriterion, sortcriterion=sortcriterion, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **selection** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **searchcriterion** | **str**|  | [optional] if omitted the server will use the default value of "Code"
 **sortcriterion** | **str**|  | [optional] if omitted the server will use the default value of "Name"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **values2variable**
> values2variable()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    selection = "selection_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    searchcriterion = "Code" # str |  (optional) if omitted the server will use the default value of "Code"
    sortcriterion = "Name" # str |  (optional) if omitted the server will use the default value of "Name"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.values2variable(username=username, password=password, name=name, selection=selection, area=area, searchcriterion=searchcriterion, sortcriterion=sortcriterion, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->values2variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **selection** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **searchcriterion** | **str**|  | [optional] if omitted the server will use the default value of "Code"
 **sortcriterion** | **str**|  | [optional] if omitted the server will use the default value of "Name"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variable**
> variable()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.variable(username=username, password=password, name=name, area=area, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variables**
> variables()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    selection = "selection_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    searchcriterion = "Code" # str |  (optional) if omitted the server will use the default value of "Code"
    sortcriterion = "Name" # str |  (optional) if omitted the server will use the default value of "Name"
    type = "Alle" # str |  (optional) if omitted the server will use the default value of "Alle"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.variables(username=username, password=password, selection=selection, area=area, searchcriterion=searchcriterion, sortcriterion=sortcriterion, type=type, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->variables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **selection** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **searchcriterion** | **str**|  | [optional] if omitted the server will use the default value of "Code"
 **sortcriterion** | **str**|  | [optional] if omitted the server will use the default value of "Name"
 **type** | **str**|  | [optional] if omitted the server will use the default value of "Alle"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variables2statistic**
> variables2statistic()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    username = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    password = "GAST" # str |  (optional) if omitted the server will use the default value of "GAST"
    name = "name_example" # str |  (optional)
    selection = "selection_example" # str |  (optional)
    area = "free" # str |  (optional) if omitted the server will use the default value of "free"
    searchcriterion = "Code" # str |  (optional) if omitted the server will use the default value of "Code"
    sortcriterion = "Name" # str |  (optional) if omitted the server will use the default value of "Name"
    type = "Alle" # str |  (optional) if omitted the server will use the default value of "Alle"
    pagelength = "100" # str |  (optional) if omitted the server will use the default value of "100"
    language = "de" # str |  (optional) if omitted the server will use the default value of "de"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.variables2statistic(username=username, password=password, name=name, selection=selection, area=area, searchcriterion=searchcriterion, sortcriterion=sortcriterion, type=type, pagelength=pagelength, language=language)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->variables2statistic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **password** | **str**|  | [optional] if omitted the server will use the default value of "GAST"
 **name** | **str**|  | [optional]
 **selection** | **str**|  | [optional]
 **area** | **str**|  | [optional] if omitted the server will use the default value of "free"
 **searchcriterion** | **str**|  | [optional] if omitted the server will use the default value of "Code"
 **sortcriterion** | **str**|  | [optional] if omitted the server will use the default value of "Name"
 **type** | **str**|  | [optional] if omitted the server will use the default value of "Alle"
 **pagelength** | **str**|  | [optional] if omitted the server will use the default value of "100"
 **language** | **str**|  | [optional] if omitted the server will use the default value of "de"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **whoami**
> whoami()



### Example


```python
import time
from deutschland import destatis
from deutschland.destatis.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www-genesis.destatis.de/genesisWS/rest/2020
# See configuration.py for a list of all supported configuration parameters.
configuration = destatis.Configuration(
    host = "https://www-genesis.destatis.de/genesisWS/rest/2020"
)


# Enter a context with an instance of the API client
with destatis.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_agent = "user-agent_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.whoami(user_agent=user_agent)
    except destatis.ApiException as e:
        print("Exception when calling DefaultApi->whoami: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_agent** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

