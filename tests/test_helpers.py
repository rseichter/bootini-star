"""
Tests for the helper functions.
"""
__author__ = 'Ralph Seichter'

import unittest
from datetime import datetime

from bootini_star import html_filter, showinfo_filter, time_filter


class Helpers(unittest.TestCase):

    def test_html_filter(self):
        html = '<font size="12" color="#bfffffff">Dear Candidate,<br><br>Your Application no </font><font size="12" color="#ffffff00"><b>"123"</font><font size="12" color="#bfffffff"> </b>has been </font><font size="12" color="#ff007f00"><b>positively</b></font><font size="12" color="#bfffffff"> verified.'
        self.assertTrue(html_filter(html).find(
            'Application no <b>"123" </b>has been <b>positively</b> verified.') == 28)

    def test_showinfo_filter_char(self):
        self.assertEqual(
            showinfo_filter('<a href="showinfo:1377//54321">eggs</a>',
                            '/spam/'),
            '<a href="/spam/character/54321">eggs</a>')

    def test_showinfo_filter_bogus(self):
        html = '<a href="showinfo:0//321">ham</a>'
        self.assertEqual(showinfo_filter(html, '/ham/'), html)

    def test_time_filter_dt(self):
        self.assertIsNotNone(time_filter(datetime.utcnow()))

    def test_time_filter_str(self):
        s = '2018-05-14T12:34:56'
        self.assertEqual(time_filter(s), '2018-05-14 12:34')

    def test_time_filter_ham(self):
        self.assertEqual(time_filter('ham'), 'ham')


if __name__ == "__main__":
    unittest.main()
