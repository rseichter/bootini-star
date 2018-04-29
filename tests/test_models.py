"""
Tests for the application's model classes and SQLAlchemy.
"""
__author__ = 'Ralph Seichter'

import unittest

from sqlalchemy.exc import IntegrityError

from bootini_star import app
from bootini_star.extensions import db
from bootini_star.models import character_loader
from bootini_star.models import mssql_utcnow, mysql_utcnow, pg_utcnow
from .base import TestCase, Character, User
from .base import character_id, character_name
from .base import email, uuid


class Dialects(unittest.TestCase):

    def test_mssql_utcnow(self):
        self.assertTrue('GETUTCDATE' in mssql_utcnow(None, None))

    def test_mysql_utcnow(self):
        self.assertTrue('CURRENT_TIMESTAMP' in mysql_utcnow(None, None))

    def test_pg_utcnow(self):
        self.assertTrue('CURRENT_TIMESTAMP' in pg_utcnow(None, None))


class UserModel(TestCase):

    def test_get_existing_user(self):
        with app.app_context():
            user = User.query.filter_by(email=email).first()
            self.assertIsNotNone(user)

    def test_get_missing_user(self):
        with app.app_context():
            user = User.query.filter_by(email='!' + email).first()
            self.assertIsNone(user)

    def test_duplicate_email(self):
        with app.app_context():
            user = User(email, 'dummy', 'dummy')
            db.session.add(user)
            with self.assertRaises(IntegrityError):
                db.session.commit()

    def test_duplicate_uuid(self):
        with app.app_context():
            user = User('!' + email, 'dummy', uuid)
            db.session.add(user)
            with self.assertRaises(IntegrityError):
                db.session.commit()

    def test_set_current_character(self):
        with app.app_context():
            user = User.query.filter_by(email=email).first()
            character = user.load_character(character_id)
            self.assertIsNotNone(character)
            user.current_character = None
            with self.assertRaises(TypeError):
                user.current_character = 123
            user.current_character = character

    def test_get_current_character(self):
        with app.app_context():
            user = User.query.filter_by(email=email).first()
            character = user.load_character(character_id)
            self.assertIsNotNone(character)
            user.current_character = character
            self.assertEqual(character, user.current_character)


class CharacterModel(TestCase):

    def test_get_existing_char(self):
        with app.app_context():
            character = character_loader(character_id)
            self.assertIsNotNone(character)

    def test_get_existing_char_wrong_owner(self):
        with app.app_context():
            character = character_loader(character_id, owner='bad')
            self.assertIsNone(character)

    def test_character_loader(self):
        self.assertIsNone(character_loader(None))

    def test_bad_owner(self):
        with app.app_context():
            character = Character('bad', 0, '!' + character_name, 'dummy')
            db.session.add(character)
            with self.assertRaises(IntegrityError):
                db.session.commit()

    def test_add_char(self):
        with app.app_context():
            character = Character(uuid, 0, '!' + character_name, 'dummy')
            db.session.add(character)
            db.session.commit()

    def test_merge_auth_token(self):
        with app.app_context():
            character = Character.query.filter_by(id=character_id).first()
            token = {
                'access_token': 'access',
                'expires_at': 1524411513.324366,
                'expires_in': 123,
                'refresh_token': 'refresh',
                'token_type': 'Bearer'
            }
            character.set_token(token)
            td = character.token_dict()
            self.assertEqual(token['access_token'], td['access_token'])
            self.assertEqual(token['expires_at'], td['expires_at'])
            self.assertEqual(token['expires_in'], td['expires_in'])
            self.assertEqual(token['refresh_token'], td['refresh_token'])
            self.assertEqual(token['token_type'], td['token_type'])
