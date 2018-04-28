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


class PostFleetsFleetIdMembersInvitation(object):
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
        'character_id': 'int',
        'role': 'str',
        'wing_id': 'int',
        'squad_id': 'int'
    }

    attribute_map = {
        'character_id': 'character_id',
        'role': 'role',
        'wing_id': 'wing_id',
        'squad_id': 'squad_id'
    }

    def __init__(self, character_id=None, role=None, wing_id=None, squad_id=None):  # noqa: E501
        """PostFleetsFleetIdMembersInvitation - a model defined in Swagger"""  # noqa: E501

        self._character_id = None
        self._role = None
        self._wing_id = None
        self._squad_id = None
        self.discriminator = None

        self.character_id = character_id
        self.role = role
        if wing_id is not None:
            self.wing_id = wing_id
        if squad_id is not None:
            self.squad_id = squad_id

    @property
    def character_id(self):
        """Gets the character_id of this PostFleetsFleetIdMembersInvitation.  # noqa: E501

        The character you want to invite  # noqa: E501

        :return: The character_id of this PostFleetsFleetIdMembersInvitation.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this PostFleetsFleetIdMembersInvitation.

        The character you want to invite  # noqa: E501

        :param character_id: The character_id of this PostFleetsFleetIdMembersInvitation.  # noqa: E501
        :type: int
        """
        if character_id is None:
            raise ValueError("Invalid value for `character_id`, must not be `None`")  # noqa: E501

        self._character_id = character_id

    @property
    def role(self):
        """Gets the role of this PostFleetsFleetIdMembersInvitation.  # noqa: E501

        If a character is invited with the `fleet_commander` role, neither `wing_id` or `squad_id` should be specified. If a character is invited with the `wing_commander` role, only `wing_id` should be specified. If a character is invited with the `squad_commander` role, both `wing_id` and `squad_id` should be specified. If a character is invited with the `squad_member` role, `wing_id` and `squad_id` should either both be specified or not specified at all. If they aren’t specified, the invited character will join any squad with available positions.  # noqa: E501

        :return: The role of this PostFleetsFleetIdMembersInvitation.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this PostFleetsFleetIdMembersInvitation.

        If a character is invited with the `fleet_commander` role, neither `wing_id` or `squad_id` should be specified. If a character is invited with the `wing_commander` role, only `wing_id` should be specified. If a character is invited with the `squad_commander` role, both `wing_id` and `squad_id` should be specified. If a character is invited with the `squad_member` role, `wing_id` and `squad_id` should either both be specified or not specified at all. If they aren’t specified, the invited character will join any squad with available positions.  # noqa: E501

        :param role: The role of this PostFleetsFleetIdMembersInvitation.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["fleet_commander", "wing_commander", "squad_commander", "squad_member"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def wing_id(self):
        """Gets the wing_id of this PostFleetsFleetIdMembersInvitation.  # noqa: E501

        wing_id integer  # noqa: E501

        :return: The wing_id of this PostFleetsFleetIdMembersInvitation.  # noqa: E501
        :rtype: int
        """
        return self._wing_id

    @wing_id.setter
    def wing_id(self, wing_id):
        """Sets the wing_id of this PostFleetsFleetIdMembersInvitation.

        wing_id integer  # noqa: E501

        :param wing_id: The wing_id of this PostFleetsFleetIdMembersInvitation.  # noqa: E501
        :type: int
        """
        if wing_id is not None and wing_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `wing_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._wing_id = wing_id

    @property
    def squad_id(self):
        """Gets the squad_id of this PostFleetsFleetIdMembersInvitation.  # noqa: E501

        squad_id integer  # noqa: E501

        :return: The squad_id of this PostFleetsFleetIdMembersInvitation.  # noqa: E501
        :rtype: int
        """
        return self._squad_id

    @squad_id.setter
    def squad_id(self, squad_id):
        """Sets the squad_id of this PostFleetsFleetIdMembersInvitation.

        squad_id integer  # noqa: E501

        :param squad_id: The squad_id of this PostFleetsFleetIdMembersInvitation.  # noqa: E501
        :type: int
        """
        if squad_id is not None and squad_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `squad_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._squad_id = squad_id

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
        if not isinstance(other, PostFleetsFleetIdMembersInvitation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
