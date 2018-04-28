"""
Tests for the helper functions.
"""
__author__ = 'Ralph Seichter'

import unittest
from bootini_star import evecleanup_filter


class Helpers(unittest.TestCase):

    def test_evecleanup_filter(self):
        html = '<font size="12" color="#bfffffff">Dear Candidate,<br><br>Your Application no </font><font size="12" color="#ffffff00"><b>"123"</font><font size="12" color="#bfffffff"> </b>has been </font><font size="12" color="#ff007f00"><b>positively</b></font><font size="12" color="#bfffffff"> verified.'
        s = evecleanup_filter(html)
        self.assertTrue(s.find(
            'Application no <b>"123" </b>has been <b>positively</b> verified.') == 28)


if __name__ == "__main__":
    unittest.main()
