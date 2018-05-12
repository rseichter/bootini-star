"""
Defining some objects here avoids circular imports.
"""
__author__ = 'Ralph Seichter'

import logging

import flask_login
import flask_mongoengine
import passlib.context

logging.basicConfig(level=logging.WARNING, format='%(asctime)s %(message)s')
log = logging.getLogger('bootini_star')

app_config = {}

login_manager = flask_login.LoginManager()

db = flask_mongoengine.MongoEngine()

pwd_context = passlib.context.CryptContext(schemes=["pbkdf2_sha256"])
