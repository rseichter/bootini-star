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

from swagger_client.models.get_universe_stargates_stargate_id_destination import GetUniverseStargatesStargateIdDestination  # noqa: F401,E501
from swagger_client.models.get_universe_stargates_stargate_id_position import GetUniverseStargatesStargateIdPosition  # noqa: F401,E501


class GetUniverseStargatesStargateIdOk(object):
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
        'stargate_id': 'int',
        'name': 'str',
        'type_id': 'int',
        'position': 'GetUniverseStargatesStargateIdPosition',
        'system_id': 'int',
        'destination': 'GetUniverseStargatesStargateIdDestination'
    }

    attribute_map = {
        'stargate_id': 'stargate_id',
        'name': 'name',
        'type_id': 'type_id',
        'position': 'position',
        'system_id': 'system_id',
        'destination': 'destination'
    }

    def __init__(self, stargate_id=None, name=None, type_id=None, position=None, system_id=None, destination=None):  # noqa: E501
        """GetUniverseStargatesStargateIdOk - a model defined in Swagger"""  # noqa: E501

        self._stargate_id = None
        self._name = None
        self._type_id = None
        self._position = None
        self._system_id = None
        self._destination = None
        self.discriminator = None

        self.stargate_id = stargate_id
        self.name = name
        self.type_id = type_id
        self.position = position
        self.system_id = system_id
        self.destination = destination

    @property
    def stargate_id(self):
        """Gets the stargate_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501

        stargate_id integer  # noqa: E501

        :return: The stargate_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :rtype: int
        """
        return self._stargate_id

    @stargate_id.setter
    def stargate_id(self, stargate_id):
        """Sets the stargate_id of this GetUniverseStargatesStargateIdOk.

        stargate_id integer  # noqa: E501

        :param stargate_id: The stargate_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :type: int
        """
        if stargate_id is None:
            raise ValueError("Invalid value for `stargate_id`, must not be `None`")  # noqa: E501

        self._stargate_id = stargate_id

    @property
    def name(self):
        """Gets the name of this GetUniverseStargatesStargateIdOk.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetUniverseStargatesStargateIdOk.

        name string  # noqa: E501

        :param name: The name of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type_id(self):
        """Gets the type_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetUniverseStargatesStargateIdOk.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

    @property
    def position(self):
        """Gets the position of this GetUniverseStargatesStargateIdOk.  # noqa: E501


        :return: The position of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :rtype: GetUniverseStargatesStargateIdPosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this GetUniverseStargatesStargateIdOk.


        :param position: The position of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :type: GetUniverseStargatesStargateIdPosition
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

    @property
    def system_id(self):
        """Gets the system_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501

        The solar system this stargate is in  # noqa: E501

        :return: The system_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this GetUniverseStargatesStargateIdOk.

        The solar system this stargate is in  # noqa: E501

        :param system_id: The system_id of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :type: int
        """
        if system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")  # noqa: E501

        self._system_id = system_id

    @property
    def destination(self):
        """Gets the destination of this GetUniverseStargatesStargateIdOk.  # noqa: E501


        :return: The destination of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :rtype: GetUniverseStargatesStargateIdDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this GetUniverseStargatesStargateIdOk.


        :param destination: The destination of this GetUniverseStargatesStargateIdOk.  # noqa: E501
        :type: GetUniverseStargatesStargateIdDestination
        """
        if destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

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
        if not isinstance(other, GetUniverseStargatesStargateIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
