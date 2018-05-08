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

from flask.wrappers import Response

from bootini_star import app, version
from bootini_star.email import unittest_address
from bootini_star.extensions import db
from bootini_star.models import Character, User

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

    def __init__(self, email, password, uuid,
                 level=User.valid_levels['default'], activation_token=None):
        super().__init__(email, password, uuid, level=level,
                         activation_token=activation_token)


class TestCase(unittest.TestCase):

    def setUp(self):
        warnings.filterwarnings(
            'ignore', message='unclosed <ssl\.SSLSocket ',
            category=ResourceWarning)
        warnings.filterwarnings(
            'ignore', message='The psycopg2 wheel package will be renamed ',
            category=UserWarning)
        app.config.from_object('bootini_star.config.Testing')

        with app.app_context():
            db.create_all()
            user = TestUser(email, password, uuid)
            db.session.add(user)
            character = Character(uuid, character_id, character_name)
            character.token_str = json.dumps({
                'access_token': 'foo',
                'expires_at': time.time() + 600,  # Expires in 10 minutes
                'refresh_token': 'bar'
            })
            db.session.add(character)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def assertRedirect(self, response, relative_url):
        if not (response and isinstance(response, Response)):
            self.fail('No Response instance found')
        if response.status_code != 302:
            self.fail('Unexpected return code ' + str(response.status_code))
        location = response.headers.get('Location')
        if not re.match(relative_url, location, re.RegexFlag.IGNORECASE):
            msg = self._formatMessage(
                "%s does not start with %s" % (
                    safe_repr(location), safe_repr(relative_url)),
                'unexpected redirect target'
            )
            raise self.failureException(msg)


if __name__ == "__main__":
    unittest.main()
