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


class GetUniverseCategoriesCategoryIdOk(object):
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
        'category_id': 'int',
        'name': 'str',
        'published': 'bool',
        'groups': 'list[int]'
    }

    attribute_map = {
        'category_id': 'category_id',
        'name': 'name',
        'published': 'published',
        'groups': 'groups'
    }

    def __init__(self, category_id=None, name=None, published=None, groups=None):  # noqa: E501
        """GetUniverseCategoriesCategoryIdOk - a model defined in Swagger"""  # noqa: E501

        self._category_id = None
        self._name = None
        self._published = None
        self._groups = None
        self.discriminator = None

        self.category_id = category_id
        self.name = name
        self.published = published
        self.groups = groups

    @property
    def category_id(self):
        """Gets the category_id of this GetUniverseCategoriesCategoryIdOk.  # noqa: E501

        category_id integer  # noqa: E501

        :return: The category_id of this GetUniverseCategoriesCategoryIdOk.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this GetUniverseCategoriesCategoryIdOk.

        category_id integer  # noqa: E501

        :param category_id: The category_id of this GetUniverseCategoriesCategoryIdOk.  # noqa: E501
        :type: int
        """
        if category_id is None:
            raise ValueError("Invalid value for `category_id`, must not be `None`")  # noqa: E501

        self._category_id = category_id

    @property
    def name(self):
        """Gets the name of this GetUniverseCategoriesCategoryIdOk.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetUniverseCategoriesCategoryIdOk.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetUniverseCategoriesCategoryIdOk.

        name string  # noqa: E501

        :param name: The name of this GetUniverseCategoriesCategoryIdOk.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def published(self):
        """Gets the published of this GetUniverseCategoriesCategoryIdOk.  # noqa: E501

        published boolean  # noqa: E501

        :return: The published of this GetUniverseCategoriesCategoryIdOk.  # noqa: E501
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this GetUniverseCategoriesCategoryIdOk.

        published boolean  # noqa: E501

        :param published: The published of this GetUniverseCategoriesCategoryIdOk.  # noqa: E501
        :type: bool
        """
        if published is None:
            raise ValueError("Invalid value for `published`, must not be `None`")  # noqa: E501

        self._published = published

    @property
    def groups(self):
        """Gets the groups of this GetUniverseCategoriesCategoryIdOk.  # noqa: E501

        groups array  # noqa: E501

        :return: The groups of this GetUniverseCategoriesCategoryIdOk.  # noqa: E501
        :rtype: list[int]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this GetUniverseCategoriesCategoryIdOk.

        groups array  # noqa: E501

        :param groups: The groups of this GetUniverseCategoriesCategoryIdOk.  # noqa: E501
        :type: list[int]
        """
        if groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")  # noqa: E501

        self._groups = groups

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
        if not isinstance(other, GetUniverseCategoriesCategoryIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other