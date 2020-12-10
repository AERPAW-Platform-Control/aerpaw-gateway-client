# aerpawgw_client.ProfileApi

All URIs are relative to *http://0.0.0.0:8080/aerpawgateway/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_profile**](ProfileApi.md#create_profile) | **POST** /profile | create profile
[**delete_profile**](ProfileApi.md#delete_profile) | **DELETE** /profile | delete profile
[**get_profiles**](ProfileApi.md#get_profiles) | **GET** /profiles | get profiles under user
[**query_profile**](ProfileApi.md#query_profile) | **GET** /profile | query specific profile

# **create_profile**
> ApiResponse create_profile(body)

create profile

Create Profile

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.ProfileApi()
body = aerpawgw_client.Profile() # Profile | Profile Object

try:
    # create profile
    api_response = api_instance.create_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->create_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Profile**](Profile.md)| Profile Object | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_profile**
> delete_profile(name, username=username, project=project)

delete profile

delete profile

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.ProfileApi()
name = 'name_example' # str | name of profile to delete
username = 'username_example' # str | username for the request (optional)
project = 'project_example' # str | project name (optional)

try:
    # delete profile
    api_instance.delete_profile(name, username=username, project=project)
except ApiException as e:
    print("Exception when calling ProfileApi->delete_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of profile to delete | 
 **username** | **str**| username for the request | [optional] 
 **project** | **str**| project name | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profiles**
> list[Profile] get_profiles(username=username)

get profiles under user

get profiles under user

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.ProfileApi()
username = 'username_example' # str | creator of the profile (optional)

try:
    # get profiles under user
    api_response = api_instance.get_profiles(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->get_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| creator of the profile | [optional] 

### Return type

[**list[Profile]**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_profile**
> Profile query_profile(profile, username=username, project=project)

query specific profile

query specific profile

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.ProfileApi()
profile = 'profile_example' # str | profile name to query
username = 'username_example' # str | creator of the profile (optional)
project = 'project_example' # str | project name (optional)

try:
    # query specific profile
    api_response = api_instance.query_profile(profile, username=username, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->query_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | **str**| profile name to query | 
 **username** | **str**| creator of the profile | [optional] 
 **project** | **str**| project name | [optional] 

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

