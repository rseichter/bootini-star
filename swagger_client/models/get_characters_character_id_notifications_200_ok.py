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


class GetCharactersCharacterIdNotifications200Ok(object):
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
        'notification_id': 'int',
        'sender_id': 'int',
        'sender_type': 'str',
        'timestamp': 'datetime',
        'is_read': 'bool',
        'text': 'str',
        'type': 'str'
    }

    attribute_map = {
        'notification_id': 'notification_id',
        'sender_id': 'sender_id',
        'sender_type': 'sender_type',
        'timestamp': 'timestamp',
        'is_read': 'is_read',
        'text': 'text',
        'type': 'type'
    }

    def __init__(self, notification_id=None, sender_id=None, sender_type=None, timestamp=None, is_read=None, text=None, type=None):  # noqa: E501
        """GetCharactersCharacterIdNotifications200Ok - a model defined in Swagger"""  # noqa: E501

        self._notification_id = None
        self._sender_id = None
        self._sender_type = None
        self._timestamp = None
        self._is_read = None
        self._text = None
        self._type = None
        self.discriminator = None

        self.notification_id = notification_id
        self.sender_id = sender_id
        self.sender_type = sender_type
        self.timestamp = timestamp
        if is_read is not None:
            self.is_read = is_read
        if text is not None:
            self.text = text
        self.type = type

    @property
    def notification_id(self):
        """Gets the notification_id of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501

        notification_id integer  # noqa: E501

        :return: The notification_id of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501
        :rtype: int
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        """Sets the notification_id of this GetCharactersCharacterIdNotifications200Ok.

        notification_id integer  # noqa: E501

        :param notification_id: The notification_id of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501
        :type: int
        """
        if notification_id is None:
            raise ValueError("Invalid value for `notification_id`, must not be `None`")  # noqa: E501

        self._notification_id = notification_id

    @property
    def sender_id(self):
        """Gets the sender_id of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501

        sender_id integer  # noqa: E501

        :return: The sender_id of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501
        :rtype: int
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        """Sets the sender_id of this GetCharactersCharacterIdNotifications200Ok.

        sender_id integer  # noqa: E501

        :param sender_id: The sender_id of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501
        :type: int
        """
        if sender_id is None:
            raise ValueError("Invalid value for `sender_id`, must not be `None`")  # noqa: E501

        self._sender_id = sender_id

    @property
    def sender_type(self):
        """Gets the sender_type of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501

        sender_type string  # noqa: E501

        :return: The sender_type of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501
        :rtype: str
        """
        return self._sender_type

    @sender_type.setter
    def sender_type(self, sender_type):
        """Sets the sender_type of this GetCharactersCharacterIdNotifications200Ok.

        sender_type string  # noqa: E501

        :param sender_type: The sender_type of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501
        :type: str
        """
        if sender_type is None:
            raise ValueError("Invalid value for `sender_type`, must not be `None`")  # noqa: E501
        allowed_values = ["character", "corporation", "alliance", "faction", "other"]  # noqa: E501
        if sender_type not in allowed_values:
            raise ValueError(
                "Invalid value for `sender_type` ({0}), must be one of {1}"  # noqa: E501
                .format(sender_type, allowed_values)
            )

        self._sender_type = sender_type

    @property
    def timestamp(self):
        """Gets the timestamp of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501

        timestamp string  # noqa: E501

        :return: The timestamp of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this GetCharactersCharacterIdNotifications200Ok.

        timestamp string  # noqa: E501

        :param timestamp: The timestamp of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def is_read(self):
        """Gets the is_read of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501

        is_read boolean  # noqa: E501

        :return: The is_read of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._is_read

    @is_read.setter
    def is_read(self, is_read):
        """Sets the is_read of this GetCharactersCharacterIdNotifications200Ok.

        is_read boolean  # noqa: E501

        :param is_read: The is_read of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501
        :type: bool
        """

        self._is_read = is_read

    @property
    def text(self):
        """Gets the text of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501

        text string  # noqa: E501

        :return: The text of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this GetCharactersCharacterIdNotifications200Ok.

        text string  # noqa: E501

        :param text: The text of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def type(self):
        """Gets the type of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501

        type string  # noqa: E501

        :return: The type of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetCharactersCharacterIdNotifications200Ok.

        type string  # noqa: E501

        :param type: The type of this GetCharactersCharacterIdNotifications200Ok.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["AcceptedAlly", "AcceptedSurrender", "AllAnchoringMsg", "AllMaintenanceBillMsg", "AllStrucInvulnerableMsg", "AllStructVulnerableMsg", "AllWarCorpJoinedAllianceMsg", "AllWarDeclaredMsg", "AllWarInvalidatedMsg", "AllWarRetractedMsg", "AllWarSurrenderMsg", "AllianceCapitalChanged", "AllyContractCancelled", "AllyJoinedWarAggressorMsg", "AllyJoinedWarAllyMsg", "AllyJoinedWarDefenderMsg", "BattlePunishFriendlyFire", "BillOutOfMoneyMsg", "BillPaidCorpAllMsg", "BountyClaimMsg", "BountyESSShared", "BountyESSTaken", "BountyPlacedAlliance", "BountyPlacedChar", "BountyPlacedCorp", "BountyYourBountyClaimed", "BuddyConnectContactAdd", "CharAppAcceptMsg", "CharAppRejectMsg", "CharAppWithdrawMsg", "CharLeftCorpMsg", "CharMedalMsg", "CharTerminationMsg", "CloneActivationMsg", "CloneActivationMsg2", "CloneMovedMsg", "CloneRevokedMsg1", "CloneRevokedMsg2", "ContactAdd", "ContactEdit", "ContainerPasswordMsg", "CorpAllBillMsg", "CorpAppAcceptMsg", "CorpAppInvitedMsg", "CorpAppNewMsg", "CorpAppRejectCustomMsg", "CorpAppRejectMsg", "CorpDividendMsg", "CorpFriendlyFireDisableTimerCompleted", "CorpFriendlyFireDisableTimerStarted", "CorpFriendlyFireEnableTimerCompleted", "CorpFriendlyFireEnableTimerStarted", "CorpKicked", "CorpLiquidationMsg", "CorpNewCEOMsg", "CorpNewsMsg", "CorpOfficeExpirationMsg", "CorpStructLostMsg", "CorpTaxChangeMsg", "CorpVoteCEORevokedMsg", "CorpVoteMsg", "CorpWarDeclaredMsg", "CorpWarFightingLegalMsg", "CorpWarInvalidatedMsg", "CorpWarRetractedMsg", "CorpWarSurrenderMsg", "CustomsMsg", "DeclareWar", "DistrictAttacked", "DustAppAcceptedMsg", "EntosisCaptureStarted", "FWAllianceKickMsg", "FWAllianceWarningMsg", "FWCharKickMsg", "FWCharRankGainMsg", "FWCharRankLossMsg", "FWCharWarningMsg", "FWCorpJoinMsg", "FWCorpKickMsg", "FWCorpLeaveMsg", "FWCorpWarningMsg", "FacWarCorpJoinRequestMsg", "FacWarCorpJoinWithdrawMsg", "FacWarCorpLeaveRequestMsg", "FacWarCorpLeaveWithdrawMsg", "FacWarLPDisqualifiedEvent", "FacWarLPDisqualifiedKill", "FacWarLPPayoutEvent", "FacWarLPPayoutKill", "GameTimeAdded", "GameTimeReceived", "GameTimeSent", "GiftReceived", "IHubDestroyedByBillFailure", "IncursionCompletedMsg", "IndustryTeamAuctionLost", "IndustryTeamAuctionWon", "InfrastructureHubBillAboutToExpire", "InsuranceExpirationMsg", "InsuranceFirstShipMsg", "InsuranceInvalidatedMsg", "InsuranceIssuedMsg", "InsurancePayoutMsg", "JumpCloneDeletedMsg1", "JumpCloneDeletedMsg2", "KillReportFinalBlow", "KillReportVictim", "KillRightAvailable", "KillRightAvailableOpen", "KillRightEarned", "KillRightUnavailable", "KillRightUnavailableOpen", "KillRightUsed", "LocateCharMsg", "MadeWarMutual", "MercOfferedNegotiationMsg", "MissionOfferExpirationMsg", "MissionTimeoutMsg", "MoonminingAutomaticFracture", "MoonminingExtractionCancelled", "MoonminingExtractionFinished", "MoonminingExtractionStarted", "MoonminingLaserFired", "NPCStandingsGained", "NPCStandingsLost", "OfferedSurrender", "OfferedToAlly", "OldLscMessages", "OperationFinished", "OrbitalAttacked", "OrbitalReinforced", "OwnershipTransferred", "ReimbursementMsg", "ResearchMissionAvailableMsg", "RetractsWar", "SeasonalChallengeCompleted", "SovAllClaimAquiredMsg", "SovAllClaimLostMsg", "SovCommandNodeEventStarted", "SovCorpBillLateMsg", "SovCorpClaimFailMsg", "SovDisruptorMsg", "SovStationEnteredFreeport", "SovStructureDestroyed", "SovStructureReinforced", "SovStructureSelfDestructCancel", "SovStructureSelfDestructFinished", "SovStructureSelfDestructRequested", "SovereigntyIHDamageMsg", "SovereigntySBUDamageMsg", "SovereigntyTCUDamageMsg", "StationAggressionMsg1", "StationAggressionMsg2", "StationConquerMsg", "StationServiceDisabled", "StationServiceEnabled", "StationStateChangeMsg", "StoryLineMissionAvailableMsg", "StructureAnchoring", "StructureCourierContractChanged", "StructureDestroyed", "StructureFuelAlert", "StructureItemsDelivered", "StructureLostArmor", "StructureLostShields", "StructureOnline", "StructureServicesOffline", "StructureUnanchoring", "StructureUnderAttack", "StructureWentHighPower", "StructureWentLowPower", "StructuresReinforcementChanged", "TowerAlertMsg", "TowerResourceAlertMsg", "TransactionReversalMsg", "TutorialMsg", "WarAllyOfferDeclinedMsg", "WarSurrenderDeclinedMsg", "WarSurrenderOfferMsg"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, GetCharactersCharacterIdNotifications200Ok):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
