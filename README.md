# aerpawgw-client
This is Aerpaw gateway service to interact with Emulab

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import aerpawgw_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import aerpawgw_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import aerpawgw_client
from aerpawgw_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aerpawgw_client.ExperimentApi(aerpawgw_client.ApiClient(configuration))
body = aerpawgw_client.Experiment() # Experiment | Experiment Object

try:
    # create a experiment
    api_response = api_instance.create_experiment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->create_experiment: %s\n" % e)

# create an instance of the API class
api_instance = aerpawgw_client.ExperimentApi(aerpawgw_client.ApiClient(configuration))
experiment = 'experiment_example' # str | experiment to delete
username = 'username_example' # str | username for the request (optional)
project = 'project_example' # str | project name (optional)

try:
    # delete experiment
    api_instance.delete_experiment(experiment, username=username, project=project)
except ApiException as e:
    print("Exception when calling ExperimentApi->delete_experiment: %s\n" % e)

# create an instance of the API class
api_instance = aerpawgw_client.ExperimentApi(aerpawgw_client.ApiClient(configuration))
username = 'username_example' # str | username for the request (optional)

try:
    # get experiment(s) under user
    api_response = api_instance.get_experiments(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->get_experiments: %s\n" % e)

# create an instance of the API class
api_instance = aerpawgw_client.ExperimentApi(aerpawgw_client.ApiClient(configuration))
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

## Documentation for API Endpoints

All URIs are relative to *http://0.0.0.0:8080/aerpawgateway/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ExperimentApi* | [**create_experiment**](docs/ExperimentApi.md#create_experiment) | **POST** /experiment | create a experiment
*ExperimentApi* | [**delete_experiment**](docs/ExperimentApi.md#delete_experiment) | **DELETE** /experiment | delete experiment
*ExperimentApi* | [**get_experiments**](docs/ExperimentApi.md#get_experiments) | **GET** /experiments | get experiment(s) under user
*ExperimentApi* | [**query_experiment**](docs/ExperimentApi.md#query_experiment) | **GET** /experiment/{experiment} | get status of specific experiment
*ProfileApi* | [**create_profile**](docs/ProfileApi.md#create_profile) | **POST** /profile | create profile
*ProfileApi* | [**delete_profile**](docs/ProfileApi.md#delete_profile) | **DELETE** /profile | delete profile
*ProfileApi* | [**get_profiles**](docs/ProfileApi.md#get_profiles) | **GET** /profiles | get profiles under user
*ProfileApi* | [**query_profile**](docs/ProfileApi.md#query_profile) | **GET** /profile | query specific profile
*ReservationApi* | [**create_reservation**](docs/ReservationApi.md#create_reservation) | **POST** /reservation | create reservation
*ReservationApi* | [**delete_reservation**](docs/ReservationApi.md#delete_reservation) | **DELETE** /reservation | delete reservation
*ReservationApi* | [**get_reservation**](docs/ReservationApi.md#get_reservation) | **GET** /reservation | get reservation under user
*ResourcesApi* | [**list_resources**](docs/ResourcesApi.md#list_resources) | **GET** /resources | list resources
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /user | create user on emulab testbed
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /user | delete user
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /user | get user information
*VersionApi* | [**get_version**](docs/VersionApi.md#get_version) | **GET** /version | API version

## Documentation For Models

 - [ApiResponse](docs/ApiResponse.md)
 - [Experiment](docs/Experiment.md)
 - [Node](docs/Node.md)
 - [Profile](docs/Profile.md)
 - [Reservation](docs/Reservation.md)
 - [Resource](docs/Resource.md)
 - [User](docs/User.md)
 - [Vnode](docs/Vnode.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

ericafu@renci.org