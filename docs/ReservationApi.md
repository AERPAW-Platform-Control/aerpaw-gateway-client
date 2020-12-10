# aerpawgw_client.ReservationApi

All URIs are relative to *http://0.0.0.0:8080/aerpawgateway/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reservation**](ReservationApi.md#create_reservation) | **POST** /reservation | create reservation
[**delete_reservation**](ReservationApi.md#delete_reservation) | **DELETE** /reservation | delete reservation
[**get_reservation**](ReservationApi.md#get_reservation) | **GET** /reservation | get reservation under user

# **create_reservation**
> ApiResponse create_reservation(body, validate=validate)

create reservation

Create Reservation

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.ReservationApi()
body = aerpawgw_client.Reservation() # Reservation | Reservation Object
validate = true # bool | set to true if just to validate instead of actual reserve (optional)

try:
    # create reservation
    api_response = api_instance.create_reservation(body, validate=validate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReservationApi->create_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Reservation**](Reservation.md)| Reservation Object | 
 **validate** | **bool**| set to true if just to validate instead of actual reserve | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reservation**
> ApiResponse delete_reservation(reservation, username=username, cluster=cluster, project=project)

delete reservation

Delete Reservation

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.ReservationApi()
reservation = 'reservation_example' # str | reservation uuid to delete
username = 'username_example' # str | username who request to delete (optional)
cluster = 'cluster_example' # str | either cluster name or cluster_urn (optional)
project = 'project_example' # str | The project name (optional)

try:
    # delete reservation
    api_response = api_instance.delete_reservation(reservation, username=username, cluster=cluster, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReservationApi->delete_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation** | **str**| reservation uuid to delete | 
 **username** | **str**| username who request to delete | [optional] 
 **cluster** | **str**| either cluster name or cluster_urn | [optional] 
 **project** | **str**| The project name | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reservation**
> list[Reservation] get_reservation(username=username, cluster=cluster)

get reservation under user

get reservation under user

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.ReservationApi()
username = 'username_example' # str | username for the request (optional)
cluster = 'cluster_example' # str | either cluster name or cluster_urn (optional)

try:
    # get reservation under user
    api_response = api_instance.get_reservation(username=username, cluster=cluster)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReservationApi->get_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username for the request | [optional] 
 **cluster** | **str**| either cluster name or cluster_urn | [optional] 

### Return type

[**list[Reservation]**](Reservation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

