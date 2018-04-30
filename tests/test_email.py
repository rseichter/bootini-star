"""
Tests for the Mail classes.
"""
__author__ = 'Ralph Seichter'

import unittest
from bootini_star import app
from bootini_star.email import RegistrationMail

url = 'Ze URL goes here'


class Mail(unittest.TestCase):

    def test_regmail(self):
        address = app.config['SMTP_SENDER_ADDRESS']
        headers = {'From': address, 'To': address}
        RegistrationMail(app).send(headers, url)

    def test_regmail_no_headers(self):
        headers = {}
        with self.assertRaises(TypeError):
            RegistrationMail(app).send(headers, url)

    def test_regmail_no_address(self):
        headers = {}
        with self.assertRaises(TypeError):
            RegistrationMail(app).send(headers, url)

    def test_regmail_malformed_address(self):
        saved = app.config['SMTP_SENDER_ADDRESS']
        address = app.config['SMTP_SENDER_ADDRESS'] = 'malformed@address'
        headers = {'From': address, 'To': address}
        with self.assertRaises(ValueError):
            RegistrationMail(app).send(headers, url)
        app.config['SMTP_SENDER_ADDRESS'] = saved

if __name__ == "__main__":
    unittest.main()
