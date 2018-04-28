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


class GetDogmaEffectsEffectIdModifier(object):
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
        'func': 'str',
        'domain': 'str',
        'modified_attribute_id': 'int',
        'modifying_attribute_id': 'int',
        'effect_id': 'int',
        'operator': 'int'
    }

    attribute_map = {
        'func': 'func',
        'domain': 'domain',
        'modified_attribute_id': 'modified_attribute_id',
        'modifying_attribute_id': 'modifying_attribute_id',
        'effect_id': 'effect_id',
        'operator': 'operator'
    }

    def __init__(self, func=None, domain=None, modified_attribute_id=None, modifying_attribute_id=None, effect_id=None, operator=None):  # noqa: E501
        """GetDogmaEffectsEffectIdModifier - a model defined in Swagger"""  # noqa: E501

        self._func = None
        self._domain = None
        self._modified_attribute_id = None
        self._modifying_attribute_id = None
        self._effect_id = None
        self._operator = None
        self.discriminator = None

        self.func = func
        if domain is not None:
            self.domain = domain
        if modified_attribute_id is not None:
            self.modified_attribute_id = modified_attribute_id
        if modifying_attribute_id is not None:
            self.modifying_attribute_id = modifying_attribute_id
        if effect_id is not None:
            self.effect_id = effect_id
        if operator is not None:
            self.operator = operator

    @property
    def func(self):
        """Gets the func of this GetDogmaEffectsEffectIdModifier.  # noqa: E501

        func string  # noqa: E501

        :return: The func of this GetDogmaEffectsEffectIdModifier.  # noqa: E501
        :rtype: str
        """
        return self._func

    @func.setter
    def func(self, func):
        """Sets the func of this GetDogmaEffectsEffectIdModifier.

        func string  # noqa: E501

        :param func: The func of this GetDogmaEffectsEffectIdModifier.  # noqa: E501
        :type: str
        """
        if func is None:
            raise ValueError("Invalid value for `func`, must not be `None`")  # noqa: E501

        self._func = func

    @property
    def domain(self):
        """Gets the domain of this GetDogmaEffectsEffectIdModifier.  # noqa: E501

        domain string  # noqa: E501

        :return: The domain of this GetDogmaEffectsEffectIdModifier.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this GetDogmaEffectsEffectIdModifier.

        domain string  # noqa: E501

        :param domain: The domain of this GetDogmaEffectsEffectIdModifier.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def modified_attribute_id(self):
        """Gets the modified_attribute_id of this GetDogmaEffectsEffectIdModifier.  # noqa: E501

        modified_attribute_id integer  # noqa: E501

        :return: The modified_attribute_id of this GetDogmaEffectsEffectIdModifier.  # noqa: E501
        :rtype: int
        """
        return self._modified_attribute_id

    @modified_attribute_id.setter
    def modified_attribute_id(self, modified_attribute_id):
        """Sets the modified_attribute_id of this GetDogmaEffectsEffectIdModifier.

        modified_attribute_id integer  # noqa: E501

        :param modified_attribute_id: The modified_attribute_id of this GetDogmaEffectsEffectIdModifier.  # noqa: E501
        :type: int
        """

        self._modified_attribute_id = modified_attribute_id

    @property
    def modifying_attribute_id(self):
        """Gets the modifying_attribute_id of this GetDogmaEffectsEffectIdModifier.  # noqa: E501

        modifying_attribute_id integer  # noqa: E501

        :return: The modifying_attribute_id of this GetDogmaEffectsEffectIdModifier.  # noqa: E501
        :rtype: int
        """
        return self._modifying_attribute_id

    @modifying_attribute_id.setter
    def modifying_attribute_id(self, modifying_attribute_id):
        """Sets the modifying_attribute_id of this GetDogmaEffectsEffectIdModifier.

        modifying_attribute_id integer  # noqa: E501

        :param modifying_attribute_id: The modifying_attribute_id of this GetDogmaEffectsEffectIdModifier.  # noqa: E501
        :type: int
        """

        self._modifying_attribute_id = modifying_attribute_id

    @property
    def effect_id(self):
        """Gets the effect_id of this GetDogmaEffectsEffectIdModifier.  # noqa: E501

        effect_id integer  # noqa: E501

        :return: The effect_id of this GetDogmaEffectsEffectIdModifier.  # noqa: E501
        :rtype: int
        """
        return self._effect_id

    @effect_id.setter
    def effect_id(self, effect_id):
        """Sets the effect_id of this GetDogmaEffectsEffectIdModifier.

        effect_id integer  # noqa: E501

        :param effect_id: The effect_id of this GetDogmaEffectsEffectIdModifier.  # noqa: E501
        :type: int
        """

        self._effect_id = effect_id

    @property
    def operator(self):
        """Gets the operator of this GetDogmaEffectsEffectIdModifier.  # noqa: E501

        operator integer  # noqa: E501

        :return: The operator of this GetDogmaEffectsEffectIdModifier.  # noqa: E501
        :rtype: int
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this GetDogmaEffectsEffectIdModifier.

        operator integer  # noqa: E501

        :param operator: The operator of this GetDogmaEffectsEffectIdModifier.  # noqa: E501
        :type: int
        """

        self._operator = operator

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
        if not isinstance(other, GetDogmaEffectsEffectIdModifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
