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


class GetFwLeaderboardsCorporationsActiveTotal(object):
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
        'corporation_id': 'int',
        'amount': 'int'
    }

    attribute_map = {
        'corporation_id': 'corporation_id',
        'amount': 'amount'
    }

    def __init__(self, corporation_id=None, amount=None):  # noqa: E501
        """GetFwLeaderboardsCorporationsActiveTotal - a model defined in Swagger"""  # noqa: E501

        self._corporation_id = None
        self._amount = None
        self.discriminator = None

        if corporation_id is not None:
            self.corporation_id = corporation_id
        if amount is not None:
            self.amount = amount

    @property
    def corporation_id(self):
        """Gets the corporation_id of this GetFwLeaderboardsCorporationsActiveTotal.  # noqa: E501

        corporation_id integer  # noqa: E501

        :return: The corporation_id of this GetFwLeaderboardsCorporationsActiveTotal.  # noqa: E501
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """Sets the corporation_id of this GetFwLeaderboardsCorporationsActiveTotal.

        corporation_id integer  # noqa: E501

        :param corporation_id: The corporation_id of this GetFwLeaderboardsCorporationsActiveTotal.  # noqa: E501
        :type: int
        """

        self._corporation_id = corporation_id

    @property
    def amount(self):
        """Gets the amount of this GetFwLeaderboardsCorporationsActiveTotal.  # noqa: E501

        Amount of kills  # noqa: E501

        :return: The amount of this GetFwLeaderboardsCorporationsActiveTotal.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetFwLeaderboardsCorporationsActiveTotal.

        Amount of kills  # noqa: E501

        :param amount: The amount of this GetFwLeaderboardsCorporationsActiveTotal.  # noqa: E501
        :type: int
        """

        self._amount = amount

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
        if not isinstance(other, GetFwLeaderboardsCorporationsActiveTotal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
