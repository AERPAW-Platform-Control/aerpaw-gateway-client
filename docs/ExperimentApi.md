# aerpawgw_client.ExperimentApi

All URIs are relative to *http://0.0.0.0:8080/aerpawgateway/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_experiment**](ExperimentApi.md#create_experiment) | **POST** /experiment | create a experiment
[**delete_experiment**](ExperimentApi.md#delete_experiment) | **DELETE** /experiment | delete experiment
[**get_experiments**](ExperimentApi.md#get_experiments) | **GET** /experiments | get experiment(s) under user
[**query_experiment**](ExperimentApi.md#query_experiment) | **GET** /experiment/{experiment} | get status of specific experiment

# **create_experiment**
> ApiResponse create_experiment(body)

create a experiment

instantiate/start experiment

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.ExperimentApi()
body = aerpawgw_client.Experiment() # Experiment | Experiment Object

try:
    # create a experiment
    api_response = api_instance.create_experiment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->create_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Experiment**](Experiment.md)| Experiment Object | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_experiment**
> delete_experiment(experiment, username=username, project=project)

delete experiment

delete/terminate experiment

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.ExperimentApi()
experiment = 'experiment_example' # str | experiment to delete
username = 'username_example' # str | username for the request (optional)
project = 'project_example' # str | project name (optional)

try:
    # delete experiment
    api_instance.delete_experiment(experiment, username=username, project=project)
except ApiException as e:
    print("Exception when calling ExperimentApi->delete_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment** | **str**| experiment to delete | 
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

# **get_experiments**
> list[Experiment] get_experiments(username=username)

get experiment(s) under user

get experiment(s) under user

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.ExperimentApi()
username = 'username_example' # str | username for the request (optional)

try:
    # get experiment(s) under user
    api_response = api_instance.get_experiments(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->get_experiments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username for the request | [optional] 

### Return type

[**list[Experiment]**](Experiment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_experiment**
> Experiment query_experiment(experiment, username=username, project=project)

get status of specific experiment

get Experiment status of specific experiment

### Example
```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.ExperimentApi()
experiment = 'experiment_example' # str | experiment name to query
username = 'username_example' # str | username for the request (optional)
project = 'project_example' # str | project name (optional)

try:
    # get status of specific experiment
    api_response = api_instance.query_experiment(experiment, username=username, project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->query_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment** | **str**| experiment name to query | 
 **username** | **str**| username for the request | [optional] 
 **project** | **str**| project name | [optional] 

### Return type

[**Experiment**](Experiment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

