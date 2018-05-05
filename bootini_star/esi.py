"""
Classes in this module are used to cache EVE Swagger Interface calls and static
database entries like EVE item groups and types.
"""
__author__ = 'Ralph Seichter'

from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import relationship

import swagger_client
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
    name = Column(String(100), nullable=False)
    expires = Column(DateTime)

    def __init__(self, entry_id, name):
        self.id = entry_id
        self.name = name


class CacheBase:
    """Base class for handling Cache objects."""

    @staticmethod
    def get_cached(entry_id):
        ce = Cache.query.filter_by(id=entry_id).first()
        if ce:
            log.debug('Found ID ' + str(entry_id) + ' in cache')
            return ce
        return None

    @staticmethod
    def add(entry_id, entry_name):
        ce = Cache(entry_id, entry_name)
        log.debug('Adding ID ' + str(entry_id) + ' to cache')
        db.session.add(ce)
        db.session.commit()
        return ce


class IdNameCache(CacheBase):
    """Cache for both ID-name-pairs and EVE types."""

    def eve_character(self, char_id):
        """
        Return the EVE character for a given character ID.

        :type char_id: int
        :param char_id: Character ID used for lookup
        """
        ce = self.get_cached(char_id)
        if ce:
            return ce
        api = swagger_client.CharacterApi()
        log.debug('Querying ESI for character ID ' + str(char_id))
        rv = api.get_characters_character_id(char_id)
        return self.add(char_id, rv._name)

    @staticmethod
    def eve_type(type_id):
        """
        Return the EVE type for a given ID.

        :type type_id: int
        :param type_id: EVE type ID used for lookup
        """
        log.debug('Querying DB for EVE type ID ' + str(type_id))
        return EveType.query.filter_by(id=type_id).one()
