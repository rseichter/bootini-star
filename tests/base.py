"""
Basic unittest configuration, classes and functions.
"""
from bootini_star.esi import Cache

__author__ = 'Ralph Seichter'

import ast
import json
import os
import re
import unittest
import warnings
from unittest.util import safe_repr
from uuid import uuid4

import time
from flask.wrappers import Response

from bootini_star import app, version
from bootini_star.email import unittest_address
from bootini_star.extensions import pwd_context
from bootini_star.models import Character, User, UserLevel

user_agent = version.USER_AGENT + ' Unittest'

email = unittest_address('spam')
password = 'secret1'
uuid = str(uuid4())

email2 = unittest_address('ham')
password2 = 'secret2'
uuid2 = str(uuid4())

email3 = unittest_address('eggs')
password3 = 'secret3'
uuid3 = str(uuid4())

email4 = unittest_address('monty')
password4 = 'secret4'
token4 = str(uuid4())

character_id = 123
character_name = 'Character ' + str(character_id)

chribba_id = 196379789
eulynn_id = 701626672

skipUnlessOnline = unittest.skipUnless(ast.literal_eval(
    os.getenv('ONLINE_TESTS', 'False')), 'ONLINE_TESTS=False')


class TestUser(User):
    def __init__(self, email, password, uuid, token=None, *args, **kwargs):
        super().__init__(email=email, level=UserLevel.DEFAULT, password=pwd_context.hash(password), uuid=uuid, activation_token=token)


class TestCharacter(Character):
    def __init__(self, owner, id, name, *args, **kwargs):
        super().__init__(owner=owner, id=id, name=name)


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
            user = TestUser(email, password, uuid)
            user.save()
            character = TestCharacter(uuid, character_id, character_name)
            character.token_str = json.dumps({
                'access_token': 'foo',
                'expires_at': time.time() + 600,  # Expires in 10 minutes
                'refresh_token': 'bar'
            })
            TestUser.objects(email=email).update_one(
                push__characters=character)

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


if __name__ == "__main__":
    unittest.main()
