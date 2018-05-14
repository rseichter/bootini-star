"""
Model classes and related helper functions. SQLAlchemy is used for ORM.
"""
__author__ = 'Ralph Seichter'

import datetime
import enum
import json
from typing import Optional

import flask_login
import mongoengine
from mongoengine import MongoEngineConnectionError

from .extensions import log, login_manager, pwd_context


@enum.unique
class UserLevel(enum.IntEnum):
    INACTIVE = 0
    REGISTERED = 1
    DEFAULT = 2
    ADMIN = 100


class Character(mongoengine.EmbeddedDocument):
    """
    Model class representing an EVE Online player character. Each application
    user can own multiple player characters. Character names are unique, but
    each character still has a technical ID.
    """
    meta = {'collection': 'characters', 'allow_inheritance': True}

    # Use ESI character ID as primary key.
    id = mongoengine.LongField(primary_key=True)
    name = mongoengine.StringField(required=True, max_length=256)
    modified_at = mongoengine.DateTimeField(default=datetime.datetime.utcnow)
    # SSO authentication token data
    token_str = mongoengine.StringField(max_length=500)

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


class User(mongoengine.Document, flask_login.UserMixin):
    """
    Model class representing an application user.
    """
    meta = {'collection': 'users', 'allow_inheritance': True}

    email = mongoengine.EmailField(required=True, unique=True)
    password = mongoengine.StringField(required=True, max_length=90)
    level = mongoengine.IntField(required=True, min_value=-100, max_value=100)
    registered_at = mongoengine.DateTimeField(default=datetime.datetime.utcnow)
    modified_at = mongoengine.DateTimeField(default=datetime.datetime.utcnow)
    activation_token = mongoengine.StringField(max_length=40)
    characters = mongoengine.EmbeddedDocumentListField(Character)

    def get_id(self):
        """Use email as ID (method required by Flask-Login)."""
        return self.email

    @property
    def is_admin(self):
        return self.level >= UserLevel.ADMIN

    def load_character(self, character_id):
        for c in self.characters:
            if c.id == character_id:
                return c
        return None


def save_user(user: User):
    """Save user to DB, updating the modification timestamp."""
    log.debug(f'save_user {user.email}')
    user.modified_at = datetime.datetime.utcnow()
    user.save()


@login_manager.user_loader
def load_user(email: str) -> Optional[User]:
    """
    Load user from DB based on email address.

    :param email: Lookup key.
    :return: User object or None if not found.
    """
    log.debug(f'load_user {email}')
    try:
        user = User.objects(email=email).first()
        if user:
            print(f'{user.email} is level {user.level}')
        return user
    except MongoEngineConnectionError as e:
        log.error(f'Error loading user {email}: {e}')
    return None


@login_manager.request_loader
def request_loader(request, min_level: UserLevel = UserLevel.DEFAULT):
    log.debug(f'request_loader {request}')
    email = request.form.get('email')
    password = request.form.get('password')
    if not (email and password):
        return None
    user = User.objects(email=email.strip(), level__gte=min_level).first()
    if not user:
        log.warning(f'No user {email} with level >= {min_level}')
    elif not pwd_context.verify(password, user.password):
        log.warning(f'User {email} password mismatch')
    else:
        log.info(f'User {email} (level {user.level}) logged in')
        return user
    return None
