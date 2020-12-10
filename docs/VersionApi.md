# aerpawgw_client.VersionApi

All URIs are relative to *http://0.0.0.0:8080/aerpawgateway/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_version**](VersionApi.md#get_version) | **GET** /version | API version

# **get_version**
> str get_version()

API version

The API version

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.VersionApi()

try:
    # API version
    api_response = api_instance.get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

