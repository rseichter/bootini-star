"""
Tests for EVE SSO views (login, callback).
"""
__author__ = 'Ralph Seichter'

import unittest

from flask.helpers import url_for

from bootini_star import app
from .base import TestCase
from .base import email, password


class SsoViews(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.app = app.test_client()

    def test_unauthorized_callback(self):
        with app.app_context():
            resp = self.app.get(url_for('sso.callback'))
        self.assertEqual(resp.status_code, 302)

    def test_callback(self):
        suffix = '?code=79ZuSjgpQQ34nVQUTqw1RpZMshfdK320q9Hdzh23UijlpLiMqjc-8ZRN7drWuFIF0'
        self.login(email, password)
        with app.app_context():
            resp = self.app.get(url_for('sso.callback') +
                                suffix, follow_redirects=True)
        self.assertTrue(b'Error obtaining authentication token' in resp.data)


if __name__ == "__main__":
    unittest.main()
