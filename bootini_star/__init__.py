"""
Inspect EVE Online in-game mail and skill queues in a web browser. Inspired by
CCP's discontinued EVE Gate app.

This project was started on 2018-04-20 by Ralph Seichter.
"""
__author__ = 'Ralph Seichter'

import os
import re

from flask import Flask
from flask.views import MethodView
from flask_migrate import Migrate, migrate
from flask_sqlalchemy import SQLAlchemy

from .extensions import db, login_manager
from .sso_views import blueprint as sso_blueprint
from .views import blueprint as bs_blueprint

app = Flask(__name__)
# Development configuration settings are the default.
app_settings = os.getenv('APP_SETTINGS', 'bootini_star.config.Development')
app.config.from_object(app_settings)

db.init_app(app)
migrate = Migrate(app, db)

login_manager.init_app(app)
login_manager.login_message_category = 'info'
login_manager.blueprint_login_views = {
    bs_blueprint.name: 'bs.login',
    sso_blueprint.name: 'bs.login'
}

app.register_blueprint(bs_blueprint)
app.register_blueprint(sso_blueprint)


@app.template_filter('evecleanup')
def evecleanup_filter(html):
    """
    Strip selected HTML tags created within EVE's mail client.

    :type html: str
    :param html: HTML string to clean up
    """
    flags = re.RegexFlag.MULTILINE
    s = re.sub(r'<(font[^>]*|/font)>', '', html, flags=flags)
    s = re.sub(r'<(span[^>]*|/span)>', '', s, flags=flags)
    return re.sub(r'<div>(.*?)</div>', r'\1', s, flags=flags)
