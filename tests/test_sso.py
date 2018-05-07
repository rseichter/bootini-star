"""
Tests for EVE Single-Sign-On.
"""
__author__ = 'Ralph Seichter'

import unittest
from bootini_star.sso import EveSso
from .base import TestCase
from uuid import uuid4
from oauthlib.oauth2.rfc6749.errors import OAuth2Error


class Sso(TestCase):

    def setUp(self):
        super().setUp()
        self.es = EveSso()

    def test_auth_url_state(self):
        my_state = str(uuid4())
        url, state = self.es.auth_url_state(state=my_state)
        self.assertIsNotNone(url)
        self.assertEqual(state, my_state)

    def test_refresh_token(self):
        rt = self.es.refresh_token()
        self.assertFalse(rt.token)
        self.assertFalse(rt.token_changed)

    def test_refresh_token_force(self):
        with self.assertRaises(OAuth2Error):
            self.es.refresh_token(refresh=True)


if __name__ == "__main__":
    unittest.main()
