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

from swagger_client.models.get_fleets_fleet_id_wings_squad import GetFleetsFleetIdWingsSquad  # noqa: F401,E501


class GetFleetsFleetIdWings200Ok(object):
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
        'id': 'int',
        'squads': 'list[GetFleetsFleetIdWingsSquad]'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'squads': 'squads'
    }

    def __init__(self, name=None, id=None, squads=None):  # noqa: E501
        """GetFleetsFleetIdWings200Ok - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._id = None
        self._squads = None
        self.discriminator = None

        self.name = name
        self.id = id
        self.squads = squads

    @property
    def name(self):
        """Gets the name of this GetFleetsFleetIdWings200Ok.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetFleetsFleetIdWings200Ok.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetFleetsFleetIdWings200Ok.

        name string  # noqa: E501

        :param name: The name of this GetFleetsFleetIdWings200Ok.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this GetFleetsFleetIdWings200Ok.  # noqa: E501

        id integer  # noqa: E501

        :return: The id of this GetFleetsFleetIdWings200Ok.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetFleetsFleetIdWings200Ok.

        id integer  # noqa: E501

        :param id: The id of this GetFleetsFleetIdWings200Ok.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def squads(self):
        """Gets the squads of this GetFleetsFleetIdWings200Ok.  # noqa: E501

        squads array  # noqa: E501

        :return: The squads of this GetFleetsFleetIdWings200Ok.  # noqa: E501
        :rtype: list[GetFleetsFleetIdWingsSquad]
        """
        return self._squads

    @squads.setter
    def squads(self, squads):
        """Sets the squads of this GetFleetsFleetIdWings200Ok.

        squads array  # noqa: E501

        :param squads: The squads of this GetFleetsFleetIdWings200Ok.  # noqa: E501
        :type: list[GetFleetsFleetIdWingsSquad]
        """
        if squads is None:
            raise ValueError("Invalid value for `squads`, must not be `None`")  # noqa: E501

        self._squads = squads

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
        if not isinstance(other, GetFleetsFleetIdWings200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
