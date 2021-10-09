# ladestationen.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_get**](DefaultApi.md#query_get) | **GET** /query | Query für alle Ladesäulen


# **query_get**
> StationOverview query_get(geometry, )

Query für alle Ladesäulen

### Example


```python
import time
from deutschland import ladestationen
from deutschland.ladestationen.api import default_api
from deutschland.ladestationen.model.station_overview import StationOverview
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ladestationen.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ladestationen.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    geometry = "geometry_example" # str | Geometry filter. URL-enkodiertes JSON Objekt vom Typ `Geometry`
    geometry_type = "" # str | Art der Geometry (optional) if omitted the server will use the default value of ""
    f = "json" # str | Ausgabeformat der Daten. Default ist 'html'. (optional)
    object_ids = "42,123,666" # str | Komma-separierte Liste von IDs (integer), filtert nach den einzelnen Objekten (optional)
    order_by_fields = "orderByFields_example" # str |  (optional)
    return_geometry = True # bool |  (optional)
    spatial_rel = "esriSpatialRelIntersects" # str | Spatial Relationships (optional)
    in_sr = 1 # int | Input Spatial Reference (optional)
    out_sr = 1 # int | Output Spatial Reference (optional)
    max_record_count_factor = 1 # int |  (optional)
    result_type = "none" # str |  (optional)
    quantization_parameters = "quantizationParameters_example" # str | URL-enkodiertes JSON Objekt vom Typ `QuantizationParameter` (optional)
    where = "where_example" # str | SQL \"where\" Filter (optional)
    having = "having_example" # str |  (optional)
    time = 1 # int |  (optional)
    distance = "0.0" # str |  (optional)
    units = "esriSRUnit_Meter" # str |  (optional)
    geometry_precision = "geometryPrecision_example" # str |  (optional)
    feature_encoding = "esriDefault" # str |  (optional)
    group_by_fields_for_statistics = "groupByFieldsForStatistics_example" # str |  (optional)
    cache_hint = True # bool |  (optional)
    return_extent_only = True # bool |  (optional)
    return_z = True # bool |  (optional)
    return_ids_only = True # bool |  (optional)
    return_centroid = True # bool |  (optional)
    return_exceeded_limit_features = True # bool |  (optional)
    datum_transformation = "datumTransformation_example" # str |  (optional)
    result_offset = "resultOffset_example" # str |  (optional)
    apply_vcs_projection = True # bool |  (optional)
    out_statistics = "outStatistics_example" # str |  (optional)
    return_distinct_values = True # bool |  (optional)
    multipatch_option = "none" # str |  (optional)
    return_m = True # bool |  (optional)
    max_allowable_offset = 1 # int |  (optional)
    return_count_only = True # bool |  (optional)
    return_unique_ids_only = True # bool |  (optional)
    return_query_geometry = True # bool |  (optional)
    result_record_count = 1 # int |  (optional)
    sql_format = "none" # str |  (optional)
    token = "token_example" # str |  (optional)
    return_geodetic = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Query für alle Ladesäulen
        api_response = api_instance.query_get(geometry, )
        pprint(api_response)
    except ladestationen.ApiException as e:
        print("Exception when calling DefaultApi->query_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Query für alle Ladesäulen
        api_response = api_instance.query_get(geometry, geometry_type=geometry_type, f=f, object_ids=object_ids, order_by_fields=order_by_fields, return_geometry=return_geometry, spatial_rel=spatial_rel, in_sr=in_sr, out_sr=out_sr, max_record_count_factor=max_record_count_factor, result_type=result_type, quantization_parameters=quantization_parameters, where=where, having=having, time=time, distance=distance, units=units, geometry_precision=geometry_precision, feature_encoding=feature_encoding, group_by_fields_for_statistics=group_by_fields_for_statistics, cache_hint=cache_hint, return_extent_only=return_extent_only, return_z=return_z, return_ids_only=return_ids_only, return_centroid=return_centroid, return_exceeded_limit_features=return_exceeded_limit_features, datum_transformation=datum_transformation, result_offset=result_offset, apply_vcs_projection=apply_vcs_projection, out_statistics=out_statistics, return_distinct_values=return_distinct_values, multipatch_option=multipatch_option, return_m=return_m, max_allowable_offset=max_allowable_offset, return_count_only=return_count_only, return_unique_ids_only=return_unique_ids_only, return_query_geometry=return_query_geometry, result_record_count=result_record_count, sql_format=sql_format, token=token, return_geodetic=return_geodetic)
        pprint(api_response)
    except ladestationen.ApiException as e:
        print("Exception when calling DefaultApi->query_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geometry** | **str**| Geometry filter. URL-enkodiertes JSON Objekt vom Typ &#x60;Geometry&#x60; |
 **out_fields** | **str**| Auswahl der Felder, die ausgegeben werden sollen, durch Komma getrennt | defaults to "*"
 **geometry_type** | **str**| Art der Geometry | [optional] if omitted the server will use the default value of ""
 **f** | **str**| Ausgabeformat der Daten. Default ist &#39;html&#39;. | [optional]
 **object_ids** | **str**| Komma-separierte Liste von IDs (integer), filtert nach den einzelnen Objekten | [optional]
 **order_by_fields** | **str**|  | [optional]
 **return_geometry** | **bool**|  | [optional]
 **spatial_rel** | **str**| Spatial Relationships | [optional]
 **in_sr** | **int**| Input Spatial Reference | [optional]
 **out_sr** | **int**| Output Spatial Reference | [optional]
 **max_record_count_factor** | **int**|  | [optional]
 **result_type** | **str**|  | [optional]
 **quantization_parameters** | **str**| URL-enkodiertes JSON Objekt vom Typ &#x60;QuantizationParameter&#x60; | [optional]
 **where** | **str**| SQL \&quot;where\&quot; Filter | [optional]
 **having** | **str**|  | [optional]
 **time** | **int**|  | [optional]
 **distance** | **str**|  | [optional]
 **units** | **str**|  | [optional]
 **geometry_precision** | **str**|  | [optional]
 **feature_encoding** | **str**|  | [optional]
 **group_by_fields_for_statistics** | **str**|  | [optional]
 **cache_hint** | **bool**|  | [optional]
 **return_extent_only** | **bool**|  | [optional]
 **return_z** | **bool**|  | [optional]
 **return_ids_only** | **bool**|  | [optional]
 **return_centroid** | **bool**|  | [optional]
 **return_exceeded_limit_features** | **bool**|  | [optional]
 **datum_transformation** | **str**|  | [optional]
 **result_offset** | **str**|  | [optional]
 **apply_vcs_projection** | **bool**|  | [optional]
 **out_statistics** | **str**|  | [optional]
 **return_distinct_values** | **bool**|  | [optional]
 **multipatch_option** | **str**|  | [optional]
 **return_m** | **bool**|  | [optional]
 **max_allowable_offset** | **int**|  | [optional]
 **return_count_only** | **bool**|  | [optional]
 **return_unique_ids_only** | **bool**|  | [optional]
 **return_query_geometry** | **bool**|  | [optional]
 **result_record_count** | **int**|  | [optional]
 **sql_format** | **str**|  | [optional]
 **token** | **str**|  | [optional]
 **return_geodetic** | **bool**|  | [optional]

### Return type

[**StationOverview**](StationOverview.md)

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

