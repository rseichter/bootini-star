"""
Tests for the Mail classes.
"""
__author__ = 'Ralph Seichter'

import unittest

from bootini_star.email import RegistrationMail
from bootini_star.extensions import app_config
from .base import email, skipUnlessOnline

UNITTEST_URL = '<<< No URL for unit tests >>>'


class Mail(unittest.TestCase):

    @skipUnlessOnline
    def test_regmail_to_operator(self):
        address = app_config['SMTP_SENDER_ADDRESS']
        headers = {'From': address, 'To': address}
        RegistrationMail().send(headers, UNITTEST_URL)

    @skipUnlessOnline
    def test_regmail_to_unittest_address(self):
        address = app_config['SMTP_SENDER_ADDRESS']
        headers = {'From': address, 'To': email}
        RegistrationMail().send(headers, UNITTEST_URL)

    @skipUnlessOnline
    def test_regmail_no_headers(self):
        headers = {}
        with self.assertRaises(TypeError):
            RegistrationMail().send(headers, UNITTEST_URL)

    def test_regmail_malformed_address(self):
        saved = app_config['SMTP_SENDER_ADDRESS']
        address = app_config['SMTP_SENDER_ADDRESS'] = 'malformed@address'
        headers = {'From': address, 'To': address}
        with self.assertRaises(ValueError):
            RegistrationMail().send(headers, UNITTEST_URL)
        app_config['SMTP_SENDER_ADDRESS'] = saved

    def test_regmail_unknown_scheme(self):
        saved = app_config['SMTP_SERVER_URI']
        app_config['SMTP_SERVER_URI'] = 'spam://x'
        address = app_config['SMTP_SENDER_ADDRESS']
        headers = {'From': address, 'To': address}
        with self.assertRaises(ValueError):
            RegistrationMail().send(headers, UNITTEST_URL)
        app_config['SMTP_SERVER_URI'] = saved


if __name__ == "__main__":
    unittest.main()
