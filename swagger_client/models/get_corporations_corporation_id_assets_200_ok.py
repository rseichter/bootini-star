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


class GetCorporationsCorporationIdAssets200Ok(object):
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
        'type_id': 'int',
        'quantity': 'int',
        'location_id': 'int',
        'location_type': 'str',
        'item_id': 'int',
        'is_singleton': 'bool',
        'location_flag': 'str'
    }

    attribute_map = {
        'type_id': 'type_id',
        'quantity': 'quantity',
        'location_id': 'location_id',
        'location_type': 'location_type',
        'item_id': 'item_id',
        'is_singleton': 'is_singleton',
        'location_flag': 'location_flag'
    }

    def __init__(self, type_id=None, quantity=None, location_id=None, location_type=None, item_id=None, is_singleton=None, location_flag=None):  # noqa: E501
        """GetCorporationsCorporationIdAssets200Ok - a model defined in Swagger"""  # noqa: E501

        self._type_id = None
        self._quantity = None
        self._location_id = None
        self._location_type = None
        self._item_id = None
        self._is_singleton = None
        self._location_flag = None
        self.discriminator = None

        self.type_id = type_id
        self.quantity = quantity
        self.location_id = location_id
        self.location_type = location_type
        self.item_id = item_id
        self.is_singleton = is_singleton
        self.location_flag = location_flag

    @property
    def type_id(self):
        """Gets the type_id of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetCorporationsCorporationIdAssets200Ok.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501
        :type: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

    @property
    def quantity(self):
        """Gets the quantity of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501

        quantity integer  # noqa: E501

        :return: The quantity of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this GetCorporationsCorporationIdAssets200Ok.

        quantity integer  # noqa: E501

        :param quantity: The quantity of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def location_id(self):
        """Gets the location_id of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501

        location_id integer  # noqa: E501

        :return: The location_id of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this GetCorporationsCorporationIdAssets200Ok.

        location_id integer  # noqa: E501

        :param location_id: The location_id of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501
        :type: int
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def location_type(self):
        """Gets the location_type of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501

        location_type string  # noqa: E501

        :return: The location_type of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501
        :rtype: str
        """
        return self._location_type

    @location_type.setter
    def location_type(self, location_type):
        """Sets the location_type of this GetCorporationsCorporationIdAssets200Ok.

        location_type string  # noqa: E501

        :param location_type: The location_type of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501
        :type: str
        """
        if location_type is None:
            raise ValueError("Invalid value for `location_type`, must not be `None`")  # noqa: E501
        allowed_values = ["station", "solar_system", "other"]  # noqa: E501
        if location_type not in allowed_values:
            raise ValueError(
                "Invalid value for `location_type` ({0}), must be one of {1}"  # noqa: E501
                .format(location_type, allowed_values)
            )

        self._location_type = location_type

    @property
    def item_id(self):
        """Gets the item_id of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501

        item_id integer  # noqa: E501

        :return: The item_id of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this GetCorporationsCorporationIdAssets200Ok.

        item_id integer  # noqa: E501

        :param item_id: The item_id of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501
        :type: int
        """
        if item_id is None:
            raise ValueError("Invalid value for `item_id`, must not be `None`")  # noqa: E501

        self._item_id = item_id

    @property
    def is_singleton(self):
        """Gets the is_singleton of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501

        is_singleton boolean  # noqa: E501

        :return: The is_singleton of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._is_singleton

    @is_singleton.setter
    def is_singleton(self, is_singleton):
        """Sets the is_singleton of this GetCorporationsCorporationIdAssets200Ok.

        is_singleton boolean  # noqa: E501

        :param is_singleton: The is_singleton of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501
        :type: bool
        """
        if is_singleton is None:
            raise ValueError("Invalid value for `is_singleton`, must not be `None`")  # noqa: E501

        self._is_singleton = is_singleton

    @property
    def location_flag(self):
        """Gets the location_flag of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501

        location_flag string  # noqa: E501

        :return: The location_flag of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501
        :rtype: str
        """
        return self._location_flag

    @location_flag.setter
    def location_flag(self, location_flag):
        """Sets the location_flag of this GetCorporationsCorporationIdAssets200Ok.

        location_flag string  # noqa: E501

        :param location_flag: The location_flag of this GetCorporationsCorporationIdAssets200Ok.  # noqa: E501
        :type: str
        """
        if location_flag is None:
            raise ValueError("Invalid value for `location_flag`, must not be `None`")  # noqa: E501
        allowed_values = ["AssetSafety", "AutoFit", "Bonus", "Booster", "BoosterBay", "Capsule", "Cargo", "CorpDeliveries", "CorpSAG1", "CorpSAG2", "CorpSAG3", "CorpSAG4", "CorpSAG5", "CorpSAG6", "CorpSAG7", "CrateLoot", "Deliveries", "DroneBay", "DustBattle", "DustDatabank", "FighterBay", "FighterTube0", "FighterTube1", "FighterTube2", "FighterTube3", "FighterTube4", "FleetHangar", "Hangar", "HangarAll", "HiSlot0", "HiSlot1", "HiSlot2", "HiSlot3", "HiSlot4", "HiSlot5", "HiSlot6", "HiSlot7", "HiddenModifiers", "Implant", "Impounded", "JunkyardReprocessed", "JunkyardTrashed", "LoSlot0", "LoSlot1", "LoSlot2", "LoSlot3", "LoSlot4", "LoSlot5", "LoSlot6", "LoSlot7", "Locked", "MedSlot0", "MedSlot1", "MedSlot2", "MedSlot3", "MedSlot4", "MedSlot5", "MedSlot6", "MedSlot7", "OfficeFolder", "Pilot", "PlanetSurface", "QuafeBay", "Reward", "RigSlot0", "RigSlot1", "RigSlot2", "RigSlot3", "RigSlot4", "RigSlot5", "RigSlot6", "RigSlot7", "SecondaryStorage", "ServiceSlot0", "ServiceSlot1", "ServiceSlot2", "ServiceSlot3", "ServiceSlot4", "ServiceSlot5", "ServiceSlot6", "ServiceSlot7", "ShipHangar", "ShipOffline", "Skill", "SkillInTraining", "SpecializedAmmoHold", "SpecializedCommandCenterHold", "SpecializedFuelBay", "SpecializedGasHold", "SpecializedIndustrialShipHold", "SpecializedLargeShipHold", "SpecializedMaterialBay", "SpecializedMediumShipHold", "SpecializedMineralHold", "SpecializedOreHold", "SpecializedPlanetaryCommoditiesHold", "SpecializedSalvageHold", "SpecializedShipHold", "SpecializedSmallShipHold", "StructureActive", "StructureFuel", "StructureInactive", "StructureOffline", "SubSystemBay", "SubSystemSlot0", "SubSystemSlot1", "SubSystemSlot2", "SubSystemSlot3", "SubSystemSlot4", "SubSystemSlot5", "SubSystemSlot6", "SubSystemSlot7", "Unlocked", "Wallet", "Wardrobe"]  # noqa: E501
        if location_flag not in allowed_values:
            raise ValueError(
                "Invalid value for `location_flag` ({0}), must be one of {1}"  # noqa: E501
                .format(location_flag, allowed_values)
            )

        self._location_flag = location_flag

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
        if not isinstance(other, GetCorporationsCorporationIdAssets200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other