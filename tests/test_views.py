"""
Tests for the application's views/routes.
"""
__author__ = 'Ralph Seichter'

import json
import time
import unittest

from flask.helpers import url_for

from bootini_star import account_views, app, forms
from bootini_star.account_views import InvalidUsageError, SIGNUP_FAILED
from bootini_star.extensions import app_config
from bootini_star.forms import CREATE_INDEXES
from bootini_star.models import User, UserLevel, user_loader
from .base import Character, TestCase
from .base import activation_token, password, password2, password3
from .base import character_id, character_name
from .base import chribba_id, skipUnlessOnline
from .base import email, email2, email3, email4

character_id3 = character_id + 3
character_name3 = character_name + '3'


def add_user2():
    with app.app_context():
        user = User()
        user.email = email2
        user.password = password2
        user.level = UserLevel.DEFAULT
        user.insert()
        return user


def add_user3():
    with app.app_context():
        user = User()
        user.email = email3
        user.password = password3
        user.level = UserLevel.ADMIN

        character = Character()
        character.eve_id = character_id3
        character.name = character_name3
        character.token = json.dumps({
            'access_token': 'foo',
            'expires_at': time.time() - 600,  # Expired 10 minutes ago
            'refresh_token': 'bar'
        })
        user.characters = [character]
        user.insert()
        return user


def add_user4():
    with app.app_context():
        user = User()
        user.email = email4
        user.password = 'dummy'
        user.activation_token = activation_token
        user.level = UserLevel.REGISTERED
        user.insert()
        return user


