# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 0.8.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetCharactersCharacterIdBookmarksFolders200Ok(object):
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
        'folder_id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'folder_id': 'folder_id',
        'name': 'name'
    }

    def __init__(self, folder_id=None, name=None):  # noqa: E501
        """GetCharactersCharacterIdBookmarksFolders200Ok - a model defined in Swagger"""  # noqa: E501

        self._folder_id = None
        self._name = None
        self.discriminator = None

        self.folder_id = folder_id
        self.name = name

    @property
    def folder_id(self):
        """Gets the folder_id of this GetCharactersCharacterIdBookmarksFolders200Ok.  # noqa: E501

        folder_id integer  # noqa: E501

        :return: The folder_id of this GetCharactersCharacterIdBookmarksFolders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this GetCharactersCharacterIdBookmarksFolders200Ok.

        folder_id integer  # noqa: E501

        :param folder_id: The folder_id of this GetCharactersCharacterIdBookmarksFolders200Ok.  # noqa: E501
        :type: int
        """
        if folder_id is None:
            raise ValueError("Invalid value for `folder_id`, must not be `None`")  # noqa: E501

        self._folder_id = folder_id

    @property
    def name(self):
        """Gets the name of this GetCharactersCharacterIdBookmarksFolders200Ok.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetCharactersCharacterIdBookmarksFolders200Ok.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetCharactersCharacterIdBookmarksFolders200Ok.

        name string  # noqa: E501

        :param name: The name of this GetCharactersCharacterIdBookmarksFolders200Ok.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetCharactersCharacterIdBookmarksFolders200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
