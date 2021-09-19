# jobsuche.DefaultApi

All URIs are relative to *https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ed_v1_arbeitgeberlogo_hash_id_get**](DefaultApi.md#ed_v1_arbeitgeberlogo_hash_id_get) | **GET** /ed/v1/arbeitgeberlogo/{hashID} | Unternehmen Logo
[**pc_v1_app_jobs_hash_id_bewerbung_get**](DefaultApi.md#pc_v1_app_jobs_hash_id_bewerbung_get) | **GET** /pc/v1/app/jobs/{hashID}/bewerbung | Bewerbung Kontaktdaten
[**pc_v1_jobdetails_hash_id_get**](DefaultApi.md#pc_v1_jobdetails_hash_id_get) | **GET** /pc/v1/jobdetails/{hashID} | Jobdetail
[**pc_v2_app_jobs_get**](DefaultApi.md#pc_v2_app_jobs_get) | **GET** /pc/v2/app/jobs/ | Jobsuche


# **ed_v1_arbeitgeberlogo_hash_id_get**
> file_type ed_v1_arbeitgeberlogo_hash_id_get(hash_id)

Unternehmen Logo

Abrufen des Logos eines Unternehmens

### Example

* OAuth Authentication (clientCredAuth):

```python
import time
import jobsuche
from jobsuche.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service
# See configuration.py for a list of all supported configuration parameters.
configuration = jobsuche.Configuration(
    host = "https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: clientCredAuth
configuration = jobsuche.Configuration(
    host = "https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with jobsuche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    hash_id = "VK2qoXBe0s-UAdH_qxLDRrZrY5iY8a1PJt3MjJCXsdo=" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unternehmen Logo
        api_response = api_instance.ed_v1_arbeitgeberlogo_hash_id_get(hash_id)
        pprint(api_response)
    except jobsuche.ApiException as e:
        print("Exception when calling DefaultApi->ed_v1_arbeitgeberlogo_hash_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash_id** | **str**|  |

### Return type

**file_type**

### Authorization

[clientCredAuth](../README.md#clientCredAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pc_v1_app_jobs_hash_id_bewerbung_get**
> JobApplicationDetails pc_v1_app_jobs_hash_id_bewerbung_get(hash_id)

Bewerbung Kontaktdaten

Abrufen von Kontaktdaten zu einem Job.

### Example

* OAuth Authentication (clientCredAuth):

```python
import time
import jobsuche
from jobsuche.api import default_api
from jobsuche.model.job_application_details import JobApplicationDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service
# See configuration.py for a list of all supported configuration parameters.
configuration = jobsuche.Configuration(
    host = "https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: clientCredAuth
configuration = jobsuche.Configuration(
    host = "https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with jobsuche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    hash_id = "VK2qoXBe0s-UAdH_qxLDRrZrY5iY8a1PJt3MjJCXsdo=" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Bewerbung Kontaktdaten
        api_response = api_instance.pc_v1_app_jobs_hash_id_bewerbung_get(hash_id)
        pprint(api_response)
    except jobsuche.ApiException as e:
        print("Exception when calling DefaultApi->pc_v1_app_jobs_hash_id_bewerbung_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash_id** | **str**|  |

### Return type

[**JobApplicationDetails**](JobApplicationDetails.md)

### Authorization

[clientCredAuth](../README.md#clientCredAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pc_v1_jobdetails_hash_id_get**
> JobDetails pc_v1_jobdetails_hash_id_get(hash_id)

Jobdetail

Abrufen von Details zu einem Job.

### Example

* OAuth Authentication (clientCredAuth):

```python
import time
import jobsuche
from jobsuche.api import default_api
from jobsuche.model.job_details import JobDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service
# See configuration.py for a list of all supported configuration parameters.
configuration = jobsuche.Configuration(
    host = "https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: clientCredAuth
configuration = jobsuche.Configuration(
    host = "https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with jobsuche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    hash_id = "VK2qoXBe0s-UAdH_qxLDRrZrY5iY8a1PJt3MjJCXsdo=" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Jobdetail
        api_response = api_instance.pc_v1_jobdetails_hash_id_get(hash_id)
        pprint(api_response)
    except jobsuche.ApiException as e:
        print("Exception when calling DefaultApi->pc_v1_jobdetails_hash_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash_id** | **str**|  |

### Return type

[**JobDetails**](JobDetails.md)

### Authorization

[clientCredAuth](../README.md#clientCredAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pc_v2_app_jobs_get**
> JobSearchResponse pc_v2_app_jobs_get()

Jobsuche

Die Jobsuche ermöglicht verfügbare Jobangebote mit verschiedenen get Parametern zu filtern.

### Example

* OAuth Authentication (clientCredAuth):

```python
import time
import jobsuche
from jobsuche.api import default_api
from jobsuche.model.job_search_response import JobSearchResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service
# See configuration.py for a list of all supported configuration parameters.
configuration = jobsuche.Configuration(
    host = "https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: clientCredAuth
configuration = jobsuche.Configuration(
    host = "https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with jobsuche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    was = "Referatsleiter" # str | Freitext suche Jobtitel (optional)
    wo = "Berlin" # str | Freitext suche Beschäftigungsort (optional)
    page = 1 # int | Ergebnissseite (optional)
    size = 50 # int | Anzahl von Ergebnissen (optional)
    arbeitgeber = "Deutsche%20Bahn%20AG_W4qFQypjw_IWOJAkn2NMSE-Yf-mRbt_6_PvZr0FLdX4%3D" # str | Arbeitgeber der Stelle (optional)
    fct_aktualitaet = 30 # int | Anzahl der Tage, seit der Job veröffentlicht wurde. Kann zwischen 0 und 100 Tagen liegen. (optional)
    fct_arbeitsvermittlung = "MIT_AV" # str | Gibt an, ob Jobs von externen Arbeitsvermittlungen in die Suchergebnisse einbezogen werden sollen. (optional)
    fct_angebotsart = "ARBEIT" # str |  (optional)
    fct_befristung = "UNBEFRISTET" # str | Kann mehrere Werte haben z.B. FCT.BEFRISTUNG=UNBEFRISTET&FCT.BEFRISTUNG=KEINE_ANGABE. (optional)
    fct_arbeitszeitmodell = "VOLLZEIT" # str | Kann mehrere Werte haben z.B. FCT.ARBEITSZEITMODELL=HEIM_TELEARBEIT&FCT.ARBEITSZEITMODELL=MINIJOB (optional)
    fct_behinderung = "AN" # str |  (optional)
    fct_aktion = "AN" # str | Wenn AN, werden nur Jobs die im Kontext von Corona angeboten werden angezeigt. (optional) if omitted the server will use the default value of "AN"
    fct_umkreis = 25 # int | Umkreis in Kilometern von Wo-Parameter. (z.B. 25 oder 200) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Jobsuche
        api_response = api_instance.pc_v2_app_jobs_get(was=was, wo=wo, page=page, size=size, arbeitgeber=arbeitgeber, fct_aktualitaet=fct_aktualitaet, fct_arbeitsvermittlung=fct_arbeitsvermittlung, fct_angebotsart=fct_angebotsart, fct_befristung=fct_befristung, fct_arbeitszeitmodell=fct_arbeitszeitmodell, fct_behinderung=fct_behinderung, fct_aktion=fct_aktion, fct_umkreis=fct_umkreis)
        pprint(api_response)
    except jobsuche.ApiException as e:
        print("Exception when calling DefaultApi->pc_v2_app_jobs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **was** | **str**| Freitext suche Jobtitel | [optional]
 **wo** | **str**| Freitext suche Beschäftigungsort | [optional]
 **page** | **int**| Ergebnissseite | [optional]
 **size** | **int**| Anzahl von Ergebnissen | [optional]
 **arbeitgeber** | **str**| Arbeitgeber der Stelle | [optional]
 **fct_aktualitaet** | **int**| Anzahl der Tage, seit der Job veröffentlicht wurde. Kann zwischen 0 und 100 Tagen liegen. | [optional]
 **fct_arbeitsvermittlung** | **str**| Gibt an, ob Jobs von externen Arbeitsvermittlungen in die Suchergebnisse einbezogen werden sollen. | [optional]
 **fct_angebotsart** | **str**|  | [optional]
 **fct_befristung** | **str**| Kann mehrere Werte haben z.B. FCT.BEFRISTUNG&#x3D;UNBEFRISTET&amp;FCT.BEFRISTUNG&#x3D;KEINE_ANGABE. | [optional]
 **fct_arbeitszeitmodell** | **str**| Kann mehrere Werte haben z.B. FCT.ARBEITSZEITMODELL&#x3D;HEIM_TELEARBEIT&amp;FCT.ARBEITSZEITMODELL&#x3D;MINIJOB | [optional]
 **fct_behinderung** | **str**|  | [optional]
 **fct_aktion** | **str**| Wenn AN, werden nur Jobs die im Kontext von Corona angeboten werden angezeigt. | [optional] if omitted the server will use the default value of "AN"
 **fct_umkreis** | **int**| Umkreis in Kilometern von Wo-Parameter. (z.B. 25 oder 200) | [optional]

### Return type

[**JobSearchResponse**](JobSearchResponse.md)

### Authorization

[clientCredAuth](../README.md#clientCredAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

