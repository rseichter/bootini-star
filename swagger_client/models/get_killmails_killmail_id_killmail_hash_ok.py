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

from swagger_client.models.get_killmails_killmail_id_killmail_hash_attacker import GetKillmailsKillmailIdKillmailHashAttacker  # noqa: F401,E501
from swagger_client.models.get_killmails_killmail_id_killmail_hash_victim import GetKillmailsKillmailIdKillmailHashVictim  # noqa: F401,E501


class GetKillmailsKillmailIdKillmailHashOk(object):
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
        'killmail_id': 'int',
        'killmail_time': 'datetime',
        'victim': 'GetKillmailsKillmailIdKillmailHashVictim',
        'attackers': 'list[GetKillmailsKillmailIdKillmailHashAttacker]',
        'solar_system_id': 'int',
        'moon_id': 'int',
        'war_id': 'int'
    }

    attribute_map = {
        'killmail_id': 'killmail_id',
        'killmail_time': 'killmail_time',
        'victim': 'victim',
        'attackers': 'attackers',
        'solar_system_id': 'solar_system_id',
        'moon_id': 'moon_id',
        'war_id': 'war_id'
    }

    def __init__(self, killmail_id=None, killmail_time=None, victim=None, attackers=None, solar_system_id=None, moon_id=None, war_id=None):  # noqa: E501
        """GetKillmailsKillmailIdKillmailHashOk - a model defined in Swagger"""  # noqa: E501

        self._killmail_id = None
        self._killmail_time = None
        self._victim = None
        self._attackers = None
        self._solar_system_id = None
        self._moon_id = None
        self._war_id = None
        self.discriminator = None

        self.killmail_id = killmail_id
        self.killmail_time = killmail_time
        self.victim = victim
        self.attackers = attackers
        self.solar_system_id = solar_system_id
        if moon_id is not None:
            self.moon_id = moon_id
        if war_id is not None:
            self.war_id = war_id

    @property
    def killmail_id(self):
        """Gets the killmail_id of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501

        ID of the killmail  # noqa: E501

        :return: The killmail_id of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501
        :rtype: int
        """
        return self._killmail_id

    @killmail_id.setter
    def killmail_id(self, killmail_id):
        """Sets the killmail_id of this GetKillmailsKillmailIdKillmailHashOk.

        ID of the killmail  # noqa: E501

        :param killmail_id: The killmail_id of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501
        :type: int
        """
        if killmail_id is None:
            raise ValueError("Invalid value for `killmail_id`, must not be `None`")  # noqa: E501

        self._killmail_id = killmail_id

    @property
    def killmail_time(self):
        """Gets the killmail_time of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501

        Time that the victim was killed and the killmail generated   # noqa: E501

        :return: The killmail_time of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501
        :rtype: datetime
        """
        return self._killmail_time

    @killmail_time.setter
    def killmail_time(self, killmail_time):
        """Sets the killmail_time of this GetKillmailsKillmailIdKillmailHashOk.

        Time that the victim was killed and the killmail generated   # noqa: E501

        :param killmail_time: The killmail_time of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501
        :type: datetime
        """
        if killmail_time is None:
            raise ValueError("Invalid value for `killmail_time`, must not be `None`")  # noqa: E501

        self._killmail_time = killmail_time

    @property
    def victim(self):
        """Gets the victim of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501


        :return: The victim of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501
        :rtype: GetKillmailsKillmailIdKillmailHashVictim
        """
        return self._victim

    @victim.setter
    def victim(self, victim):
        """Sets the victim of this GetKillmailsKillmailIdKillmailHashOk.


        :param victim: The victim of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501
        :type: GetKillmailsKillmailIdKillmailHashVictim
        """
        if victim is None:
            raise ValueError("Invalid value for `victim`, must not be `None`")  # noqa: E501

        self._victim = victim

    @property
    def attackers(self):
        """Gets the attackers of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501

        attackers array  # noqa: E501

        :return: The attackers of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501
        :rtype: list[GetKillmailsKillmailIdKillmailHashAttacker]
        """
        return self._attackers

    @attackers.setter
    def attackers(self, attackers):
        """Sets the attackers of this GetKillmailsKillmailIdKillmailHashOk.

        attackers array  # noqa: E501

        :param attackers: The attackers of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501
        :type: list[GetKillmailsKillmailIdKillmailHashAttacker]
        """
        if attackers is None:
            raise ValueError("Invalid value for `attackers`, must not be `None`")  # noqa: E501

        self._attackers = attackers

    @property
    def solar_system_id(self):
        """Gets the solar_system_id of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501

        Solar system that the kill took place in   # noqa: E501

        :return: The solar_system_id of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501
        :rtype: int
        """
        return self._solar_system_id

    @solar_system_id.setter
    def solar_system_id(self, solar_system_id):
        """Sets the solar_system_id of this GetKillmailsKillmailIdKillmailHashOk.

        Solar system that the kill took place in   # noqa: E501

        :param solar_system_id: The solar_system_id of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501
        :type: int
        """
        if solar_system_id is None:
            raise ValueError("Invalid value for `solar_system_id`, must not be `None`")  # noqa: E501

        self._solar_system_id = solar_system_id

    @property
    def moon_id(self):
        """Gets the moon_id of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501

        Moon if the kill took place at one  # noqa: E501

        :return: The moon_id of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501
        :rtype: int
        """
        return self._moon_id

    @moon_id.setter
    def moon_id(self, moon_id):
        """Sets the moon_id of this GetKillmailsKillmailIdKillmailHashOk.

        Moon if the kill took place at one  # noqa: E501

        :param moon_id: The moon_id of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501
        :type: int
        """

        self._moon_id = moon_id

    @property
    def war_id(self):
        """Gets the war_id of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501

        War if the killmail is generated in relation to an official war   # noqa: E501

        :return: The war_id of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501
        :rtype: int
        """
        return self._war_id

    @war_id.setter
    def war_id(self, war_id):
        """Sets the war_id of this GetKillmailsKillmailIdKillmailHashOk.

        War if the killmail is generated in relation to an official war   # noqa: E501

        :param war_id: The war_id of this GetKillmailsKillmailIdKillmailHashOk.  # noqa: E501
        :type: int
        """

        self._war_id = war_id

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
        if not isinstance(other, GetKillmailsKillmailIdKillmailHashOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
