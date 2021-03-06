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


class GetMarketsRegionIdOrders200Ok(object):
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
        'order_id': 'int',
        'type_id': 'int',
        'location_id': 'int',
        'system_id': 'int',
        'volume_total': 'int',
        'volume_remain': 'int',
        'min_volume': 'int',
        'price': 'float',
        'is_buy_order': 'bool',
        'duration': 'int',
        'issued': 'datetime',
        'range': 'str'
    }

    attribute_map = {
        'order_id': 'order_id',
        'type_id': 'type_id',
        'location_id': 'location_id',
        'system_id': 'system_id',
        'volume_total': 'volume_total',
        'volume_remain': 'volume_remain',
        'min_volume': 'min_volume',
        'price': 'price',
        'is_buy_order': 'is_buy_order',
        'duration': 'duration',
        'issued': 'issued',
        'range': 'range'
    }

    def __init__(self, order_id=None, type_id=None, location_id=None, system_id=None, volume_total=None, volume_remain=None, min_volume=None, price=None, is_buy_order=None, duration=None, issued=None, range=None):  # noqa: E501
        """GetMarketsRegionIdOrders200Ok - a model defined in Swagger"""  # noqa: E501

        self._order_id = None
        self._type_id = None
        self._location_id = None
        self._system_id = None
        self._volume_total = None
        self._volume_remain = None
        self._min_volume = None
        self._price = None
        self._is_buy_order = None
        self._duration = None
        self._issued = None
        self._range = None
        self.discriminator = None

        self.order_id = order_id
        self.type_id = type_id
        self.location_id = location_id
        self.system_id = system_id
        self.volume_total = volume_total
        self.volume_remain = volume_remain
        self.min_volume = min_volume
        self.price = price
        self.is_buy_order = is_buy_order
        self.duration = duration
        self.issued = issued
        self.range = range

    @property
    def order_id(self):
        """Gets the order_id of this GetMarketsRegionIdOrders200Ok.  # noqa: E501

        order_id integer  # noqa: E501

        :return: The order_id of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this GetMarketsRegionIdOrders200Ok.

        order_id integer  # noqa: E501

        :param order_id: The order_id of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def type_id(self):
        """Gets the type_id of this GetMarketsRegionIdOrders200Ok.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetMarketsRegionIdOrders200Ok.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

    @property
    def location_id(self):
        """Gets the location_id of this GetMarketsRegionIdOrders200Ok.  # noqa: E501

        location_id integer  # noqa: E501

        :return: The location_id of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this GetMarketsRegionIdOrders200Ok.

        location_id integer  # noqa: E501

        :param location_id: The location_id of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def system_id(self):
        """Gets the system_id of this GetMarketsRegionIdOrders200Ok.  # noqa: E501

        The solar system this order was placed  # noqa: E501

        :return: The system_id of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this GetMarketsRegionIdOrders200Ok.

        The solar system this order was placed  # noqa: E501

        :param system_id: The system_id of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")  # noqa: E501

        self._system_id = system_id

    @property
    def volume_total(self):
        """Gets the volume_total of this GetMarketsRegionIdOrders200Ok.  # noqa: E501

        volume_total integer  # noqa: E501

        :return: The volume_total of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._volume_total

    @volume_total.setter
    def volume_total(self, volume_total):
        """Sets the volume_total of this GetMarketsRegionIdOrders200Ok.

        volume_total integer  # noqa: E501

        :param volume_total: The volume_total of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if volume_total is None:
            raise ValueError("Invalid value for `volume_total`, must not be `None`")  # noqa: E501

        self._volume_total = volume_total

    @property
    def volume_remain(self):
        """Gets the volume_remain of this GetMarketsRegionIdOrders200Ok.  # noqa: E501

        volume_remain integer  # noqa: E501

        :return: The volume_remain of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._volume_remain

    @volume_remain.setter
    def volume_remain(self, volume_remain):
        """Sets the volume_remain of this GetMarketsRegionIdOrders200Ok.

        volume_remain integer  # noqa: E501

        :param volume_remain: The volume_remain of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if volume_remain is None:
            raise ValueError("Invalid value for `volume_remain`, must not be `None`")  # noqa: E501

        self._volume_remain = volume_remain

    @property
    def min_volume(self):
        """Gets the min_volume of this GetMarketsRegionIdOrders200Ok.  # noqa: E501

        min_volume integer  # noqa: E501

        :return: The min_volume of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._min_volume

    @min_volume.setter
    def min_volume(self, min_volume):
        """Sets the min_volume of this GetMarketsRegionIdOrders200Ok.

        min_volume integer  # noqa: E501

        :param min_volume: The min_volume of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if min_volume is None:
            raise ValueError("Invalid value for `min_volume`, must not be `None`")  # noqa: E501

        self._min_volume = min_volume

    @property
    def price(self):
        """Gets the price of this GetMarketsRegionIdOrders200Ok.  # noqa: E501

        price number  # noqa: E501

        :return: The price of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this GetMarketsRegionIdOrders200Ok.

        price number  # noqa: E501

        :param price: The price of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def is_buy_order(self):
        """Gets the is_buy_order of this GetMarketsRegionIdOrders200Ok.  # noqa: E501

        is_buy_order boolean  # noqa: E501

        :return: The is_buy_order of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._is_buy_order

    @is_buy_order.setter
    def is_buy_order(self, is_buy_order):
        """Sets the is_buy_order of this GetMarketsRegionIdOrders200Ok.

        is_buy_order boolean  # noqa: E501

        :param is_buy_order: The is_buy_order of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :type: bool
        """
        if is_buy_order is None:
            raise ValueError("Invalid value for `is_buy_order`, must not be `None`")  # noqa: E501

        self._is_buy_order = is_buy_order

    @property
    def duration(self):
        """Gets the duration of this GetMarketsRegionIdOrders200Ok.  # noqa: E501

        duration integer  # noqa: E501

        :return: The duration of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this GetMarketsRegionIdOrders200Ok.

        duration integer  # noqa: E501

        :param duration: The duration of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :type: int
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def issued(self):
        """Gets the issued of this GetMarketsRegionIdOrders200Ok.  # noqa: E501

        issued string  # noqa: E501

        :return: The issued of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._issued

    @issued.setter
    def issued(self, issued):
        """Sets the issued of this GetMarketsRegionIdOrders200Ok.

        issued string  # noqa: E501

        :param issued: The issued of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :type: datetime
        """
        if issued is None:
            raise ValueError("Invalid value for `issued`, must not be `None`")  # noqa: E501

        self._issued = issued

    @property
    def range(self):
        """Gets the range of this GetMarketsRegionIdOrders200Ok.  # noqa: E501

        range string  # noqa: E501

        :return: The range of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this GetMarketsRegionIdOrders200Ok.

        range string  # noqa: E501

        :param range: The range of this GetMarketsRegionIdOrders200Ok.  # noqa: E501
        :type: str
        """
        if range is None:
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501
        allowed_values = ["station", "region", "solarsystem", "1", "2", "3", "4", "5", "10", "20", "30", "40"]  # noqa: E501
        if range not in allowed_values:
            raise ValueError(
                "Invalid value for `range` ({0}), must be one of {1}"  # noqa: E501
                .format(range, allowed_values)
            )

        self._range = range

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
        if not isinstance(other, GetMarketsRegionIdOrders200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
