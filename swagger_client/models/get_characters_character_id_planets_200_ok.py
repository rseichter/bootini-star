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


class GetCharactersCharacterIdPlanets200Ok(object):
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
        'solar_system_id': 'int',
        'planet_id': 'int',
        'owner_id': 'int',
        'upgrade_level': 'int',
        'num_pins': 'int',
        'last_update': 'datetime',
        'planet_type': 'str'
    }

    attribute_map = {
        'solar_system_id': 'solar_system_id',
        'planet_id': 'planet_id',
        'owner_id': 'owner_id',
        'upgrade_level': 'upgrade_level',
        'num_pins': 'num_pins',
        'last_update': 'last_update',
        'planet_type': 'planet_type'
    }

    def __init__(self, solar_system_id=None, planet_id=None, owner_id=None, upgrade_level=None, num_pins=None, last_update=None, planet_type=None):  # noqa: E501
        """GetCharactersCharacterIdPlanets200Ok - a model defined in Swagger"""  # noqa: E501

        self._solar_system_id = None
        self._planet_id = None
        self._owner_id = None
        self._upgrade_level = None
        self._num_pins = None
        self._last_update = None
        self._planet_type = None
        self.discriminator = None

        self.solar_system_id = solar_system_id
        self.planet_id = planet_id
        self.owner_id = owner_id
        self.upgrade_level = upgrade_level
        self.num_pins = num_pins
        self.last_update = last_update
        self.planet_type = planet_type

    @property
    def solar_system_id(self):
        """Gets the solar_system_id of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501

        solar_system_id integer  # noqa: E501

        :return: The solar_system_id of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501
        :rtype: int
        """
        return self._solar_system_id

    @solar_system_id.setter
    def solar_system_id(self, solar_system_id):
        """Sets the solar_system_id of this GetCharactersCharacterIdPlanets200Ok.

        solar_system_id integer  # noqa: E501

        :param solar_system_id: The solar_system_id of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501
        :type: int
        """
        if solar_system_id is None:
            raise ValueError("Invalid value for `solar_system_id`, must not be `None`")  # noqa: E501

        self._solar_system_id = solar_system_id

    @property
    def planet_id(self):
        """Gets the planet_id of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501

        planet_id integer  # noqa: E501

        :return: The planet_id of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501
        :rtype: int
        """
        return self._planet_id

    @planet_id.setter
    def planet_id(self, planet_id):
        """Sets the planet_id of this GetCharactersCharacterIdPlanets200Ok.

        planet_id integer  # noqa: E501

        :param planet_id: The planet_id of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501
        :type: int
        """
        if planet_id is None:
            raise ValueError("Invalid value for `planet_id`, must not be `None`")  # noqa: E501

        self._planet_id = planet_id

    @property
    def owner_id(self):
        """Gets the owner_id of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501

        owner_id integer  # noqa: E501

        :return: The owner_id of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this GetCharactersCharacterIdPlanets200Ok.

        owner_id integer  # noqa: E501

        :param owner_id: The owner_id of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501
        :type: int
        """
        if owner_id is None:
            raise ValueError("Invalid value for `owner_id`, must not be `None`")  # noqa: E501

        self._owner_id = owner_id

    @property
    def upgrade_level(self):
        """Gets the upgrade_level of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501

        upgrade_level integer  # noqa: E501

        :return: The upgrade_level of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501
        :rtype: int
        """
        return self._upgrade_level

    @upgrade_level.setter
    def upgrade_level(self, upgrade_level):
        """Sets the upgrade_level of this GetCharactersCharacterIdPlanets200Ok.

        upgrade_level integer  # noqa: E501

        :param upgrade_level: The upgrade_level of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501
        :type: int
        """
        if upgrade_level is None:
            raise ValueError("Invalid value for `upgrade_level`, must not be `None`")  # noqa: E501
        if upgrade_level is not None and upgrade_level > 5:  # noqa: E501
            raise ValueError("Invalid value for `upgrade_level`, must be a value less than or equal to `5`")  # noqa: E501
        if upgrade_level is not None and upgrade_level < 0:  # noqa: E501
            raise ValueError("Invalid value for `upgrade_level`, must be a value greater than or equal to `0`")  # noqa: E501

        self._upgrade_level = upgrade_level

    @property
    def num_pins(self):
        """Gets the num_pins of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501

        num_pins integer  # noqa: E501

        :return: The num_pins of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501
        :rtype: int
        """
        return self._num_pins

    @num_pins.setter
    def num_pins(self, num_pins):
        """Sets the num_pins of this GetCharactersCharacterIdPlanets200Ok.

        num_pins integer  # noqa: E501

        :param num_pins: The num_pins of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501
        :type: int
        """
        if num_pins is None:
            raise ValueError("Invalid value for `num_pins`, must not be `None`")  # noqa: E501
        if num_pins is not None and num_pins < 1:  # noqa: E501
            raise ValueError("Invalid value for `num_pins`, must be a value greater than or equal to `1`")  # noqa: E501

        self._num_pins = num_pins

    @property
    def last_update(self):
        """Gets the last_update of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501

        last_update string  # noqa: E501

        :return: The last_update of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this GetCharactersCharacterIdPlanets200Ok.

        last_update string  # noqa: E501

        :param last_update: The last_update of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501
        :type: datetime
        """
        if last_update is None:
            raise ValueError("Invalid value for `last_update`, must not be `None`")  # noqa: E501

        self._last_update = last_update

    @property
    def planet_type(self):
        """Gets the planet_type of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501

        planet_type string  # noqa: E501

        :return: The planet_type of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501
        :rtype: str
        """
        return self._planet_type

    @planet_type.setter
    def planet_type(self, planet_type):
        """Sets the planet_type of this GetCharactersCharacterIdPlanets200Ok.

        planet_type string  # noqa: E501

        :param planet_type: The planet_type of this GetCharactersCharacterIdPlanets200Ok.  # noqa: E501
        :type: str
        """
        if planet_type is None:
            raise ValueError("Invalid value for `planet_type`, must not be `None`")  # noqa: E501
        allowed_values = ["temperate", "barren", "oceanic", "ice", "gas", "lava", "storm", "plasma"]  # noqa: E501
        if planet_type not in allowed_values:
            raise ValueError(
                "Invalid value for `planet_type` ({0}), must be one of {1}"  # noqa: E501
                .format(planet_type, allowed_values)
            )

        self._planet_type = planet_type

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
        if not isinstance(other, GetCharactersCharacterIdPlanets200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
