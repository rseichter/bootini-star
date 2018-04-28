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


class Forbidden(object):
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
        'error': 'str',
        'sso_status': 'int'
    }

    attribute_map = {
        'error': 'error',
        'sso_status': 'sso_status'
    }

    def __init__(self, error=None, sso_status=None):  # noqa: E501
        """Forbidden - a model defined in Swagger"""  # noqa: E501

        self._error = None
        self._sso_status = None
        self.discriminator = None

        self.error = error
        if sso_status is not None:
            self.sso_status = sso_status

    @property
    def error(self):
        """Gets the error of this Forbidden.  # noqa: E501

        Forbidden message  # noqa: E501

        :return: The error of this Forbidden.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Forbidden.

        Forbidden message  # noqa: E501

        :param error: The error of this Forbidden.  # noqa: E501
        :type: str
        """
        if error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

    @property
    def sso_status(self):
        """Gets the sso_status of this Forbidden.  # noqa: E501

        Status code received from SSO  # noqa: E501

        :return: The sso_status of this Forbidden.  # noqa: E501
        :rtype: int
        """
        return self._sso_status

    @sso_status.setter
    def sso_status(self, sso_status):
        """Sets the sso_status of this Forbidden.

        Status code received from SSO  # noqa: E501

        :param sso_status: The sso_status of this Forbidden.  # noqa: E501
        :type: int
        """

        self._sso_status = sso_status

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
        if not isinstance(other, Forbidden):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
