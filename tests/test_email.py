"""
Tests for the Mail classes.
"""
__author__ = 'Ralph Seichter'

import unittest
from bootini_star import app
from bootini_star.email import RegistrationMail
from bootini_star.extensions import app_config
from .base import skipUnlessOnline

url = '<<< No URL for unit tests >>>'


class Mail(unittest.TestCase):

    @skipUnlessOnline
    def test_regmail_ok(self):
        address = app_config['SMTP_SENDER_ADDRESS']
        headers = {'From': address, 'To': address}
        RegistrationMail().send(headers, url)

    @skipUnlessOnline
    def test_regmail_no_headers(self):
        headers = {}
        with self.assertRaises(TypeError):
            RegistrationMail().send(headers, url)

    def test_regmail_malformed_address(self):
        saved = app_config['SMTP_SENDER_ADDRESS']
        address = app_config['SMTP_SENDER_ADDRESS'] = 'malformed@address'
        headers = {'From': address, 'To': address}
        with self.assertRaises(ValueError):
            RegistrationMail().send(headers, url)
        app_config['SMTP_SENDER_ADDRESS'] = saved

    def test_regmail_unknown_scheme(self):
        saved = app_config['SMTP_SERVER_URI']
        app_config['SMTP_SERVER_URI'] = 'spam://x'
        address = app_config['SMTP_SENDER_ADDRESS']
        headers = {'From': address, 'To': address}
        with self.assertRaises(ValueError):
            RegistrationMail().send(headers, url)
        app_config['SMTP_SERVER_URI'] = saved


if __name__ == "__main__":
    unittest.main()
