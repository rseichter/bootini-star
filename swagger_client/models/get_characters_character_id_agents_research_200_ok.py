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


class GetCharactersCharacterIdAgentsResearch200Ok(object):
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
        'agent_id': 'int',
        'skill_type_id': 'int',
        'started_at': 'datetime',
        'points_per_day': 'float',
        'remainder_points': 'float'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'skill_type_id': 'skill_type_id',
        'started_at': 'started_at',
        'points_per_day': 'points_per_day',
        'remainder_points': 'remainder_points'
    }

    def __init__(self, agent_id=None, skill_type_id=None, started_at=None, points_per_day=None, remainder_points=None):  # noqa: E501
        """GetCharactersCharacterIdAgentsResearch200Ok - a model defined in Swagger"""  # noqa: E501

        self._agent_id = None
        self._skill_type_id = None
        self._started_at = None
        self._points_per_day = None
        self._remainder_points = None
        self.discriminator = None

        self.agent_id = agent_id
        self.skill_type_id = skill_type_id
        self.started_at = started_at
        self.points_per_day = points_per_day
        self.remainder_points = remainder_points

    @property
    def agent_id(self):
        """Gets the agent_id of this GetCharactersCharacterIdAgentsResearch200Ok.  # noqa: E501

        agent_id integer  # noqa: E501

        :return: The agent_id of this GetCharactersCharacterIdAgentsResearch200Ok.  # noqa: E501
        :rtype: int
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this GetCharactersCharacterIdAgentsResearch200Ok.

        agent_id integer  # noqa: E501

        :param agent_id: The agent_id of this GetCharactersCharacterIdAgentsResearch200Ok.  # noqa: E501
        :type: int
        """
        if agent_id is None:
            raise ValueError("Invalid value for `agent_id`, must not be `None`")  # noqa: E501

        self._agent_id = agent_id

    @property
    def skill_type_id(self):
        """Gets the skill_type_id of this GetCharactersCharacterIdAgentsResearch200Ok.  # noqa: E501

        skill_type_id integer  # noqa: E501

        :return: The skill_type_id of this GetCharactersCharacterIdAgentsResearch200Ok.  # noqa: E501
        :rtype: int
        """
        return self._skill_type_id

    @skill_type_id.setter
    def skill_type_id(self, skill_type_id):
        """Sets the skill_type_id of this GetCharactersCharacterIdAgentsResearch200Ok.

        skill_type_id integer  # noqa: E501

        :param skill_type_id: The skill_type_id of this GetCharactersCharacterIdAgentsResearch200Ok.  # noqa: E501
        :type: int
        """
        if skill_type_id is None:
            raise ValueError("Invalid value for `skill_type_id`, must not be `None`")  # noqa: E501

        self._skill_type_id = skill_type_id

    @property
    def started_at(self):
        """Gets the started_at of this GetCharactersCharacterIdAgentsResearch200Ok.  # noqa: E501

        started_at string  # noqa: E501

        :return: The started_at of this GetCharactersCharacterIdAgentsResearch200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this GetCharactersCharacterIdAgentsResearch200Ok.

        started_at string  # noqa: E501

        :param started_at: The started_at of this GetCharactersCharacterIdAgentsResearch200Ok.  # noqa: E501
        :type: datetime
        """
        if started_at is None:
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def points_per_day(self):
        """Gets the points_per_day of this GetCharactersCharacterIdAgentsResearch200Ok.  # noqa: E501

        points_per_day number  # noqa: E501

        :return: The points_per_day of this GetCharactersCharacterIdAgentsResearch200Ok.  # noqa: E501
        :rtype: float
        """
        return self._points_per_day

    @points_per_day.setter
    def points_per_day(self, points_per_day):
        """Sets the points_per_day of this GetCharactersCharacterIdAgentsResearch200Ok.

        points_per_day number  # noqa: E501

        :param points_per_day: The points_per_day of this GetCharactersCharacterIdAgentsResearch200Ok.  # noqa: E501
        :type: float
        """
        if points_per_day is None:
            raise ValueError("Invalid value for `points_per_day`, must not be `None`")  # noqa: E501

        self._points_per_day = points_per_day

    @property
    def remainder_points(self):
        """Gets the remainder_points of this GetCharactersCharacterIdAgentsResearch200Ok.  # noqa: E501

        remainder_points number  # noqa: E501

        :return: The remainder_points of this GetCharactersCharacterIdAgentsResearch200Ok.  # noqa: E501
        :rtype: float
        """
        return self._remainder_points

    @remainder_points.setter
    def remainder_points(self, remainder_points):
        """Sets the remainder_points of this GetCharactersCharacterIdAgentsResearch200Ok.

        remainder_points number  # noqa: E501

        :param remainder_points: The remainder_points of this GetCharactersCharacterIdAgentsResearch200Ok.  # noqa: E501
        :type: float
        """
        if remainder_points is None:
            raise ValueError("Invalid value for `remainder_points`, must not be `None`")  # noqa: E501

        self._remainder_points = remainder_points

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
        if not isinstance(other, GetCharactersCharacterIdAgentsResearch200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
