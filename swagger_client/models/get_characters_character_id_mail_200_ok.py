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

from swagger_client.models.get_characters_character_id_mail_recipient import GetCharactersCharacterIdMailRecipient  # noqa: F401,E501


class GetCharactersCharacterIdMail200Ok(object):
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
        'mail_id': 'int',
        'subject': 'str',
        '_from': 'int',
        'timestamp': 'datetime',
        'labels': 'list[int]',
        'recipients': 'list[GetCharactersCharacterIdMailRecipient]',
        'is_read': 'bool'
    }

    attribute_map = {
        'mail_id': 'mail_id',
        'subject': 'subject',
        '_from': 'from',
        'timestamp': 'timestamp',
        'labels': 'labels',
        'recipients': 'recipients',
        'is_read': 'is_read'
    }

    def __init__(self, mail_id=None, subject=None, _from=None, timestamp=None, labels=None, recipients=None, is_read=None):  # noqa: E501
        """GetCharactersCharacterIdMail200Ok - a model defined in Swagger"""  # noqa: E501

        self._mail_id = None
        self._subject = None
        self.__from = None
        self._timestamp = None
        self._labels = None
        self._recipients = None
        self._is_read = None
        self.discriminator = None

        if mail_id is not None:
            self.mail_id = mail_id
        if subject is not None:
            self.subject = subject
        if _from is not None:
            self._from = _from
        if timestamp is not None:
            self.timestamp = timestamp
        if labels is not None:
            self.labels = labels
        if recipients is not None:
            self.recipients = recipients
        if is_read is not None:
            self.is_read = is_read

    @property
    def mail_id(self):
        """Gets the mail_id of this GetCharactersCharacterIdMail200Ok.  # noqa: E501

        mail_id integer  # noqa: E501

        :return: The mail_id of this GetCharactersCharacterIdMail200Ok.  # noqa: E501
        :rtype: int
        """
        return self._mail_id

    @mail_id.setter
    def mail_id(self, mail_id):
        """Sets the mail_id of this GetCharactersCharacterIdMail200Ok.

        mail_id integer  # noqa: E501

        :param mail_id: The mail_id of this GetCharactersCharacterIdMail200Ok.  # noqa: E501
        :type: int
        """

        self._mail_id = mail_id

    @property
    def subject(self):
        """Gets the subject of this GetCharactersCharacterIdMail200Ok.  # noqa: E501

        Mail subject  # noqa: E501

        :return: The subject of this GetCharactersCharacterIdMail200Ok.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this GetCharactersCharacterIdMail200Ok.

        Mail subject  # noqa: E501

        :param subject: The subject of this GetCharactersCharacterIdMail200Ok.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def _from(self):
        """Gets the _from of this GetCharactersCharacterIdMail200Ok.  # noqa: E501

        From whom the mail was sent  # noqa: E501

        :return: The _from of this GetCharactersCharacterIdMail200Ok.  # noqa: E501
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this GetCharactersCharacterIdMail200Ok.

        From whom the mail was sent  # noqa: E501

        :param _from: The _from of this GetCharactersCharacterIdMail200Ok.  # noqa: E501
        :type: int
        """

        self.__from = _from

    @property
    def timestamp(self):
        """Gets the timestamp of this GetCharactersCharacterIdMail200Ok.  # noqa: E501

        When the mail was sent  # noqa: E501

        :return: The timestamp of this GetCharactersCharacterIdMail200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this GetCharactersCharacterIdMail200Ok.

        When the mail was sent  # noqa: E501

        :param timestamp: The timestamp of this GetCharactersCharacterIdMail200Ok.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def labels(self):
        """Gets the labels of this GetCharactersCharacterIdMail200Ok.  # noqa: E501

        labels array  # noqa: E501

        :return: The labels of this GetCharactersCharacterIdMail200Ok.  # noqa: E501
        :rtype: list[int]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this GetCharactersCharacterIdMail200Ok.

        labels array  # noqa: E501

        :param labels: The labels of this GetCharactersCharacterIdMail200Ok.  # noqa: E501
        :type: list[int]
        """

        self._labels = labels

    @property
    def recipients(self):
        """Gets the recipients of this GetCharactersCharacterIdMail200Ok.  # noqa: E501

        Recipients of the mail  # noqa: E501

        :return: The recipients of this GetCharactersCharacterIdMail200Ok.  # noqa: E501
        :rtype: list[GetCharactersCharacterIdMailRecipient]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this GetCharactersCharacterIdMail200Ok.

        Recipients of the mail  # noqa: E501

        :param recipients: The recipients of this GetCharactersCharacterIdMail200Ok.  # noqa: E501
        :type: list[GetCharactersCharacterIdMailRecipient]
        """

        self._recipients = recipients

    @property
    def is_read(self):
        """Gets the is_read of this GetCharactersCharacterIdMail200Ok.  # noqa: E501

        is_read boolean  # noqa: E501

        :return: The is_read of this GetCharactersCharacterIdMail200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._is_read

    @is_read.setter
    def is_read(self, is_read):
        """Sets the is_read of this GetCharactersCharacterIdMail200Ok.

        is_read boolean  # noqa: E501

        :param is_read: The is_read of this GetCharactersCharacterIdMail200Ok.  # noqa: E501
        :type: bool
        """

        self._is_read = is_read

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
        if not isinstance(other, GetCharactersCharacterIdMail200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
