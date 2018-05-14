"""
Tests for resource views.
"""
__author__ = 'Ralph Seichter'

import unittest

from flask.helpers import url_for

from bootini_star import app
from .base import TestCase


class ResourceViews(TestCase):
    def image_url(self, filename):
        with app.app_context():
            self.assertRedirect(
                self.app.get(url_for('res.static', filename=filename)),
                url_for('static', filename=filename)
            )

    def test_png(self):
        self.image_url('ham.png')

    def test_ico(self):
        self.image_url('spam.ico')

    def test_svg(self):
        self.image_url('eggs.svg')


if __name__ == "__main__":
    unittest.main()
