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

from swagger_client.models.get_universe_structures_structure_id_position import GetUniverseStructuresStructureIdPosition  # noqa: F401,E501


class GetUniverseStructuresStructureIdOk(object):
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
        'name': 'str',
        'solar_system_id': 'int',
        'type_id': 'int',
        'position': 'GetUniverseStructuresStructureIdPosition'
    }

    attribute_map = {
        'name': 'name',
        'solar_system_id': 'solar_system_id',
        'type_id': 'type_id',
        'position': 'position'
    }

    def __init__(self, name=None, solar_system_id=None, type_id=None, position=None):  # noqa: E501
        """GetUniverseStructuresStructureIdOk - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._solar_system_id = None
        self._type_id = None
        self._position = None
        self.discriminator = None

        self.name = name
        self.solar_system_id = solar_system_id
        if type_id is not None:
            self.type_id = type_id
        if position is not None:
            self.position = position

    @property
    def name(self):
        """Gets the name of this GetUniverseStructuresStructureIdOk.  # noqa: E501

        The full name of the structure  # noqa: E501

        :return: The name of this GetUniverseStructuresStructureIdOk.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetUniverseStructuresStructureIdOk.

        The full name of the structure  # noqa: E501

        :param name: The name of this GetUniverseStructuresStructureIdOk.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def solar_system_id(self):
        """Gets the solar_system_id of this GetUniverseStructuresStructureIdOk.  # noqa: E501

        solar_system_id integer  # noqa: E501

        :return: The solar_system_id of this GetUniverseStructuresStructureIdOk.  # noqa: E501
        :rtype: int
        """
        return self._solar_system_id

    @solar_system_id.setter
    def solar_system_id(self, solar_system_id):
        """Sets the solar_system_id of this GetUniverseStructuresStructureIdOk.

        solar_system_id integer  # noqa: E501

        :param solar_system_id: The solar_system_id of this GetUniverseStructuresStructureIdOk.  # noqa: E501
        :type: int
        """
        if solar_system_id is None:
            raise ValueError("Invalid value for `solar_system_id`, must not be `None`")  # noqa: E501

        self._solar_system_id = solar_system_id

    @property
    def type_id(self):
        """Gets the type_id of this GetUniverseStructuresStructureIdOk.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetUniverseStructuresStructureIdOk.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetUniverseStructuresStructureIdOk.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetUniverseStructuresStructureIdOk.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

    @property
    def position(self):
        """Gets the position of this GetUniverseStructuresStructureIdOk.  # noqa: E501


        :return: The position of this GetUniverseStructuresStructureIdOk.  # noqa: E501
        :rtype: GetUniverseStructuresStructureIdPosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this GetUniverseStructuresStructureIdOk.


        :param position: The position of this GetUniverseStructuresStructureIdOk.  # noqa: E501
        :type: GetUniverseStructuresStructureIdPosition
        """

        self._position = position

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
        if not isinstance(other, GetUniverseStructuresStructureIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
