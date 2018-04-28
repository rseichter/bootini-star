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


class GetCharactersCharacterIdCorporationhistory200Ok(object):
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
        'start_date': 'datetime',
        'corporation_id': 'int',
        'is_deleted': 'bool',
        'record_id': 'int'
    }

    attribute_map = {
        'start_date': 'start_date',
        'corporation_id': 'corporation_id',
        'is_deleted': 'is_deleted',
        'record_id': 'record_id'
    }

    def __init__(self, start_date=None, corporation_id=None, is_deleted=None, record_id=None):  # noqa: E501
        """GetCharactersCharacterIdCorporationhistory200Ok - a model defined in Swagger"""  # noqa: E501

        self._start_date = None
        self._corporation_id = None
        self._is_deleted = None
        self._record_id = None
        self.discriminator = None

        self.start_date = start_date
        self.corporation_id = corporation_id
        if is_deleted is not None:
            self.is_deleted = is_deleted
        self.record_id = record_id

    @property
    def start_date(self):
        """Gets the start_date of this GetCharactersCharacterIdCorporationhistory200Ok.  # noqa: E501

        start_date string  # noqa: E501

        :return: The start_date of this GetCharactersCharacterIdCorporationhistory200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this GetCharactersCharacterIdCorporationhistory200Ok.

        start_date string  # noqa: E501

        :param start_date: The start_date of this GetCharactersCharacterIdCorporationhistory200Ok.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def corporation_id(self):
        """Gets the corporation_id of this GetCharactersCharacterIdCorporationhistory200Ok.  # noqa: E501

        corporation_id integer  # noqa: E501

        :return: The corporation_id of this GetCharactersCharacterIdCorporationhistory200Ok.  # noqa: E501
        :rtype: int
        """
        return self._corporation_id

    @corporation_id.setter
    def corporation_id(self, corporation_id):
        """Sets the corporation_id of this GetCharactersCharacterIdCorporationhistory200Ok.

        corporation_id integer  # noqa: E501

        :param corporation_id: The corporation_id of this GetCharactersCharacterIdCorporationhistory200Ok.  # noqa: E501
        :type: int
        """
        if corporation_id is None:
            raise ValueError("Invalid value for `corporation_id`, must not be `None`")  # noqa: E501

        self._corporation_id = corporation_id

    @property
    def is_deleted(self):
        """Gets the is_deleted of this GetCharactersCharacterIdCorporationhistory200Ok.  # noqa: E501

        True if the corporation has been deleted  # noqa: E501

        :return: The is_deleted of this GetCharactersCharacterIdCorporationhistory200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this GetCharactersCharacterIdCorporationhistory200Ok.

        True if the corporation has been deleted  # noqa: E501

        :param is_deleted: The is_deleted of this GetCharactersCharacterIdCorporationhistory200Ok.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def record_id(self):
        """Gets the record_id of this GetCharactersCharacterIdCorporationhistory200Ok.  # noqa: E501

        An incrementing ID that can be used to canonically establish order of records in cases where dates may be ambiguous  # noqa: E501

        :return: The record_id of this GetCharactersCharacterIdCorporationhistory200Ok.  # noqa: E501
        :rtype: int
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this GetCharactersCharacterIdCorporationhistory200Ok.

        An incrementing ID that can be used to canonically establish order of records in cases where dates may be ambiguous  # noqa: E501

        :param record_id: The record_id of this GetCharactersCharacterIdCorporationhistory200Ok.  # noqa: E501
        :type: int
        """
        if record_id is None:
            raise ValueError("Invalid value for `record_id`, must not be `None`")  # noqa: E501

        self._record_id = record_id

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
        if not isinstance(other, GetCharactersCharacterIdCorporationhistory200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other