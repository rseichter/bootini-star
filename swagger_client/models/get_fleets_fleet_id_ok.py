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


class GetFleetsFleetIdOk(object):
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
        'motd': 'str',
        'is_free_move': 'bool',
        'is_registered': 'bool',
        'is_voice_enabled': 'bool'
    }

    attribute_map = {
        'motd': 'motd',
        'is_free_move': 'is_free_move',
        'is_registered': 'is_registered',
        'is_voice_enabled': 'is_voice_enabled'
    }

    def __init__(self, motd=None, is_free_move=None, is_registered=None, is_voice_enabled=None):  # noqa: E501
        """GetFleetsFleetIdOk - a model defined in Swagger"""  # noqa: E501

        self._motd = None
        self._is_free_move = None
        self._is_registered = None
        self._is_voice_enabled = None
        self.discriminator = None

        self.motd = motd
        self.is_free_move = is_free_move
        self.is_registered = is_registered
        self.is_voice_enabled = is_voice_enabled

    @property
    def motd(self):
        """Gets the motd of this GetFleetsFleetIdOk.  # noqa: E501

        Fleet MOTD in CCP flavoured HTML  # noqa: E501

        :return: The motd of this GetFleetsFleetIdOk.  # noqa: E501
        :rtype: str
        """
        return self._motd

    @motd.setter
    def motd(self, motd):
        """Sets the motd of this GetFleetsFleetIdOk.

        Fleet MOTD in CCP flavoured HTML  # noqa: E501

        :param motd: The motd of this GetFleetsFleetIdOk.  # noqa: E501
        :type: str
        """
        if motd is None:
            raise ValueError("Invalid value for `motd`, must not be `None`")  # noqa: E501

        self._motd = motd

    @property
    def is_free_move(self):
        """Gets the is_free_move of this GetFleetsFleetIdOk.  # noqa: E501

        Is free-move enabled  # noqa: E501

        :return: The is_free_move of this GetFleetsFleetIdOk.  # noqa: E501
        :rtype: bool
        """
        return self._is_free_move

    @is_free_move.setter
    def is_free_move(self, is_free_move):
        """Sets the is_free_move of this GetFleetsFleetIdOk.

        Is free-move enabled  # noqa: E501

        :param is_free_move: The is_free_move of this GetFleetsFleetIdOk.  # noqa: E501
        :type: bool
        """
        if is_free_move is None:
            raise ValueError("Invalid value for `is_free_move`, must not be `None`")  # noqa: E501

        self._is_free_move = is_free_move

    @property
    def is_registered(self):
        """Gets the is_registered of this GetFleetsFleetIdOk.  # noqa: E501

        Does the fleet have an active fleet advertisement  # noqa: E501

        :return: The is_registered of this GetFleetsFleetIdOk.  # noqa: E501
        :rtype: bool
        """
        return self._is_registered

    @is_registered.setter
    def is_registered(self, is_registered):
        """Sets the is_registered of this GetFleetsFleetIdOk.

        Does the fleet have an active fleet advertisement  # noqa: E501

        :param is_registered: The is_registered of this GetFleetsFleetIdOk.  # noqa: E501
        :type: bool
        """
        if is_registered is None:
            raise ValueError("Invalid value for `is_registered`, must not be `None`")  # noqa: E501

        self._is_registered = is_registered

    @property
    def is_voice_enabled(self):
        """Gets the is_voice_enabled of this GetFleetsFleetIdOk.  # noqa: E501

        Is EVE Voice enabled  # noqa: E501

        :return: The is_voice_enabled of this GetFleetsFleetIdOk.  # noqa: E501
        :rtype: bool
        """
        return self._is_voice_enabled

    @is_voice_enabled.setter
    def is_voice_enabled(self, is_voice_enabled):
        """Sets the is_voice_enabled of this GetFleetsFleetIdOk.

        Is EVE Voice enabled  # noqa: E501

        :param is_voice_enabled: The is_voice_enabled of this GetFleetsFleetIdOk.  # noqa: E501
        :type: bool
        """
        if is_voice_enabled is None:
            raise ValueError("Invalid value for `is_voice_enabled`, must not be `None`")  # noqa: E501

        self._is_voice_enabled = is_voice_enabled

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
        if not isinstance(other, GetFleetsFleetIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other