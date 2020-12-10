# aerpawgw_client.UserApi

All URIs are relative to *http://0.0.0.0:8080/aerpawgateway/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UserApi.md#create_user) | **POST** /user | create user on emulab testbed
[**delete_user**](UserApi.md#delete_user) | **DELETE** /user | delete user
[**get_user**](UserApi.md#get_user) | **GET** /user | get user information

# **create_user**
> list[ApiResponse] create_user(body, username)

create user on emulab testbed

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.UserApi()
body = aerpawgw_client.User() # User | User Object
username = 'username_example' # str | username for the request

try:
    # create user on emulab testbed
    api_response = api_instance.create_user(body, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)| User Object | 
 **username** | **str**| username for the request | 

### Return type

[**list[ApiResponse]**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(username)

delete user

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.UserApi()
username = 'username_example' # str | username for the request

try:
    # delete user
    api_instance.delete_user(username)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username for the request | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> list[Experiment] get_user(username)

get user information

get user information

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.UserApi()
username = 'username_example' # str | username for the request

try:
    # get user information
    api_response = api_instance.get_user(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username for the request | 

### Return type

[**list[Experiment]**](Experiment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

