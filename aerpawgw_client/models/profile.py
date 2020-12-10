# coding: utf-8

"""
    Aerpaw Gateway

    This is Aerpaw gateway service to interact with Emulab  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: ericafu@renci.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Profile(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'creator': 'str',
        'name': 'str',
        'project': 'str',
        'version': 'str',
        'created': 'str',
        'script': 'str',
        'rspec': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'creator': 'creator',
        'name': 'name',
        'project': 'project',
        'version': 'version',
        'created': 'created',
        'script': 'script',
        'rspec': 'rspec',
        'uuid': 'uuid'
    }

    def __init__(self, creator=None, name=None, project=None, version=None, created=None, script=None, rspec=None, uuid=None):  # noqa: E501
        """Profile - a model defined in Swagger"""  # noqa: E501
        self._creator = None
        self._name = None
        self._project = None
        self._version = None
        self._created = None
        self._script = None
        self._rspec = None
        self._uuid = None
        self.discriminator = None
        if creator is not None:
            self.creator = creator
        self.name = name
        if project is not None:
            self.project = project
        if version is not None:
            self.version = version
        if created is not None:
            self.created = created
        self.script = script
        if rspec is not None:
            self.rspec = rspec
        if uuid is not None:
            self.uuid = uuid

    @property
    def creator(self):
        """Gets the creator of this Profile.  # noqa: E501


        :return: The creator of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Profile.


        :param creator: The creator of this Profile.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def name(self):
        """Gets the name of this Profile.  # noqa: E501


        :return: The name of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Profile.


        :param name: The name of this Profile.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def project(self):
        """Gets the project of this Profile.  # noqa: E501


        :return: The project of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Profile.


        :param project: The project of this Profile.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def version(self):
        """Gets the version of this Profile.  # noqa: E501


        :return: The version of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Profile.


        :param version: The version of this Profile.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def created(self):
        """Gets the created of this Profile.  # noqa: E501


        :return: The created of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Profile.


        :param created: The created of this Profile.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def script(self):
        """Gets the script of this Profile.  # noqa: E501


        :return: The script of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this Profile.


        :param script: The script of this Profile.  # noqa: E501
        :type: str
        """
        if script is None:
            raise ValueError("Invalid value for `script`, must not be `None`")  # noqa: E501

        self._script = script

    @property
    def rspec(self):
        """Gets the rspec of this Profile.  # noqa: E501


        :return: The rspec of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._rspec

    @rspec.setter
    def rspec(self, rspec):
        """Sets the rspec of this Profile.


        :param rspec: The rspec of this Profile.  # noqa: E501
        :type: str
        """

        self._rspec = rspec

    @property
    def uuid(self):
        """Gets the uuid of this Profile.  # noqa: E501


        :return: The uuid of this Profile.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Profile.


        :param uuid: The uuid of this Profile.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Profile, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Profile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
