"""
Tests for the MongoDB support classes and functions.
"""
__author__ = 'Ralph Seichter'

import unittest

import pymongo

from bootini_star.extensions import pwd_context
from bootini_star.models import Character, User, user_loader

EMAIL = 'tim@buster.net'
EMAIL2 = 'fred@flint.org'
PASSWORD = 'so secret'
PASSWORD2 = 'guess what'


class MongoDocumentTests(unittest.TestCase):
    def setUp(self):
        u = User(ensure_indexes=True)
        u.email = EMAIL
        u.password = PASSWORD
        mongo_id = u.insert()
        self.assertIsNotNone(mongo_id)

    def tearDown(self):
        User().collection.delete_many({})

    def test_read_existing_user(self):
        data = User().collection.find_one({'email': EMAIL})
        self.assertIsNotNone(data)
        self.assertTrue(pwd_context.verify(PASSWORD, data['password']))

    def test_insert_duplicate_user(self):
        u = User()
        u.email = EMAIL
        u.password = 'not' + PASSWORD
        with self.assertRaises(pymongo.errors.DuplicateKeyError):
            u.insert()

    def test_insert_valid_user(self):
        u = User()
        u.email = EMAIL2
        u.password = PASSWORD2
        self.assertIsNotNone(u.insert())

    def test_insert_character(self):
        c = Character()
        c.eve_id = 1
        c.token = 'token #1'
        with self.assertRaises(NotImplementedError):
            c.insert()

    def test_insert_user_with_character(self):
        u = User()
        u.email = EMAIL2
        u.password = PASSWORD2
        u.level = 321
        u.activation_token = 'a-token for user 2'

        c1 = Character()
        c1.eve_id = 1
        c1.token = 'token #1'

        c2 = Character()
        c2.eve_id = 2
        c2.token = 'token #2'

        u.characters = [c1, c2]
        self.assertIsNotNone(u.insert())

        u2 = user_loader(EMAIL2)
        self.assertTrue(isinstance(u2, User))


if __name__ == '__main__':
    unittest.main()
