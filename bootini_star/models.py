"""
Model classes and related helper functions. SQLAlchemy is used for ORM.
"""
__author__ = 'Ralph Seichter'

import datetime
import json
from typing import Dict, Optional

import flask_login
from sqlalchemy import BigInteger, Column, DateTime, event
from sqlalchemy import ForeignKey, SmallInteger, String
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression

from .extensions import db, log, login_manager, pwd_context


class UtcNow(expression.FunctionElement):
    """Used by SQLAlchemy."""
    type = DateTime()


# noinspection PyUnusedLocal
@compiles(UtcNow, 'postgresql')
def pg_utcnow(element, compiler, **kwargs):
    """
    Return statement representing 'UTC now' in PostgreSQL dialect.
    Used by SQLAlchemy.
    """
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


# noinspection PyUnusedLocal
@compiles(UtcNow, 'mssql')
def mssql_utcnow(element, compiler, **kwargs):
    """
    Return statement representing 'UTC now' in Microsoft SQL Server dialect.
    Used by SQLAlchemy.
    """
    return 'GETUTCDATE()'


# noinspection PyUnusedLocal
@compiles(UtcNow, 'mysql')
def mysql_utcnow(element, compiler, **kwargs):
    """
    Return statement representing 'UTC now' in MySQL dialect.
    Used by SQLAlchemy.
    """
    return 'CURRENT_TIMESTAMP()'


class User(db.Model, flask_login.UserMixin):
    """
    Model class representing an application user.

    :type email: str
    :param email: Email address

    :type password: str
    :param password: Cleartext password

    :type uuid: str
    :param uuid: Unique string
    """
    __tablename__ = "users"

    valid_levels: Dict[str, int] = {
        'inactive': 0,
        'registered': 1,
        'default': 2,
        'admin': 100,
    }

    email = Column(String(256), primary_key=True, nullable=False)
    password = Column(String(90), nullable=False)
    uuid = Column(String(40), nullable=False, unique=True)
    registered_at = Column(DateTime, nullable=False, server_default=UtcNow())
    modified_at = Column(DateTime, nullable=False, server_default=UtcNow())
    level = Column(SmallInteger, nullable=False)
    activation_token = Column(String(40))
    eve_characters = relationship('Character', backref='user', lazy=True)

    def __init__(self, email, password, uuid, level=None,
                 activation_token=None):
        self.email = email
        self.password = pwd_context.hash(password)
        self.uuid = uuid
        self.level = level if level else self.valid_levels['inactive']
        if activation_token:
            self.activation_token = activation_token
        self._current_character = None

    # Required for flask_login
    def get_id(self):
        """Use email as ID (method required by Flask-Login)."""
        return self.email

    def may_login(self):
        return self.level >= self.valid_levels['default']

    @property
    def current_character(self):
        return self._current_character

    @current_character.setter
    def current_character(self, x):
        if not x or isinstance(x, Character):
            self._current_character = x
        else:
            raise TypeError("expected argument of type '" +
                            Character.__name__ + "', found '" + x.__class__.__name__ + "'.")

    def load_character(self, character_id):
        self.current_character = character_loader(
            character_id, owner=self.uuid)
        return self.current_character


@login_manager.user_loader
def user_loader(email: str) -> Optional[User]:
    """Load user from DB, return None if not found."""
    try:
        return User.query.filter_by(email=email).first()
    except SQLAlchemyError:
        return None


@event.listens_for(User, 'before_update')
def before_user_update(mapper, connection, target: User):
    target.modified_at = datetime.datetime.utcnow()


class Character(db.Model):
    """
    Model class representing an EVE Online player character. Each application
    user can own multiple player characters. Character names are unique, but
    each character still has a technical ID.

    :type owner: str
    :param owner: Owner's UUID.

    :type char_id: int
    :param char_id: Character ID.

    :type name: str
    :param name: Character name.
    """
    __tablename__ = "characters"

    # Each EVE character is owned by an application user.
    owner = Column(String(40), ForeignKey('users.uuid'), nullable=False)
    # Use ESI character ID as primary key.
    id = Column(BigInteger, primary_key=True, autoincrement=False)
    name = Column(String(256), nullable=False, unique=True)
    modified_at = Column(DateTime, nullable=False, server_default=UtcNow())
    # SSO authentication token data
    token_str = Column('token', String(500))

    def __init__(self, owner, char_id, name):
        self.owner = owner
        self.id = char_id
        self.name = name

    def set_token(self, token_dict):
        """
        Store access token dictionary.

        :type token_dict: dict
        :param token_dict: Access token dictionary.
        """
        self.token_str = json.dumps(token_dict)

    def token_dict(self):
        """Retrieve access token dictionary."""
        return json.loads(self.token_str)


@event.listens_for(Character, 'before_update')
def before_character_update(mapper, connection, target: Character):
    target.modified_at = datetime.datetime.utcnow()


def character_loader(char_id: int, **kwargs) -> Optional[Character]:
    """Load a Character object."""
    try:
        log.debug('Load character ID=' + str(char_id))
        return Character.query.filter_by(id=char_id, **kwargs).first()
    except SQLAlchemyError:
        return None


def character_list_loader(owner):
    """
    Load all Character objects for the given owner.

    :type owner: str
    :param owner: Owner's UUID.
    """
    return Character.query.filter_by(owner=owner).all()
