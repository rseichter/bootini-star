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


class GetMarketsGroupsMarketGroupIdOk(object):
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
        'market_group_id': 'int',
        'name': 'str',
        'description': 'str',
        'types': 'list[int]',
        'parent_group_id': 'int'
    }

    attribute_map = {
        'market_group_id': 'market_group_id',
        'name': 'name',
        'description': 'description',
        'types': 'types',
        'parent_group_id': 'parent_group_id'
    }

    def __init__(self, market_group_id=None, name=None, description=None, types=None, parent_group_id=None):  # noqa: E501
        """GetMarketsGroupsMarketGroupIdOk - a model defined in Swagger"""  # noqa: E501

        self._market_group_id = None
        self._name = None
        self._description = None
        self._types = None
        self._parent_group_id = None
        self.discriminator = None

        self.market_group_id = market_group_id
        self.name = name
        self.description = description
        self.types = types
        if parent_group_id is not None:
            self.parent_group_id = parent_group_id

    @property
    def market_group_id(self):
        """Gets the market_group_id of this GetMarketsGroupsMarketGroupIdOk.  # noqa: E501

        market_group_id integer  # noqa: E501

        :return: The market_group_id of this GetMarketsGroupsMarketGroupIdOk.  # noqa: E501
        :rtype: int
        """
        return self._market_group_id

    @market_group_id.setter
    def market_group_id(self, market_group_id):
        """Sets the market_group_id of this GetMarketsGroupsMarketGroupIdOk.

        market_group_id integer  # noqa: E501

        :param market_group_id: The market_group_id of this GetMarketsGroupsMarketGroupIdOk.  # noqa: E501
        :type: int
        """
        if market_group_id is None:
            raise ValueError("Invalid value for `market_group_id`, must not be `None`")  # noqa: E501

        self._market_group_id = market_group_id

    @property
    def name(self):
        """Gets the name of this GetMarketsGroupsMarketGroupIdOk.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetMarketsGroupsMarketGroupIdOk.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetMarketsGroupsMarketGroupIdOk.

        name string  # noqa: E501

        :param name: The name of this GetMarketsGroupsMarketGroupIdOk.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this GetMarketsGroupsMarketGroupIdOk.  # noqa: E501

        description string  # noqa: E501

        :return: The description of this GetMarketsGroupsMarketGroupIdOk.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetMarketsGroupsMarketGroupIdOk.

        description string  # noqa: E501

        :param description: The description of this GetMarketsGroupsMarketGroupIdOk.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def types(self):
        """Gets the types of this GetMarketsGroupsMarketGroupIdOk.  # noqa: E501

        types array  # noqa: E501

        :return: The types of this GetMarketsGroupsMarketGroupIdOk.  # noqa: E501
        :rtype: list[int]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this GetMarketsGroupsMarketGroupIdOk.

        types array  # noqa: E501

        :param types: The types of this GetMarketsGroupsMarketGroupIdOk.  # noqa: E501
        :type: list[int]
        """
        if types is None:
            raise ValueError("Invalid value for `types`, must not be `None`")  # noqa: E501

        self._types = types

    @property
    def parent_group_id(self):
        """Gets the parent_group_id of this GetMarketsGroupsMarketGroupIdOk.  # noqa: E501

        parent_group_id integer  # noqa: E501

        :return: The parent_group_id of this GetMarketsGroupsMarketGroupIdOk.  # noqa: E501
        :rtype: int
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """Sets the parent_group_id of this GetMarketsGroupsMarketGroupIdOk.

        parent_group_id integer  # noqa: E501

        :param parent_group_id: The parent_group_id of this GetMarketsGroupsMarketGroupIdOk.  # noqa: E501
        :type: int
        """

        self._parent_group_id = parent_group_id

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
        if not isinstance(other, GetMarketsGroupsMarketGroupIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other