# aerpawgw_client.ResourcesApi

All URIs are relative to *http://0.0.0.0:8080/aerpawgateway/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_resources**](ResourcesApi.md#list_resources) | **GET** /resources | list resources
[**parse_resources**](ResourcesApi.md#parse_resources) | **POST** /resources/parse_script | Parse resources

# **list_resources**
> Resource list_resources(username=username, project=project, experiment=experiment)

list resources

List resources

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.ResourcesApi()
username = 'username_example' # str | The username for the request (optional)
project = 'project_example' # str | Project pid (optional)
experiment = 'experiment_example' # str | if experiment id is given, manifest rspec of the experiment will be returned. (optional)

try:
    # list resources
    api_response = api_instance.list_resources(username=username, project=project, experiment=experiment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->list_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username for the request | [optional] 
 **project** | **str**| Project pid | [optional] 
 **experiment** | **str**| if experiment id is given, manifest rspec of the experiment will be returned. | [optional] 

### Return type

[**Resource**](Resource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_resources**
> Resource parse_resources(body)

Parse resources

Parse resources

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.ResourcesApi()
body = aerpawgw_client.Profile() # Profile | Profile Object

try:
    # Parse resources
    api_response = api_instance.parse_resources(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->parse_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Profile**](Profile.md)| Profile Object | 

### Return type

[**Resource**](Resource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