class AllViews(TestCase):
    def assertAppVersion(self, response):
        ver = app_config['VERSION']
        self.assertSubstr(f' version {ver}', response)

    def assertSubstr(self, string: str, response):
        if not (response and response.data):
            self.fail('Invalid response object')
        self.assertTrue(string.encode('utf-8') in response.data)

    def pwchange(self, current, pw, confirm=''):
        data = dict(current=current, password=pw, confirm=confirm)
        with app.app_context():
            return self.app.post(url_for('bs.password'), data=data,
                                 follow_redirects=True)

    def signup(self, eml, pw, confirm=''):
        data = dict(email=eml, password=pw, confirm=confirm)
        with app.app_context():
            return self.app.post(url_for('bs.signup'), data=data,
                                 follow_redirects=True)

    def selfdestruct(self, eml, pw):
        data = dict(email=eml, password=pw)
        with app.app_context():
            return self.app.post(url_for('bs.selfdestruct'), data=data,
                                 follow_redirects=True)

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

    def test_bad_login_email(self):
        add_user2()
        resp = self.login('', password2)
        self.assertSubstr(forms.EMAIL_MSG, resp)

    def test_bad_login_pw(self):
        add_user2()
        resp = self.login(email2, '!' + password2)
        self.assertSubstr(account_views.LOGIN_FAILED, resp)

    def test_good_login(self):
        add_user2()
        resp = self.login(email2, password2)
        self.assertAppVersion(resp)

    def test_unsafe_target(self):
        add_user2()
        with self.assertRaises(InvalidUsageError):
            self.login(email2, password2, target=r'http://python.org')

    def test_logout(self):
        add_user2()
        self.login(email2, password2)
        resp = self.logout()
        self.assertSubstr(account_views.YOU_LOGGED_OUT, resp)

    def test_signup_get(self):
        with app.app_context():
            resp = self.app.get(url_for('bs.signup'))
        self.assertSubstr(forms.CPW_LABEL, resp)

    @skipUnlessOnline
    def test_signup(self):
        resp = self.signup(
            app_config['SMTP_SENDER_ADDRESS'], password2, confirm=password2)
        self.assertTrue(b'Registration successful' in resp.data)

    def test_signup_mismatch(self):
        resp = self.signup(email2, password2, confirm="not" + password2)
        self.assertSubstr(forms.MATCH_MSG, resp)

    def test_signup_incomplete(self):
        resp = self.signup(email2, password2)
        self.assertSubstr(forms.CPW_MSG, resp)

    def test_signup_bad_email(self):
        resp = self.signup('a@b', password2, password2)
        self.assertSubstr(forms.EMAIL_MSG, resp)

    def test_signup_existing(self):
        add_user2()
        with app.app_context():
            resp = self.signup(email2, password2, password2)
            self.assertSubstr(SIGNUP_FAILED, resp)

    def test_change_pw_get(self):
        add_user2()
        self.login(email2, password2)
        with app.app_context():
            resp = self.app.get(url_for('bs.password'))
        self.assertSubstr(forms.CURRENT_LABEL, resp)

    def test_change_pw(self):
        add_user2()
        self.login(email2, password2)
        resp = self.pwchange(password2, password, password)
        self.assertSubstr(account_views.PASSWORD_CHANGED, resp)

    def test_change_pw_wrong_current(self):
        add_user2()
        self.login(email2, password2)
        resp = self.pwchange(password3, password, password)
        self.assertSubstr(account_views.PASSWORD_MISTYPED, resp)

    def test_change_pw_missing_current(self):
        add_user2()
        self.login(email2, password2)
        resp = self.pwchange('', password, password)
        self.assertSubstr(forms.CURRENT_MSG, resp)

    def test_selfdestruct_get(self):
        add_user2()
        self.login(email2, password2)
        with app.app_context():
            resp = self.app.get(url_for('bs.selfdestruct'))
        self.assertTrue(b'really want to delete your account' in resp.data)

    def test_selfdestruct(self):
        add_user2()
        self.login(email2, password2)
        resp = self.selfdestruct(email2, password2)
        self.assertSubstr(account_views.ACCOUNT_DELETED, resp)

    def test_selfdestruct_invalid_mail(self):
        add_user2()
        self.login(email2, password2)
        resp = self.selfdestruct('', password2)
        self.assertSubstr(forms.EMAIL_MSG, resp)

    def test_selfdestruct_bad_pw(self):
        add_user2()
        self.login(email2, password2)
        resp = self.selfdestruct(email2, 'bad')
        self.assertTrue(
            account_views.ACCOUNT_DELETE_FAILED.encode('utf-8') in resp.data)

    def test_load_unknown_user(self):
        with app.app_context():
            self.assertIsNone(user_loader(email2))

    def test_dashboard(self):
        add_user2()
        self.login(email2, password2)
        with app.app_context():
            resp = self.app.get(url_for('bs.dashboard'))
        self.assertAppVersion(resp)

    def test_maillist_invalid_id(self):
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
            self.app.get(url_for('bs.mail', character_id='bad', mail_id=123))

    def test_mail_invalid_mail_id(self):
        self.login(email, password)
        with app.app_context(), self.assertRaises(ValueError):
            self.app.get(url_for('bs.mail', character_id=123, mail_id='bad'))

    def test_mail_valid_args(self):
        add_user2()
        self.login(email2, password2)
        with app.app_context():
            self.assertRedirect(
                self.app.get(
                    url_for('bs.mail', character_id=123, mail_id=456)),
                url_for('bs.dashboard')
            )

    def test_mail_known_user_past(self):
        self.login(email, password)
        with app.app_context():
            self.assertRedirect(
                self.app.get(url_for('bs.mail', character_id=character_id,
                                     mail_id=123)),
                url_for('bs.index')
            )

    def test_mail_known_user_future(self):
        add_user3()
        self.login(email3, password3)
        with app.app_context():
            self.assertRedirect(
                self.app.get(
                    url_for('bs.mail', character_id=character_id,
                            mail_id=123)),
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

    def test_rm_mail_invalid_char_id(self):
        self.login(email, password)
        with app.app_context(), self.assertRaises(ValueError):
            self.app.get(url_for('bs.rmmail', character_id='bad', mail_id=123))

    def test_rm_mail_invalid_mail_id(self):
        self.login(email, password)
        with app.app_context(), self.assertRaises(ValueError):
            self.app.get(url_for('bs.rmmail', character_id=123, mail_id='bad'))

    def test_rm_mail_valid_args(self):
        add_user3()
        self.login(email3, password3)
        with app.app_context():
            self.assertRedirect(
                self.app.get(
                    url_for('bs.rmmail', character_id=123, mail_id=456)),
                url_for('bs.dashboard')
            )

    def test_rm_mail_known_user(self):
        add_user3()
        self.login(email3, password3)
        with app.app_context():
            self.assertRedirect(
                self.app.get(
                    url_for('bs.rmmail', character_id=character_id,
                            mail_id=456)),
                url_for('bs.dashboard')
            )

    def test_activate_unknown_email(self):
        with app.app_context():
            # log.info(resp)
            self.assertRedirect(
                self.app.get(url_for('bs.activate', email='bad', token='x')),
                url_for('bs.index')
            )

    def test_activate_unknown_token(self):
        add_user4()
        with app.app_context():
            self.assertRedirect(
                self.app.get(
                    url_for('bs.activate', email=email4, token='bad')),
                url_for('bs.index')
            )

    def test_activate_unknown_email(self):
        with app.app_context():
            self.assertRedirect(
                self.app.get(url_for('bs.activate', email='bad', token='x')),
                url_for('bs.index')
            )

    def test_activate_valid(self):
        add_user4()
        with app.app_context():
            self.assertRedirect(
                self.app.get(
                    url_for('bs.activate', email=email4,
                            token=activation_token)),
                url_for('bs.login')
            )

    def test_invalid_usage(self):
        try:
            raise InvalidUsageError(password, status_code=432)
        except InvalidUsageError as e:
            self.assertEqual(e.message, password)
            self.assertEqual(e.status_code, 432)

    def test_admin_valid(self):
        add_user3()
        self.login(email3, password3)
        with app.app_context():
            resp = self.app.get(url_for('bs.admin'))
            self.assertSubstr(CREATE_INDEXES, resp)

    def test_admin_unauthorised(self):
        self.login(email, password)
        with app.app_context():
            self.assertRedirect(self.app.get(url_for('bs.admin')),
                                url_for('bs.login'))


if __name__ == "__main__":
    unittest.main()
