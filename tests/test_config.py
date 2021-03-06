"""
Tests for the configuration objects.
"""
__author__ = 'Ralph Seichter'

import unittest

from bootini_star import app
from bootini_star.config import BAD
from bootini_star.config import DEFAULT_DEVELOPMENT_DB_URI
from bootini_star.config import DEFAULT_TESTING_DB_URI


class Development(unittest.TestCase):

    def setUp(self):
        app.config.from_object('bootini_star.config.Development')

    def test_config(self):
        self.assertTrue(app.config['DEBUG'])
        self.assertNotEqual(app.config['SECRET_KEY'], BAD)
        self.assertEqual(
            app.config['MONGODB_URI'], DEFAULT_DEVELOPMENT_DB_URI)


class Testing(unittest.TestCase):

    def setUp(self):
        app.config.from_object('bootini_star.config.Testing')

    def test_config(self):
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])
        self.assertNotEqual(app.config['SECRET_KEY'], BAD)
        self.assertEqual(app.config['MONGODB_URI'], DEFAULT_TESTING_DB_URI)


class Production(unittest.TestCase):

    def setUp(self):
        app.config.from_object('bootini_star.config.Production')

    def test_config(self):
        self.assertFalse(app.config['DEBUG'])
        self.assertFalse(app.config['TESTING'])
        self.assertNotEqual(app.config['SECRET_KEY'], BAD)


if __name__ == '__main__':
    unittest.main()
