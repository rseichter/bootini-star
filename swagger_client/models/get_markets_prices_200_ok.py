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


class GetMarketsPrices200Ok(object):
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
        'type_id': 'int',
        'average_price': 'float',
        'adjusted_price': 'float'
    }

    attribute_map = {
        'type_id': 'type_id',
        'average_price': 'average_price',
        'adjusted_price': 'adjusted_price'
    }

    def __init__(self, type_id=None, average_price=None, adjusted_price=None):  # noqa: E501
        """GetMarketsPrices200Ok - a model defined in Swagger"""  # noqa: E501

        self._type_id = None
        self._average_price = None
        self._adjusted_price = None
        self.discriminator = None

        self.type_id = type_id
        if average_price is not None:
            self.average_price = average_price
        if adjusted_price is not None:
            self.adjusted_price = adjusted_price

    @property
    def type_id(self):
        """Gets the type_id of this GetMarketsPrices200Ok.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetMarketsPrices200Ok.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetMarketsPrices200Ok.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetMarketsPrices200Ok.  # noqa: E501
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

    @property
    def average_price(self):
        """Gets the average_price of this GetMarketsPrices200Ok.  # noqa: E501

        average_price number  # noqa: E501

        :return: The average_price of this GetMarketsPrices200Ok.  # noqa: E501
        :rtype: float
        """
        return self._average_price

    @average_price.setter
    def average_price(self, average_price):
        """Sets the average_price of this GetMarketsPrices200Ok.

        average_price number  # noqa: E501

        :param average_price: The average_price of this GetMarketsPrices200Ok.  # noqa: E501
        :type: float
        """

        self._average_price = average_price

    @property
    def adjusted_price(self):
        """Gets the adjusted_price of this GetMarketsPrices200Ok.  # noqa: E501

        adjusted_price number  # noqa: E501

        :return: The adjusted_price of this GetMarketsPrices200Ok.  # noqa: E501
        :rtype: float
        """
        return self._adjusted_price

    @adjusted_price.setter
    def adjusted_price(self, adjusted_price):
        """Sets the adjusted_price of this GetMarketsPrices200Ok.

        adjusted_price number  # noqa: E501

        :param adjusted_price: The adjusted_price of this GetMarketsPrices200Ok.  # noqa: E501
        :type: float
        """

        self._adjusted_price = adjusted_price

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
        if not isinstance(other, GetMarketsPrices200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
