"""
Model classes (backed by MongoDB) and related helper functions.
"""
__author__ = 'Ralph Seichter'

import enum
import re

import flask_login
import pymongo
from pymongo.results import InsertOneResult, UpdateResult, DeleteResult

from .extensions import app_config, log, login_manager, pwd_context

db = None


@enum.unique
class UserLevel(enum.IntEnum):
    INACTIVE = 0
    REGISTERED = 1
    DEFAULT = 2
    ADMIN = 100


def init_mongodb():
    global db
    db_uri = app_config['MONGODB_URI']
    match = re.search(r'/(\w+)$', db_uri)
    db_client = pymongo.MongoClient(db_uri)
    db = db_client.get_database(match[1])


def list_from_mongo(data: dict) -> list:
    result = []
    for item in data:
        obj = globals()[item['_class']]()
        obj.from_mongo(item)
        result.append(obj)
    return result


class MongoField:
    def __init__(self, name, type_, value=None, unique=False):
        self.name = name
        self.type = type_
        self.value = value
        self.unique = unique

    def to_mongo(self):
        if self.type == list:
            return [x.to_mongo() for x in self.value]
        else:
            return self.value


class MongoDocument:
    def __init__(self, collection: str):
        self._collection = collection
        self._field_dict = {}
        self.add_field(MongoField('_id', str))

    def __hash__(self) -> int:
        return hash(self.get_field_value('_id'))

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

    def add_field(self, field: MongoField):
        self._field_dict[field.name] = field

    def get_field_value(self, field_name):
        return self._field_dict[field_name].value

    def set_field_value(self, field_name, value):
        field: MongoField = self._field_dict[field_name]
        field.value = value

    def to_mongo(self) -> dict:
        result = {'_class': self.__class__.__name__}
        for name, field in self._field_dict.items():
            if field.value:
                result[name] = field.to_mongo()
        return result

    def from_mongo(self, data: dict):
        for name, field in self._field_dict.items():
            if name in data:
                if field.type == list:
                    field.value = list_from_mongo(data[name])
                else:
                    field.value = data[name]

    @property
    def collection(self) -> pymongo.collection.Collection:
        global db
        if not db:
            init_mongodb()
        return db[self._collection]

    def ensure_indexes(self):
        index_info = self.collection.index_information()
        for name, field in self._field_dict.items():
            if field.unique:
                index_name = name + '_u'
                if index_name not in index_info:
                    self.collection.create_index([(name, pymongo.ASCENDING)],
                                                 name=index_name, unique=True)

    def insert(self) -> str:
        data = self.to_mongo()
        r: InsertOneResult = self.collection.insert_one(data)
        return r.inserted_id

    def update(self) -> int:
        data = self.to_mongo()
        filter = {'_id': self.get_field_value('_id')}
        r: UpdateResult = self.collection.update_one(filter, {"$set": data})
        return r.modified_count


class EmbeddedDocument(MongoDocument):
    def insert(self) -> str:
        raise NotImplementedError('Embedded documents cannot be saved alone')


class Character(EmbeddedDocument):
    def __init__(self):
        MongoDocument.__init__(self, None)
        self.add_field(MongoField('eve_id', int))
        self.add_field(MongoField('name', str))
        self.add_field(MongoField('token', dict))

    @property
    def eve_id(self):
        return self.get_field_value('eve_id')

    @eve_id.setter
    def eve_id(self, value):
        self.set_field_value('eve_id', value)

    @property
    def name(self):
        return self.get_field_value('name')

    @name.setter
    def name(self, value):
        self.set_field_value('name', value)

    @property
    def token(self):
        return self.get_field_value('token')

    @token.setter
    def token(self, value):
        self.set_field_value('token', value)


class User(MongoDocument, flask_login.UserMixin):
    def __init__(self, ensure_indexes=False):
        MongoDocument.__init__(self, 'users')
        self.add_field(MongoField('email', str, unique=True))
        self.add_field(MongoField('password', str))
        self.add_field(MongoField('level', int))
        self.add_field(MongoField('activation_token', str))
        self.add_field(MongoField('characters', list))
        if ensure_indexes:
            self.ensure_indexes()

    @property
    def email(self) -> str:
        return self.get_field_value('email')

    @email.setter
    def email(self, value: str):
        self.set_field_value('email', value)

    @property
    def password(self) -> str:
        return self.get_field_value('password')

    @password.setter
    def password(self, value: str):
        self.set_field_value('password', pwd_context.hash(value))

    @property
    def level(self) -> int:
        return self.get_field_value('level')

    @level.setter
    def level(self, value: int):
        self.set_field_value('level', value)

    @property
    def characters(self) -> list:
        return self.get_field_value('characters')

    @characters.setter
    def characters(self, value: list):
        self.set_field_value('characters', value)

    @property
    def activation_token(self) -> str:
        return self.get_field_value('activation_token')

    @activation_token.setter
    def activation_token(self, value: str):
        self.set_field_value('activation_token', value)

    @property
    def is_admin(self):
        return self.level >= UserLevel.ADMIN

    def get_id(self):
        """Use email as ID (method required by Flask-Login)."""
        return self.email

    def load_character(self, eve_id: int):
        _list = self.characters
        if _list:
            for character in _list:
                if character.eve_id == eve_id:
                    return character
        return None

    def remove_character(self, eve_id: int):
        if self.characters:
            self.characters = [character for character in self.characters if
                               character.eve_id != eve_id]


def activate_user(email: str, token: str) -> User:
    log.debug(f'activate_user {email} {token}')
    r: UpdateResult = User().collection.update_one(
        {'email': email, 'activation_token': token},
        {'$set': {'level': UserLevel.DEFAULT},
         '$unset': {'activation_token': None}})
    return r.modified_count


def delete_user(email: str) -> User:
    log.debug(f'delete_user {email}')
    r: DeleteResult = User().collection.delete_one({'email': email})
    return r.deleted_count


@login_manager.user_loader
def load_user(email: str) -> User:
    log.debug(f'load_user {email}')
    user = User()
    data = user.collection.find_one({'email': email})
    if not data:
        return None
    user.from_mongo(data)
    return user


@login_manager.request_loader
def request_loader(request, min_level: UserLevel = UserLevel.DEFAULT):
    log.debug(f'request_loader {request}')
    email = request.form.get('email')
    password = request.form.get('password')
    if not (email and password):
        return None
    user = User()
    data = user.collection.find_one(
        {'email': email, 'level': {'$gte': min_level}})
    if not data:
        log.warning(f'No user {email} with level >= {min_level}')
    elif not pwd_context.verify(password, data['password']):
        log.warning(f'User {email} password mismatch')
    else:
        user.from_mongo(data)
        log.info(f'User {email} (level {user.level}) logged in')
        return user
    return None
