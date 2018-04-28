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

from swagger_client.models.get_wars_war_id_aggressor import GetWarsWarIdAggressor  # noqa: F401,E501
from swagger_client.models.get_wars_war_id_ally import GetWarsWarIdAlly  # noqa: F401,E501
from swagger_client.models.get_wars_war_id_defender import GetWarsWarIdDefender  # noqa: F401,E501


class GetWarsWarIdOk(object):
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
        'id': 'int',
        'declared': 'datetime',
        'started': 'datetime',
        'retracted': 'datetime',
        'finished': 'datetime',
        'mutual': 'bool',
        'open_for_allies': 'bool',
        'aggressor': 'GetWarsWarIdAggressor',
        'defender': 'GetWarsWarIdDefender',
        'allies': 'list[GetWarsWarIdAlly]'
    }

    attribute_map = {
        'id': 'id',
        'declared': 'declared',
        'started': 'started',
        'retracted': 'retracted',
        'finished': 'finished',
        'mutual': 'mutual',
        'open_for_allies': 'open_for_allies',
        'aggressor': 'aggressor',
        'defender': 'defender',
        'allies': 'allies'
    }

    def __init__(self, id=None, declared=None, started=None, retracted=None, finished=None, mutual=None, open_for_allies=None, aggressor=None, defender=None, allies=None):  # noqa: E501
        """GetWarsWarIdOk - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._declared = None
        self._started = None
        self._retracted = None
        self._finished = None
        self._mutual = None
        self._open_for_allies = None
        self._aggressor = None
        self._defender = None
        self._allies = None
        self.discriminator = None

        self.id = id
        self.declared = declared
        if started is not None:
            self.started = started
        if retracted is not None:
            self.retracted = retracted
        if finished is not None:
            self.finished = finished
        self.mutual = mutual
        self.open_for_allies = open_for_allies
        self.aggressor = aggressor
        self.defender = defender
        if allies is not None:
            self.allies = allies

    @property
    def id(self):
        """Gets the id of this GetWarsWarIdOk.  # noqa: E501

        ID of the specified war  # noqa: E501

        :return: The id of this GetWarsWarIdOk.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetWarsWarIdOk.

        ID of the specified war  # noqa: E501

        :param id: The id of this GetWarsWarIdOk.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def declared(self):
        """Gets the declared of this GetWarsWarIdOk.  # noqa: E501

        Time that the war was declared  # noqa: E501

        :return: The declared of this GetWarsWarIdOk.  # noqa: E501
        :rtype: datetime
        """
        return self._declared

    @declared.setter
    def declared(self, declared):
        """Sets the declared of this GetWarsWarIdOk.

        Time that the war was declared  # noqa: E501

        :param declared: The declared of this GetWarsWarIdOk.  # noqa: E501
        :type: datetime
        """
        if declared is None:
            raise ValueError("Invalid value for `declared`, must not be `None`")  # noqa: E501

        self._declared = declared

    @property
    def started(self):
        """Gets the started of this GetWarsWarIdOk.  # noqa: E501

        Time when the war started and both sides could shoot each other  # noqa: E501

        :return: The started of this GetWarsWarIdOk.  # noqa: E501
        :rtype: datetime
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this GetWarsWarIdOk.

        Time when the war started and both sides could shoot each other  # noqa: E501

        :param started: The started of this GetWarsWarIdOk.  # noqa: E501
        :type: datetime
        """

        self._started = started

    @property
    def retracted(self):
        """Gets the retracted of this GetWarsWarIdOk.  # noqa: E501

        Time the war was retracted but both sides could still shoot each other  # noqa: E501

        :return: The retracted of this GetWarsWarIdOk.  # noqa: E501
        :rtype: datetime
        """
        return self._retracted

    @retracted.setter
    def retracted(self, retracted):
        """Sets the retracted of this GetWarsWarIdOk.

        Time the war was retracted but both sides could still shoot each other  # noqa: E501

        :param retracted: The retracted of this GetWarsWarIdOk.  # noqa: E501
        :type: datetime
        """

        self._retracted = retracted

    @property
    def finished(self):
        """Gets the finished of this GetWarsWarIdOk.  # noqa: E501

        Time the war ended and shooting was no longer allowed  # noqa: E501

        :return: The finished of this GetWarsWarIdOk.  # noqa: E501
        :rtype: datetime
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """Sets the finished of this GetWarsWarIdOk.

        Time the war ended and shooting was no longer allowed  # noqa: E501

        :param finished: The finished of this GetWarsWarIdOk.  # noqa: E501
        :type: datetime
        """

        self._finished = finished

    @property
    def mutual(self):
        """Gets the mutual of this GetWarsWarIdOk.  # noqa: E501

        Was the war declared mutual by both parties  # noqa: E501

        :return: The mutual of this GetWarsWarIdOk.  # noqa: E501
        :rtype: bool
        """
        return self._mutual

    @mutual.setter
    def mutual(self, mutual):
        """Sets the mutual of this GetWarsWarIdOk.

        Was the war declared mutual by both parties  # noqa: E501

        :param mutual: The mutual of this GetWarsWarIdOk.  # noqa: E501
        :type: bool
        """
        if mutual is None:
            raise ValueError("Invalid value for `mutual`, must not be `None`")  # noqa: E501

        self._mutual = mutual

    @property
    def open_for_allies(self):
        """Gets the open_for_allies of this GetWarsWarIdOk.  # noqa: E501

        Is the war currently open for allies or not  # noqa: E501

        :return: The open_for_allies of this GetWarsWarIdOk.  # noqa: E501
        :rtype: bool
        """
        return self._open_for_allies

    @open_for_allies.setter
    def open_for_allies(self, open_for_allies):
        """Sets the open_for_allies of this GetWarsWarIdOk.

        Is the war currently open for allies or not  # noqa: E501

        :param open_for_allies: The open_for_allies of this GetWarsWarIdOk.  # noqa: E501
        :type: bool
        """
        if open_for_allies is None:
            raise ValueError("Invalid value for `open_for_allies`, must not be `None`")  # noqa: E501

        self._open_for_allies = open_for_allies

    @property
    def aggressor(self):
        """Gets the aggressor of this GetWarsWarIdOk.  # noqa: E501


        :return: The aggressor of this GetWarsWarIdOk.  # noqa: E501
        :rtype: GetWarsWarIdAggressor
        """
        return self._aggressor

    @aggressor.setter
    def aggressor(self, aggressor):
        """Sets the aggressor of this GetWarsWarIdOk.


        :param aggressor: The aggressor of this GetWarsWarIdOk.  # noqa: E501
        :type: GetWarsWarIdAggressor
        """
        if aggressor is None:
            raise ValueError("Invalid value for `aggressor`, must not be `None`")  # noqa: E501

        self._aggressor = aggressor

    @property
    def defender(self):
        """Gets the defender of this GetWarsWarIdOk.  # noqa: E501


        :return: The defender of this GetWarsWarIdOk.  # noqa: E501
        :rtype: GetWarsWarIdDefender
        """
        return self._defender

    @defender.setter
    def defender(self, defender):
        """Sets the defender of this GetWarsWarIdOk.


        :param defender: The defender of this GetWarsWarIdOk.  # noqa: E501
        :type: GetWarsWarIdDefender
        """
        if defender is None:
            raise ValueError("Invalid value for `defender`, must not be `None`")  # noqa: E501

        self._defender = defender

    @property
    def allies(self):
        """Gets the allies of this GetWarsWarIdOk.  # noqa: E501

        allied corporations or alliances, each object contains either corporation_id or alliance_id  # noqa: E501

        :return: The allies of this GetWarsWarIdOk.  # noqa: E501
        :rtype: list[GetWarsWarIdAlly]
        """
        return self._allies

    @allies.setter
    def allies(self, allies):
        """Sets the allies of this GetWarsWarIdOk.

        allied corporations or alliances, each object contains either corporation_id or alliance_id  # noqa: E501

        :param allies: The allies of this GetWarsWarIdOk.  # noqa: E501
        :type: list[GetWarsWarIdAlly]
        """

        self._allies = allies

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
        if not isinstance(other, GetWarsWarIdOk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
