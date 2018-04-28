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


class GetCharactersCharacterIdAttributesOk(object):
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
        'charisma': 'int',
        'intelligence': 'int',
        'memory': 'int',
        'perception': 'int',
        'willpower': 'int',
        'bonus_remaps': 'int',
        'last_remap_date': 'datetime',
        'accrued_remap_cooldown_date': 'datetime'
    }

    attribute_map = {
        'charisma': 'charisma',
        'intelligence': 'intelligence',
        'memory': 'memory',
        'perception': 'perception',
        'willpower': 'willpower',
        'bonus_remaps': 'bonus_remaps',
        'last_remap_date': 'last_remap_date',
        'accrued_remap_cooldown_date': 'accrued_remap_cooldown_date'
    }

    def __init__(self, charisma=None, intelligence=None, memory=None, perception=None, willpower=None, bonus_remaps=None, last_remap_date=None, accrued_remap_cooldown_date=None):  # noqa: E501
        """GetCharactersCharacterIdAttributesOk - a model defined in Swagger"""  # noqa: E501

        self._charisma = None
        self._intelligence = None
        self._memory = None
        self._perception = None
        self._willpower = None
        self._bonus_remaps = None
        self._last_remap_date = None
        self._accrued_remap_cooldown_date = None
        self.discriminator = None

        self.charisma = charisma
        self.intelligence = intelligence
        self.memory = memory
        self.perception = perception
        self.willpower = willpower
        if bonus_remaps is not None:
            self.bonus_remaps = bonus_remaps
        if last_remap_date is not None:
            self.last_remap_date = last_remap_date
        if accrued_remap_cooldown_date is not None:
            self.accrued_remap_cooldown_date = accrued_remap_cooldown_date

    @property
    def charisma(self):
        """Gets the charisma of this GetCharactersCharacterIdAttributesOk.  # noqa: E501

        charisma integer  # noqa: E501

        :return: The charisma of this GetCharactersCharacterIdAttributesOk.  # noqa: E501
        :rtype: int
        """
        return self._charisma

    @charisma.setter
    def charisma(self, charisma):
        """Sets the charisma of this GetCharactersCharacterIdAttributesOk.

        charisma integer  # noqa: E501

        :param charisma: The charisma of this GetCharactersCharacterIdAttributesOk.  # noqa: E501
        :type: int
        """
        if charisma is None:
            raise ValueError("Invalid value for `charisma`, must not be `None`")  # noqa: E501

        self._charisma = charisma

    @property
    def intelligence(self):
        """Gets the intelligence of this GetCharactersCharacterIdAttributesOk.  # noqa: E501

        intelligence integer  # noqa: E501

        :return: The intelligence of this GetCharactersCharacterIdAttributesOk.  # noqa: E501
        :rtype: int
        """
        return self._intelligence

    @intelligence.setter
    def intelligence(self, intelligence):
        """Sets the intelligence of this GetCharactersCharacterIdAttributesOk.

        intelligence integer  # noqa: E501

        :param intelligence: The intelligence of this GetCharactersCharacterIdAttributesOk.  # noqa: E501
        :type: int
        """
        if intelligence is None:
            raise ValueError("Invalid value for `intelligence`, must not be `None`")  # noqa: E501

        self._intelligence = intelligence

    @property
    def memory(self):
        """Gets the memory of this GetCharactersCharacterIdAttributesOk.  # noqa: E501

        memory integer  # noqa: E501

        :return: The memory of this GetCharactersCharacterIdAttributesOk.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this GetCharactersCharacterIdAttributesOk.

        memory integer  # noqa: E501

        :param memory: The memory of this GetCharactersCharacterIdAttributesOk.  # noqa: E501
        :type: int
        """
        if memory is None:
            raise ValueError("Invalid value for `memory`, must not be `None`")  # noqa: E501

        self._memory = memory

    @property
    def perception(self):
        """Gets the perception of this GetCharactersCharacterIdAttributesOk.  # noqa: E501

        perception integer  # noqa: E501

        :return: The perception of this GetCharactersCharacterIdAttributesOk.  # noqa: E501
        :rtype: int
        """
        return self._perception

    @perception.setter
    def perception(self, perception):
        """Sets the perception of this GetCharactersCharacterIdAttributesOk.

        perception integer  # noqa: E501

        :param perception: The perception of this GetCharactersCharacterIdAttributesOk.  # noqa: E501
        :type: int
        """
        if perception is None:
            raise ValueError("Invalid value for `perception`, must not be `None`")  # noqa: E501

        self._perception = perception

    @property
    def willpower(self):
        """Gets the willpower of this GetCharactersCharacterIdAttributesOk.  # noqa: E501

        willpower integer  # noqa: E501

        :return: The willpower of this GetCharactersCharacterIdAttributesOk.  # noqa: E501
        :rtype: int
        """
        return self._willpower

    @willpower.setter
    def willpower(self, willpower):
        """Sets the willpower of this GetCharactersCharacterIdAttributesOk.

        willpower integer  # noqa: E501

        :param willpower: The willpower of this GetCharactersCharacterIdAttributesOk.  # noqa: E501
        :type: int
        """
        if willpower is None:
            raise ValueError("Invalid value for `willpower`, must not be `None`")  # noqa: E501

        self._willpower = willpower

    @property
    def bonus_remaps(self):
        """Gets the bonus_remaps of this GetCharactersCharacterIdAttributesOk.  # noqa: E501

        Number of available bonus character neural remaps  # noqa: E501

        :return: The bonus_remaps of this GetCharactersCharacterIdAttributesOk.  # noqa: E501
        :rtype: int
        """
        return self._bonus_remaps

    @bonus_remaps.setter
    def bonus_remaps(self, bonus_remaps):
        """Sets the bonus_remaps of this GetCharactersCharacterIdAttributesOk.

        Number of available bonus character neural remaps  # noqa: E501

        :param bonus_remaps: The bonus_remaps of this GetCharactersCharacterIdAttributesOk.  # noqa: E501
        :type: int
        """

        self._bonus_remaps = bonus_remaps

    @property
    def last_remap_date(self):
        """Gets the last_remap_date of this GetCharactersCharacterIdAttributesOk.  # noqa: E501

        Datetime of last neural remap, including usage of bonus remaps  # noqa: E501

        :return: The last_remap_date of this GetCharactersCharacterIdAttributesOk.  # noqa: E501
        :rtype: datetime
        """
        return self._last_remap_date

    @last_remap_date.setter
    def last_remap_date(self, last_remap_date):
        """Sets the last_remap_date of this GetCharactersCharacterIdAttributesOk.

        Datetime of last neural remap, including usage of bonus remaps  # noqa: E501

        :param last_remap_date: The last_remap_date of this GetCharactersCharacterIdAttributesOk.  # noqa: E501
        :type: datetime
        """

        self._last_remap_date = last_remap_date

    @property
    def accrued_remap_cooldown_date(self):
        """Gets the accrued_remap_cooldown_date of this GetCharactersCharacterIdAttributesOk.  # noqa: E501

        Neural remapping cooldown after a character uses remap accrued over time  # noqa: E501

        :return: The accrued_remap_cooldown_date of this GetCharactersCharacterIdAttributesOk.  # noqa: E501
        :rtype: datetime
        """
        return self._accrued_remap_cooldown_date

    @accrued_remap_cooldown_date.setter
    def accrued_remap_cooldown_date(self, accrued_remap_cooldown_date):
        """Sets the accrued_remap_cooldown_date of this GetCharactersCharacterIdAttributesOk.

        Neural remapping cooldown after a character uses remap accrued over time  # noqa: E501

        :param accrued_remap_cooldown_date: The accrued_remap_cooldown_date of this GetCharactersCharacterIdAttributesOk.  # noqa: E501
        :type: datetime
        """

        self._accrued_remap_cooldown_date = accrued_remap_cooldown_date

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
        if not isinstance(other, GetCharactersCharacterIdAttributesOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
