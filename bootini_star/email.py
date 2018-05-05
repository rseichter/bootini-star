"""
Support classes for sending email to application users.
"""
__author__ = 'Ralph Seichter'

import re
import smtplib
from email.message import EmailMessage
from email.utils import localtime
from urllib.parse import urlparse
from uuid import uuid4

import bootini_star
from .extensions import app_config, log


class _Mail(object):

    def _parse_config(self):
        u = urlparse(app_config['SMTP_SERVER_URI'])
        if not u.scheme in ['smtp', 'tls']:
            raise ValueError('SMTP_SERVER_URI missing or scheme unknown')
        self.scheme = u.scheme
        self.host = u.hostname
        if u.port:
            self.port = u.port
        else:
            self.port = 587 if u.scheme == 'tls' else 25
        if u.path:
            self.username = re.sub(r'^/(.+)', r'\1', u.path)
            self.password = u.query
        else:
            self.username = None
        self.address = app_config['SMTP_SENDER_ADDRESS']
        if re.search(bootini_star.email_pat, self.address):
            return
        raise ValueError('SMTP_SENDER_ADDRESS missing or malformed')

    def send(self, headers, body):
        self._parse_config()
        log.debug('SMTP host is ' + self.host + ':' + str(self.port))
        if self.username:
            log.debug('SMTP username is ' + self.username)
        headers['Date'] = localtime()
        headers['Message-ID'] = str(uuid4()) + '@Bootini-Star'
        em = EmailMessage()
        for k, v in headers.items():
            em[k] = v
        em.set_content(body)
        with smtplib.SMTP(self.host, self.port) as smtp:
            # smtp.set_debuglevel(1)
            if self.username:
                smtp.starttls()
                smtp.login(self.username, self.password)
            smtp.send_message(em)


class RegistrationMail(_Mail):

    def send(self, headers, url):
        headers['Subject'] = 'Your Bootini Star account has been created'
        body = (
            'Somebody (hopefully you) registered your email address with a'
            '\nBootini Star account. To activate your account, please click'
            '\nthe following link:\n\n'
        )
        super().send(headers, body + url)
