"""
Tests using the EVE Swagger Interface (ESI).

Note that many of these tests are skipped unless started with the ONLINE_TESTS
environment variable set to 1.
"""
__author__ = 'Ralph Seichter'

import unittest

from sqlalchemy.orm.exc import NoResultFound

import swagger_client
from bootini_star import app
from bootini_star.esi import IdNameCache
from swagger_client.rest import ApiException
from .base import TestCase, chribba_id, eulynn_id, skipUnlessOnline, user_agent


class ESI(TestCase):

    def setUp(self):
        TestCase.setUp(self)
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
            cs = self.inCache.eve_characters(ids)
            self.assertEqual(len(ids), len(cs))
            while cs:
                c = cs.pop()
                if c.id == chribba_id:
                    self.assertEqual(c.name, 'Chribba')
                elif c.id == eulynn_id:
                    self.assertEqual(c.name, 'Eulynn')
                else:
                    self.fail('Unexpected ID: %d' % c.id)

    @skipUnlessOnline
    def test_eve_char_cached(self):
        with app.app_context():
            c1 = self.inCache.eve_character(chribba_id)
            c2 = self.inCache.eve_character(chribba_id)
            self.assertEqual(c1, c2)

    def test_eve_skill_known(self):
        with app.app_context(), self.assertRaises(NoResultFound):
            ''' Fails because the test DB is empty '''
            self.inCache.eve_type(3436)
            ''' If there was data, the following would work: '''
            # x = self.inCache.eve_type(3436)
            # self.assertEqual(x.name, 'Drones')

    def test_eve_skill_unknown(self):
        with app.app_context(), self.assertRaises(NoResultFound):
            self.inCache.eve_type(-1)

    @skipUnlessOnline
    def test_get_universe_regions(self):
        api = swagger_client.UniverseApi()
        resp = api.get_universe_regions(user_agent=user_agent, async=False)
        self.assertEqual(len(resp), 100)

    @skipUnlessOnline
    def test_get_characters_character_id(self):
        api = swagger_client.CharacterApi()
        resp = api.get_characters_character_id(
            eulynn_id, user_agent=user_agent, async=False)
        self.assertEqual(resp.name, 'Eulynn')


if __name__ == "__main__":
    unittest.main()
