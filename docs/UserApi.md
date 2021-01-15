# aerpawgw_client.UserApi

All URIs are relative to *http://0.0.0.0:8080/aerpawgateway/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adduser**](UserApi.md#adduser) | **POST** /user | add/update user and sshkey on experiment nodes

# **adduser**
> adduser(body, experiment, project=project)

add/update user and sshkey on experiment nodes

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.UserApi()
body = aerpawgw_client.Userkey() # Userkey | User Object
experiment = 'experiment_example' # str | experiment for the request
project = 'project_example' # str | project of the experiment (optional)

try:
    # add/update user and sshkey on experiment nodes
    api_instance.adduser(body, experiment, project=project)
except ApiException as e:
    print("Exception when calling UserApi->adduser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Userkey**](Userkey.md)| User Object | 
 **experiment** | **str**| experiment for the request | 
 **project** | **str**| project of the experiment | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

