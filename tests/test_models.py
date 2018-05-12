"""
Tests for the application's model classes and SQLAlchemy.
"""
__author__ = 'Ralph Seichter'

import unittest

from mongoengine.errors import NotUniqueError

from bootini_star import app
from .base import TestCase, TestCharacter, TestUser
from .base import character_id, character_name
from .base import email, uuid


class UserModel(TestCase):

    def test_get_existing_user(self):
        with app.app_context():
            user = TestUser.objects(email=email).first()
            self.assertIsNotNone(user)

    def test_get_missing_user(self):
        with app.app_context():
            user = TestUser.objects(email='!' + email).first()
            self.assertIsNone(user)

    def test_duplicate_email(self):
        with app.app_context():
            user = TestUser(email, 'dummy', 'dummy')
            with self.assertRaises(NotUniqueError):
                user.save()

    def test_duplicate_uuid(self):
        with app.app_context():
            user = TestUser('!' + email, 'dummy', uuid)
            with self.assertRaises(NotUniqueError):
                user.save()

    @unittest.skip
    def test_set_current_character(self):
        with app.app_context():
            user = TestUser.objects(email=email).first()
            character = user.load_character(character_id)
            self.assertIsNotNone(character)
            user.current_character = None
            with self.assertRaises(TypeError):
                user.current_character = 123
            user.current_character = character

    @unittest.skip
    def test_get_current_character(self):
        with app.app_context():
            user = TestUser.objects(email=email).first()
            character = user.load_character(character_id)
            self.assertIsNotNone(character)
            user.current_character = character
            self.assertEqual(character, user.current_character)


class CharacterModel(TestCase):

    def test_get_existing_char(self):
        with app.app_context():
            c = TestUser.objects(email=email,
                                 characters__id=character_id).get()
            self.assertIsNotNone(c)

    def test_add_char(self):
        with app.app_context():
            c = TestCharacter('owner', 0, '!' + character_name)
            count = TestUser.objects(email=email).update_one(
                push__characters=c)
            self.assertTrue(count == 1)

    def test_merge_auth_token(self):
        token = {
            'access_token': 'access',
            'expires_at': 1524411513.324366,
            'expires_in': 123,
            'refresh_token': 'refresh',
            'token_type': 'Bearer'
        }
        with app.app_context():
            owner = TestUser.objects(characters__id=character_id).get()
            for c1 in owner.characters:
                if c1.id == character_id:
                    c1.set_token(token)
                    owner.save()
                    owner = TestUser.objects(characters__id=character_id).get()
                    for c2 in owner.characters:
                        if c2.id == character_id:
                            td = c2.token_dict()
                            break
                    self.assertEqual(token['access_token'], td['access_token'])
                    self.assertEqual(token['expires_at'], td['expires_at'])
                    self.assertEqual(token['expires_in'], td['expires_in'])
                    self.assertEqual(token['refresh_token'],
                                     td['refresh_token'])
                    self.assertEqual(token['token_type'], td['token_type'])
                    break
