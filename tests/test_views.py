"""
Tests for the application's views/routes.
"""
__author__ = 'Ralph Seichter'

import unittest
import werkzeug
from werkzeug.exceptions import BadRequest
from uuid import uuid4
import time
from flask.helpers import url_for
import json
from bootini_star import app
from bootini_star.extensions import db
from bootini_star.models import Character, User
from .base import TestCase, skipUnlessOnline, chribba_id
from .base import email, email2, email3, password, password2, password3
from .base import character_id, character_name, character_owner_hash
from bootini_star.views import user_loader


def add_user2():
    with app.app_context():
        user = User(email=email2, password=password2, uuid=str(uuid4()))
        db.session.add(user)
        db.session.commit()
        return user


character_id3 = character_id + 3
character_name3 = character_name + '3'


def add_user3():
    with app.app_context():
        user = User(email=email3, password=password3, uuid=str(uuid4()))
        db.session.add(user)
        db.session.commit()
        character = Character(
            owner=user.uuid,
            id=character_id3,
            name=character_name3,
            owner_hash=character_owner_hash
        )
        character.token_str = json.dumps({
            'access_token': 'foo',
            'expires_at': time.time() - 600,  # Expired 10 minutes ago
            'refresh_token': 'bar'
        })
        db.session.add(character)
        db.session.commit()
        return user


class AllViews(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.app = app.test_client()

    def signup(self, email, password, confirm=''):
        with app.app_context():
            return self.app.post(url_for('bs.signup'),
                                 data=dict(
                                     email=email, password=password, confirm=confirm),
                                 follow_redirects=True)

    def login(self, email, password, target=None):
        with app.app_context():
            url = url_for('bs.login')
            if target:
                url = url + '?next=' + target
            return self.app.post(url, data=dict(email=email, password=password), follow_redirects=True)

    def logout(self):
        with app.app_context():
            return self.app.get(url_for('bs.logout'), follow_redirects=True)

    def test_index(self):
        with app.app_context():
            resp = self.app.get(url_for('bs.index'))
        self.assertEqual(resp.status_code, 200)

    def test_404(self):
        resp = self.app.get('/does-not-exist')
        self.assertEqual(resp.status_code, 404)

    def test_unauthorized_dashboard(self):
        with app.app_context():
            self.assertRedirect(
                self.app.get(url_for('bs.dashboard')),
                url_for('bs.login')
            )

    def test_unauthorized_character(self):
        with app.app_context():
            self.assertRedirect(
                self.app.get(url_for('bs.character', character_id=0)),
                url_for('bs.login')
            )

    def test_bad_character_id(self):
        add_user2()
        self.login(email2, password2)
        with app.app_context(), self.assertRaises(ValueError):
            self.app.get(url_for('bs.character', character_id='bad'))

    @skipUnlessOnline
    def test_unknown_character_id(self):
        add_user2()
        self.login(email2, password2)
        with app.app_context():
            self.assertRedirect(
                self.app.get(url_for('bs.character', character_id=123)),
                url_for('bs.index')
            )

    @skipUnlessOnline
    def test_good_character_id(self):
        add_user2()
        self.login(email2, password2)
        with app.app_context():
            resp = self.app.get(url_for('bs.character', character_id=93779241))
        self.assertTrue(b'Gallente Citizen 93779241' in resp.data)

    def test_bad_login(self):
        add_user2()
        resp = self.login(email2, '!' + password2)
        self.assertTrue(b'Your login was not successful' in resp.data)

    def test_good_login(self):
        add_user2()
        resp = self.login(email2, password2)
        msg = 'This is the dashboard of ' + email2
        self.assertTrue(bytearray(msg, 'utf-8') in resp.data)

    def test_unsafe_target(self):
        add_user2()
        with self.assertRaises(BadRequest):
            self.login(email2, password2, target=r'http://www.python.org')

    def test_logout(self):
        resp = self.logout()
        self.assertTrue(b'You are logged out' in resp.data)

    def test_signup(self):
        resp = self.signup(email2, password2, confirm=password2)
        self.assertTrue(b'Registration successful' in resp.data)

    def test_signup_mismatch(self):
        resp = self.signup(email2, password2, confirm="not" + password2)
        self.assertTrue(b'Passwords do not match' in resp.data)

    def test_signup_incomplete(self):
        resp = self.signup(email2, password2)
        self.assertTrue(b'Please fill all fields' in resp.data)

    def test_signup_existing(self):
        add_user2()
        resp = self.signup(email2, password2, password2)
        self.assertTrue(b'This address is already registered' in resp.data)

    def test_load_unknown_user(self):
        # No user has been created yet
        self.assertIsNone(user_loader(email2))

    def test_dashboard(self):
        add_user2()
        self.login(email2, password2)
        with app.app_context():
            resp = self.app.get(url_for('bs.dashboard'))
        msg = 'This is the dashboard of ' + email2
        self.assertTrue(bytearray(msg, 'utf-8') in resp.data)

    def test_maillist_invalid_id(self):
        # Not a valid EVE character ID.
        add_user2()
        self.login(email2, password2)
        with app.app_context():
            self.assertRedirect(
                self.app.get(url_for('bs.maillist', character_id=123)),
                url_for('bs.dashboard')
            )

    def test_maillist_foreign_id(self):
        # EVE character ID which does not belong to the active user.
        add_user2()
        self.login(email2, password2)
        with app.app_context():
            self.assertRedirect(
                self.app.get(url_for('bs.maillist', character_id=chribba_id)),
                url_for('bs.dashboard')
            )

    def test_mail_invalid_char_id(self):
        self.login(email, password)
        with app.app_context(), self.assertRaises(ValueError):
            self.app.get(url_for('bs.mail', args='bad,123'))

    def test_mail_invalid_mail_id(self):
        self.login(email, password)
        with app.app_context(), self.assertRaises(ValueError):
            self.app.get(url_for('bs.mail', args='123,bad'))

    def test_mail_valid_args(self):
        add_user2()
        self.login(email2, password2)
        with app.app_context():
            self.assertRedirect(
                self.app.get(url_for('bs.mail', args='123,456')),
                url_for('bs.dashboard')
            )

    def test_mail_known_user_past(self):
        self.login(email, password)
        with app.app_context():
            self.assertRedirect(
                self.app.get(
                    url_for('bs.mail', args=str(character_id) + ',123')),
                url_for('bs.index')
            )

    def test_mail_known_user_future(self):
        add_user3()
        self.login(email3, password3)
        with app.app_context():
            self.assertRedirect(
                self.app.get(
                    url_for('bs.mail', args=str(character_id) + ',123')),
                url_for('bs.dashboard')
            )

    def test_remove_char(self):
        add_user3()
        self.login(email3, password3)
        with app.app_context():
            self.assertRedirect(
                self.app.get(url_for('bs.rmcharacter',
                                     character_id=character_id3)),
                url_for('bs.dashboard')
            )

    def test_remove_char_owner_mismatch(self):
        add_user3()
        self.login(email3, password3)
        with app.app_context():
            self.assertRedirect(
                self.app.get(url_for('bs.rmcharacter',
                                     character_id=character_id)),
                url_for('bs.dashboard')
            )

    def test_skillq_foreign_id(self):
        # EVE character ID which does not belong to the active user.
        add_user2()
        self.login(email2, password2)
        with app.app_context():
            self.assertRedirect(
                self.app.get(
                    url_for('bs.skillqueue', character_id=chribba_id)),
                url_for('bs.dashboard')
            )


if __name__ == "__main__":
    unittest.main()
