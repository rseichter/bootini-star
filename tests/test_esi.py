"""
Tests using the EVE Swagger Interface (ESI).

Note that many of these tests are skipped unless started with the ONLINE_TESTS
environment variable set to 1.
"""
__author__ = 'Ralph Seichter'

import unittest

import swagger_client
from bootini_star import app
from bootini_star.esi import IdNameCache, get_mail_labels, get_mails, EveType, \
    EveGroup
from uuid import uuid4

from swagger_client.rest import ApiException
from .base import TestCase, skipUnlessOnline, user_agent
from .base import chribba_id, eulynn_id


class ESI(TestCase):

    def setUp(self):
        super().setUp()
        self.inCache = IdNameCache()

    @skipUnlessOnline
    def test_eve_char_invalid_id(self):
        with app.app_context(), self.assertRaises(ValueError):
            self.inCache.eve_character(0)

    @skipUnlessOnline
    def test_eve_char_unknown_id(self):
        with app.app_context(), self.assertRaises(ApiException):
            self.inCache.eve_character(123)

    @skipUnlessOnline
    def test_eve_char_valid_id(self):
        with app.app_context():
            c = self.inCache.eve_character(chribba_id)
            self.assertEqual(c.name, 'Chribba')

    @skipUnlessOnline
    def test_eve_char_valid_ids(self):
        ids = set([chribba_id, eulynn_id])
        with app.app_context():
            self.inCache.eve_characters(ids)  # populate cache
            cs = self.inCache.eve_characters(ids)
            self.assertEqual(len(ids), len(cs))
            while cs:
                c = cs.pop()
                if c.eve_id == chribba_id:
                    self.assertEqual(c.name, 'Chribba')
                elif c.eve_id == eulynn_id:
                    self.assertEqual(c.name, 'Eulynn')
                else:
                    self.fail(f'Unexpected ID {c.eve_id}')

    @skipUnlessOnline
    def test_eve_char_cached(self):
        with app.app_context():
            c1 = self.inCache.eve_character(chribba_id)
            c2 = self.inCache.eve_character(chribba_id)
            self.assertEqual(c1.name, c2.name)

    @skipUnlessOnline
    def test_eve_skill_known(self):
        with app.app_context():
            x = self.inCache.eve_type(3436)
            self.assertEqual(x.name['en'], 'Drones')

    def test_eve_skill_unknown(self):
        with app.app_context():
            self.inCache.eve_type(-1)

    def test_get_mail_labels(self):
        with self.assertRaises(ApiException):
            get_mail_labels(swagger_client.MailApi(), 123)

    def test_get_mail_list(self):
        with self.assertRaises(ApiException):
            get_mails(swagger_client.MailApi(), 456)

    @skipUnlessOnline
    def test_get_universe_regions(self):
        api = swagger_client.UniverseApi()
        resp = api.get_universe_regions(user_agent=user_agent, async=False)
        self.assertEqual(len(resp), 105)

    @skipUnlessOnline
    def test_get_characters_character_id(self):
        api = swagger_client.CharacterApi()
        resp = api.get_characters_character_id(
            eulynn_id, user_agent=user_agent, async=False)
        self.assertEqual(resp.name, 'Eulynn')

    def test_eve_group(self):
        eg = EveGroup()
        x = 101
        eg.eve_id = x
        self.assertEqual(eg.eve_id, x)
        x = str(uuid4())
        eg.name = x
        self.assertEqual(eg.name, x)

    def test_eve_type(self):
        et = EveType()
        x = 404
        et.eve_id = x
        self.assertEqual(et.eve_id, x)
        x = str(uuid4())
        y = str(uuid4())
        et.name = {x: y}
        self.assertEqual(et.name[x], y)
        et.description = {y: x}
        self.assertEqual(et.description[y], x)


if __name__ == "__main__":
    unittest.main()
