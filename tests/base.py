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
from bootini_star.extensions import pwd_context
from bootini_star.models import Character, User, UserLevel, save_user

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


class TestUser(User):
    def __init__(self, email, password, token=None, *args, **kwargs):
        super().__init__(email=email,
                         password=pwd_context.hash(password),
                         activation_token=token,
                         level=UserLevel.DEFAULT)


class TestCharacter(Character):
    def __init__(self, id, name, *args, **kwargs):
        super().__init__(id=id, name=name)


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
        app.config.from_object('bootini_star.config.Testing')

        with app.app_context():
            user = TestUser(email, password)
            character = TestCharacter(character_id, character_name)
            character.token_str = json.dumps({
                'access_token': 'foo',
                'expires_at': time.time() + 600,  # Expires in 10 minutes
                'refresh_token': 'bar'
            })
            user.characters.append(character)
            save_user(user)

    def tearDown(self):
        with app.app_context():
            TestUser.drop_collection()
            Cache.drop_collection()

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

    def login(self, eml, pw, target=None):
        with app.app_context():
            url = url_for('bs.login')
            if target:
                url += '?next=' + target
            data = dict(email=eml, password=pw)
            return self.app.post(url, data=data, follow_redirects=True)

    def logout(self):
        with app.app_context():
            return self.app.get(url_for('bs.logout'), follow_redirects=True)


if __name__ == "__main__":
    unittest.main()
