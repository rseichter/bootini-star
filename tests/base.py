"""
Basic unittest configuration, classes and functions.
"""
__author__ = 'Ralph Seichter'

import ast
import json
import os
import re
import time
import unittest
import warnings
from unittest.util import safe_repr
from uuid import uuid4

from flask import url_for
from flask.wrappers import Response

from bootini_star import app, version
from bootini_star.email import unittest_address
from bootini_star.esi import Cache
from bootini_star.models import Character, User, UserLevel

user_agent = version.USER_AGENT + ' Unittest'
activation_token = str(uuid4())

email = unittest_address('spam')
email2 = unittest_address('ham')
email3 = unittest_address('eggs')
email4 = unittest_address('monty')
password = 'secret1'
password2 = 'secret2'
password3 = 'secret3'
password4 = 'secret4'

character_id = 123
character_name = 'Character ' + str(character_id)

chribba_id = 196379789
eulynn_id = 701626672

skipUnlessOnline = unittest.skipUnless(ast.literal_eval(
    os.getenv('ONLINE_TESTS', 'False')), 'ONLINE_TESTS=False')


class TestCase(unittest.TestCase):

    def setUp(self):
        warnings.filterwarnings(
            'ignore', message='unclosed <ssl\.SSLSocket ',
            category=ResourceWarning)
        warnings.filterwarnings(
            'ignore', message='The psycopg2 wheel package will be renamed ',
            category=UserWarning)
        warnings.filterwarnings(
            'ignore', message='update is deprecated.',
            category=DeprecationWarning)
        warnings.filterwarnings(
            'ignore', message='save is deprecated.',
            category=DeprecationWarning)
        warnings.filterwarnings(
            'ignore', message='remove is deprecated.',
            category=DeprecationWarning)
        app.config.from_object('bootini_star.config.Testing')
        self.app = app.test_client()
        with app.app_context():
            user = User(ensure_indexes=True)
            user.email = email
            user.password = password
            user.level = UserLevel.DEFAULT

            character = Character()
            character.eve_id = character_id
            character.name = character_name
            character.token = {
                'access_token': 'foo',
                'expires_at': time.time() + 600,  # Expires in 10 minutes
                'refresh_token': 'bar'
            }

            user.characters = [character]
            self.assertIsNotNone(user.insert())

    def tearDown(self):
        Cache().collection.delete_many({})
        User().collection.delete_many({})

    def assertRedirect(self, response, relative_url):
        if not (response and isinstance(response, Response)):
            self.fail('No Response instance found')
        if response.status_code != 302:
            self.fail('Unexpected return code ' + str(response.status_code))
        location = response.headers.get('Location')
        if not re.match(relative_url, location, re.RegexFlag.IGNORECASE):
            loc = safe_repr(location)
            url = safe_repr(relative_url)
            msg = self._formatMessage(f'{loc} does not start with {url}',
                                      'unexpected redirect target')
            raise self.failureException(msg)

    def login(self, email, password, target=None):
        with app.app_context():
            url = url_for('bs.login')
            if target:
                url += '?next=' + target
            data = dict(email=email, password=password)
            return self.app.post(url, data=data, follow_redirects=True)

    def logout(self):
        with app.app_context():
            return self.app.get(url_for('bs.logout'), follow_redirects=True)

    @staticmethod
    def new_user(password, save=True):
        address = unittest_address(str(uuid4()))
        user = User()
        user.email = address
        user.password = password
        user.level = UserLevel.DEFAULT
        if save:
            user.insert()
        return address


if __name__ == "__main__":
    unittest.main()
