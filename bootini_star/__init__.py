"""
Inspect EVE Online in-game mail and skill queues in a web browser. Inspired by
CCP's discontinued EVE Gate app.

This project was started on 2018-04-20 by Ralph Seichter.
"""
__author__ = 'Ralph Seichter'

import logging
import os
import re
from datetime import datetime

from flask import Flask
from flask_bootstrap import BOOTSTRAP_VERSION, Bootstrap, WebCDN
from flask_migrate import Migrate

from .extensions import app_config, db, log, login_manager
from .resource_views import StaticFileConverter, blueprint as res_blueprint
from .sso_views import blueprint as sso_blueprint
from .views import blueprint as bs_blueprint

app = Flask(__name__)
# Development configuration settings are the default.
app_settings = os.getenv('APP_SETTINGS', 'bootini_star.config.Development')
app.config.from_object(app_settings)
app_config.update(app.config)

# Set logging level
ls = app_config['LOG_LEVEL'].upper()
ln = getattr(logging, ls, None)
if not isinstance(ln, int):
    raise ValueError("Invalid LOG_LEVEL '%s'" % ls)
log.setLevel(ln)

Bootstrap(app)
cdns = app.extensions['bootstrap']['cdns']
cdns['darkly'] = WebCDN(
    '//stackpath.bootstrapcdn.com/bootswatch/%s/darkly/' % BOOTSTRAP_VERSION)
db.init_app(app)
migrate = Migrate(app, db)

login_manager.init_app(app)
login_manager.login_message_category = 'info'
login_manager.blueprint_login_views = {
    bs_blueprint.name: 'bs.login',
    sso_blueprint.name: 'bs.login'
}

app.url_map.converters['static'] = StaticFileConverter
app.register_blueprint(res_blueprint)
app.register_blueprint(bs_blueprint)
app.register_blueprint(sso_blueprint)

_re_flags = re.RegexFlag.MULTILINE
_div_pat = re.compile(r'<div>(.*?)</div>', flags=_re_flags)
_font_pat = re.compile(r'<(font[^>]*|/font)>', flags=_re_flags)
_span_pat = re.compile(r'<(span[^>]*|/span)>', flags=_re_flags)
_time_pat = re.compile(r'\+00:00')
_si_pat = re.compile(r'href="showinfo:(\d+)//(\d+)"', flags=_re_flags)


@app.template_filter('eve_html')
def html_filter(html: str) -> str:
    """
    Strip selected HTML tags created within EVE's mail client.

    :param html: HTML string to clean up
    """
    html = re.sub(_font_pat, '', html)
    html = re.sub(_span_pat, '', html)
    return re.sub(_div_pat, r'\1', html)


@app.template_filter('showinfo')
def showinfo_filter(html: str, urlbase: str) -> str:
    """
    Convert EVE 'showinfo' links into HTML links. This currently only works for
    links that reference EVE characters, other link types are ignored.

    :param html: HTML string to parse
    :param urlbase: Base URL to append to
    """
    flags = _re_flags
    pos = 0
    m = _si_pat.search(html)
    while m:
        if 1373 <= int(m.group(1)) <= 1386:
            href = 'href="%scharacter/%s"' % (urlbase, m.group(2))
            html = re.sub(m.group(0), href, html, flags=flags)
        pos += len(m.group(0))
        m = _si_pat.search(html, pos)
    return html


@app.template_filter('eve_time')
def time_filter(dt: datetime) -> str:
    """
    Returns a string representation of a datetime object. Seconds, microseconds
    and TZ offset (EVE uses UTC anyway) are truncated.

    :param dt: Datetime object to convert to a string.
    """
    return dt.strftime('%Y-%m-%d %H:%M')
