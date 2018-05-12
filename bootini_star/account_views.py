"""
Application views/routes are based on Flask's MethodView. All primary views are
combined into a Flask blueprint.
"""
__author__ = 'Ralph Seichter'

from urllib.parse import urljoin, urlparse
from uuid import uuid4

import flask_login
from flask import flash, redirect, request, url_for
from flask.templating import render_template
from flask.views import MethodView
from flask_login.utils import current_user
from mongoengine import MongoEngineConnectionError

from bootini_star.views import flash_form_errors
from .email import RegistrationMail
from .extensions import app_config, db, log, pwd_context
from .forms import ChangePasswordForm, LoginForm, SelfDestructForm, SignupForm
from .models import User, UserLevel
from .models import request_loader, user_loader

ACCOUNT_DELETE_FAILED = 'Unable to delete your account.'
ACCOUNT_DELETED = 'Your account has been deleted.'
LOGIN_FAILED = 'Your login was not successful.'
PASSWORD_CHANGED = 'Your password was changed.'
PASSWORD_MISTYPED = 'You may have mistyped your current password.'
YOU_LOGGED_OUT = 'You are logged out.'


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    target_url = urlparse(urljoin(request.host_url, target))
    log.debug('ref netloc: ' + ref_url.netloc)
    log.debug('target netloc: ' + target_url.netloc)
    return (target_url.scheme in ('http', 'https')) \
           and ref_url.netloc.casefold() == target_url.netloc.casefold()


class InvalidUsageError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        super()
        self.message = message
        if status_code:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class Signup(MethodView):
    methods = ['GET', 'POST']

    @staticmethod
    def get():
        return render_template('quickform.html', form=SignupForm())

    # noinspection PyTypeChecker
    @staticmethod
    def post():
        form = SignupForm()
        if not form.validate_on_submit():
            flash_form_errors(form)
            return render_template('quickform.html', form=form)
        email = form.email.data.strip()
        password = form.password.data
        user = User()
        user.email = email
        user.uuid = str(uuid4())
        user.activation_token = str(uuid4())
        user.password = pwd_context.hash(password)
        user.level = UserLevel.REGISTERED
        user.save()
        log.info(f'User {user.uuid} signed up')
        headers = {'From': app_config['SMTP_SENDER_ADDRESS'], 'To': email}
        RegistrationMail().send(headers, url_for('.activate', _external=True,
                                                 email=email,
                                                 token=user.activation_token))
        flash('Registration successful, an activation email has been sent.',
              'success')
        return redirect(url_for('.index'))


class ChangePassword(MethodView):
    methods = ['GET', 'POST']

    @flask_login.login_required
    def get(self):
        return render_template('quickform.html', form=ChangePasswordForm())

    @flask_login.login_required
    def post(self):
        form = ChangePasswordForm()
        if not form.validate_on_submit():
            flash_form_errors(form)
            return render_template('quickform.html', form=form)
        if not pwd_context.verify(form.current.data, current_user.password):
            flash(PASSWORD_MISTYPED, 'warning')
            return render_template('quickform.html', form=form)
        email = current_user.email
        try:
            count = User.objects(email=email).update_one(
                set__password=(pwd_context.hash(form.password.data)))
            if count > 0:
                log.info(f'User {email} changed password')
                flash(PASSWORD_CHANGED, 'success')
            else:
                log.warning(f'Unable to change password for {email}')
                flash(f'Unable to change password.', 'danger')
        except MongoEngineConnectionError as e:
            log.error(f'Error changing password: {e}')
            flash(f'Unable to change password.', 'danger')
        return redirect(url_for('.dashboard'))


class SelfDestruct(MethodView):
    methods = ['GET', 'POST']

    @flask_login.login_required
    def get(self):
        return render_template('selfdestruct.html', form=SelfDestructForm())

    @flask_login.login_required
    def post(self):
        form = SelfDestructForm()
        if not form.validate_on_submit():
            flash_form_errors(form)
            return render_template('selfdestruct.html', form=form)
        email = current_user.email
        flask_login.logout_user()
        try:
            count = User.objects(email=email).delete()
            if count > 0:
                log.info(f'User {email} deleted')
                flash(ACCOUNT_DELETED, 'success')
                return redirect(url_for('.index'))
            else:
                log.warning(f'User {email} could not be deleted')
        except MongoEngineConnectionError as e:
            log.error(f'Error deleting account: {e}')
        flash(ACCOUNT_DELETE_FAILED, 'danger')
        return redirect(url_for('.index'))


class Activate(MethodView):
    methods = ['GET']

    @staticmethod
    def get(email, token):
        user = User.objects(email=email, activation_token=token).first()
        if user:
            user.activation_token = ''
            user.level = UserLevel.DEFAULT
            try:
                user.save()
                log.info(f'User {user.uuid} activated account')
                flash('Your account is now active, please login.', 'success')
                return redirect(url_for('.login'))
            except MongoEngineConnectionError as e:
                log.error(f'Account activation failed: {e}')
        flash('Account activation failed.', 'danger')
        return redirect(url_for('.index'))


class Login(MethodView):
    methods = ['GET', 'POST']

    @staticmethod
    def get():
        return render_template('quickform.html', form=LoginForm())

    # noinspection PyTypeChecker
    @staticmethod
    def post():
        form = LoginForm()
        if not form.validate_on_submit():
            flash_form_errors(form)
            return render_template('quickform.html', form=form)
        user = request_loader(request)
        if user:
            flask_login.login_user(user)
            nxt = request.args.get('next')
            if nxt:
                if not is_safe_url(nxt):
                    raise InvalidUsageError(f'Unsafe redirect target: {nxt}')
            return redirect(nxt or url_for('.dashboard'))
        flash(LOGIN_FAILED, 'danger')
        return redirect(url_for('.login'))


class Logout(MethodView):
    methods = ['GET']

    @flask_login.login_required
    def get(self):
        log.info(f'User {current_user.uuid} logged out')
        flask_login.logout_user()
        flash(YOU_LOGGED_OUT, 'success')
        return redirect(url_for('.index'))


def add_account_url_rules(blueprint):
    blueprint.add_url_rule('/activate/<string:email>/<string:token>',
                           view_func=Activate.as_view('activate'))
    blueprint.add_url_rule('/login', view_func=Login.as_view('login'))
    blueprint.add_url_rule('/logout', view_func=Logout.as_view('logout'))
    blueprint.add_url_rule('/password',
                           view_func=ChangePassword.as_view('password'))
    blueprint.add_url_rule('/selfdestruct',
                           view_func=SelfDestruct.as_view('selfdestruct'))
    blueprint.add_url_rule('/signup', view_func=Signup.as_view('signup'))
