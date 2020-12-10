# coding: utf-8

"""
    Aerpaw Gateway

    This is Aerpaw gateway service to interact with Emulab  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: ericafu@renci.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import aerpawgw_client
from aerpawgw_client.api.profile_api import ProfileApi  # noqa: E501
from aerpawgw_client.rest import ApiException


class TestProfileApi(unittest.TestCase):
    """ProfileApi unit test stubs"""

    def setUp(self):
        self.api = ProfileApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_profile(self):
        """Test case for create_profile

        create profile  # noqa: E501
        """
        pass

    def test_delete_profile(self):
        """Test case for delete_profile

        delete profile  # noqa: E501
        """
        pass

    def test_get_profiles(self):
        """Test case for get_profiles

        get profiles under user  # noqa: E501
        """
        pass

    def test_query_profile(self):
        """Test case for query_profile

        query specific profile  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
