"""
Classes in this module are used to cache EVE Swagger Interface calls and static
database entries like EVE item groups and types.
"""
__author__ = 'Ralph Seichter'

from typing import List, Optional, Set

from sqlalchemy import BigInteger, Column, ForeignKey, String, Text
from sqlalchemy.orm import relationship

from swagger_client import CharacterApi, MailApi
from swagger_client import GetCharactersCharacterIdMail200Ok
from swagger_client import GetCharactersCharacterIdMailLabelsOk
from swagger_client import GetCharactersCharacterIdMailLists200Ok
from swagger_client import GetCharactersCharacterIdOk
from swagger_client import PutCharactersCharacterIdMailMailIdContents
from .extensions import db, log


class EveGroup(db.Model):
    """
    EVE Online type groups.

    This is static data held in the database. Objects should only be read,
    not manually constructed.
    """
    __tablename__ = "groups"
    id = Column(BigInteger, primary_key=True, autoincrement=False)
    name = Column(Text)
    eve_types = relationship('EveType', backref='group', lazy=True)


class EveType(db.Model):
    """
    EVE Online types. Each type belongs to a group.

    This is static data held in the database. Objects should only be read,
    not manually constructed.
    """
    __tablename__ = "types"
    id = Column(BigInteger, primary_key=True, autoincrement=False)
    groupid = Column(BigInteger, ForeignKey('groups.id'), nullable=False)
    name = Column(Text)
    description = Column(Text)


class Cache(db.Model):
    """Cache ID-name pairs."""
    __tablename__ = "cache"
    id = Column(BigInteger, primary_key=True, autoincrement=False)
    name = Column(String(256), nullable=False)

    def __init__(self, entry_id, name):
        self.id = entry_id
        self.name = name


class CacheBase:
    """Base class for handling Cache objects."""

    @staticmethod
    def get_cached(entry_id) -> Optional[Cache]:
        """
        Get an entry from the cache

        :type entry_id: int
        :param entry_id: Entry ID to search
        :return: Entry if present, None otherwise.
        """
        ce = Cache.query.filter_by(id=entry_id).first()
        if ce:
            log.debug(f'Found ID {entry_id} in cache')
            return ce
        return None

    @staticmethod
    def add(entry_id: int, entry_name: str) -> Cache:
        """
        Add an entry to the cache.

        :param entry_id: Entry identifier
        :param entry_name: User-visible name of the entry
        :rtype: Cache object
        """
        ce = Cache(entry_id, entry_name)
        log.debug(f'Adding ID {entry_id} to cache')
        db.session.add(ce)
        db.session.commit()
        return ce


class IdNameCache(CacheBase):
    """Cache for both ID-name-pairs and EVE types."""

    def eve_character(self, char_id) -> Cache:
        """
        Return the EVE character for a given character ID.

        :type char_id: int
        :param char_id: Character ID used for lookup
        """
        ce = self.get_cached(char_id)
        if ce:
            return ce
        api = CharacterApi()
        log.debug(f'Querying ESI for character {char_id}')
        rv = api.get_characters_character_id(char_id)
        return self.add(char_id, rv.name)

    def eve_characters(self, char_ids: Set[int]) -> Set[Cache]:
        """
        Return the EVE characters for a given list of character IDs.

        :type char_ids: Set[int]
        :param char_ids: Set of Character IDs used for lookup
        """
        characters = set()
        unknown = list()
        for char_id in char_ids:
            character = self.get_cached(char_id)
            if character:
                characters.add(character)
            else:
                unknown.append(char_id)
        if unknown:
            log.debug(f'Querying ESI for characters {unknown}')
            for c in CharacterApi().get_characters_names(unknown):
                characters.add(self.add(c.character_id, c.character_name))
        return characters

    @staticmethod
    def eve_type(type_id) -> EveType:
        """
        Return the EVE type for a given ID.

        :type type_id: int
        :param type_id: EVE type ID used for lookup
        """
        log.debug(f'Querying DB for EVE type {type_id}')
        return EveType.query.filter_by(id=type_id).one()


def get_mail_labels(api: MailApi,
                    character_id: int) -> GetCharactersCharacterIdMailLabelsOk:
    """
    Returns the mail labels and unread counts for a character.

    :param api: Mail API
    :param character_id: Character ID
    """
    log.debug(f'get_mail_labels {character_id}')
    return api.get_characters_character_id_mail_labels(character_id)


def get_mails(api: MailApi, character_id: int, **kwargs) -> List[
        GetCharactersCharacterIdMail200Ok]:
    """
    Returns the latest 50 email headers for a character.

    :param api: Mail API
    :param character_id: Character ID
    """
    log.debug(f'get_mails {character_id}')
    return api.get_characters_character_id_mail(character_id, **kwargs)


def get_mail_lists(api: MailApi, character_id: int) -> List[GetCharactersCharacterIdMailLists200Ok]:
    """
    Returns the mailing list subscriptions for a character.

    :param api: Mail API
    :param character_id: Character ID
    """
    log.debug(f'get_mail_lists {character_id}')
    return api.get_characters_character_id_mail_lists(character_id)


def put_mail(api: MailApi, character_id: int, mail_id: int, meta: PutCharactersCharacterIdMailMailIdContents, **kwargs):
    """
    Updates mail metadata.

    :param api: Mail API
    :param character_id: Character ID
    :param mail_id: Mail ID
    :param meta: Mail metadata.
    """
    log.debug(f'get_mails {character_id}')
    api.put_characters_character_id_mail_mail_id(
        character_id, meta, mail_id, **kwargs)


def mark_mail_read(api: MailApi, character_id: int, mail_id: int, read=True):
    meta = PutCharactersCharacterIdMailMailIdContents()
    meta.read = read
    put_mail(api, character_id, mail_id, meta)


def get_character(api: CharacterApi,
                  character_id: int) -> GetCharactersCharacterIdOk:
    """
    Returns a character's public information.

    :param api: Character API
    :param character_id: Character ID
    """
    log.debug(f'get_character {character_id}')
    return api.get_characters_character_id(character_id)
