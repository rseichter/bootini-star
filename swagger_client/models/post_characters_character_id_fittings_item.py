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


class PostCharactersCharacterIdFittingsItem(object):
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
        'flag': 'int',
        'quantity': 'int'
    }

    attribute_map = {
        'type_id': 'type_id',
        'flag': 'flag',
        'quantity': 'quantity'
    }

    def __init__(self, type_id=None, flag=None, quantity=None):  # noqa: E501
        """PostCharactersCharacterIdFittingsItem - a model defined in Swagger"""  # noqa: E501

        self._type_id = None
        self._flag = None
        self._quantity = None
        self.discriminator = None

        self.type_id = type_id
        self.flag = flag
        self.quantity = quantity

    @property
    def type_id(self):
        """Gets the type_id of this PostCharactersCharacterIdFittingsItem.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this PostCharactersCharacterIdFittingsItem.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this PostCharactersCharacterIdFittingsItem.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this PostCharactersCharacterIdFittingsItem.  # noqa: E501
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

    @property
    def flag(self):
        """Gets the flag of this PostCharactersCharacterIdFittingsItem.  # noqa: E501

        flag integer  # noqa: E501

        :return: The flag of this PostCharactersCharacterIdFittingsItem.  # noqa: E501
        :rtype: int
        """
        return self._flag

    @flag.setter
    def flag(self, flag):
        """Sets the flag of this PostCharactersCharacterIdFittingsItem.

        flag integer  # noqa: E501

        :param flag: The flag of this PostCharactersCharacterIdFittingsItem.  # noqa: E501
        :type: int
        """
        if flag is None:
            raise ValueError("Invalid value for `flag`, must not be `None`")  # noqa: E501

        self._flag = flag

    @property
    def quantity(self):
        """Gets the quantity of this PostCharactersCharacterIdFittingsItem.  # noqa: E501

        quantity integer  # noqa: E501

        :return: The quantity of this PostCharactersCharacterIdFittingsItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PostCharactersCharacterIdFittingsItem.

        quantity integer  # noqa: E501

        :param quantity: The quantity of this PostCharactersCharacterIdFittingsItem.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

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
        if not isinstance(other, PostCharactersCharacterIdFittingsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
