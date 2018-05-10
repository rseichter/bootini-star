"""
Application views/routes are based on Flask's MethodView. All primary views are
combined into a Flask blueprint.
"""
__author__ = 'Ralph Seichter'

import json
from operator import attrgetter
from urllib.parse import urljoin, urlparse
from uuid import uuid4

import flask_login
from flask import Blueprint, flash, redirect, request, url_for
from flask.templating import render_template
from flask.views import MethodView, View
from flask_login.utils import current_user
from sqlalchemy.exc import SQLAlchemyError

import swagger_client
from bootini_star import esi
from swagger_client.rest import ApiException
from .email import RegistrationMail
from .extensions import app_config, db, log, pwd_context
from .forms import ChangePasswordForm, LoginForm, SelfDestructForm, SignupForm
from .models import User, character_list_loader, request_loader, user_loader
from .sso import EveSso

ACCOUNT_DELETE_FAILED = 'Unable to delete your account.'
ACCOUNT_DELETED = 'Your account has been deleted.'
LOGIN_FAILED = 'Your login was not successful.'
PASSWORD_CHANGED = 'Your password was changed.'
PASSWORD_MISTYPED = 'You may have mistyped your current password.'
YOU_LOGGED_OUT = 'You are logged out.'

eveCache = esi.IdNameCache()


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


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    target_url = urlparse(urljoin(request.host_url, target))
    log.debug('ref netloc: ' + ref_url.netloc)
    log.debug('target netloc: ' + target_url.netloc)
    return (target_url.scheme in ('http',
                                  'https')) and ref_url.netloc.casefold() == target_url.netloc.casefold()


class RenderTemplate(View):

    def __init__(self, template):
        self.template = template

    def dispatch_request(self):
        return render_template(self.template, config=app_config)


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
        token = str(uuid4())
        user = User(email, password, str(uuid4()), level=User.valid_levels[
            'registered'], activation_token=token)
        db.session.add(user)
        db.session.commit()
        log.info(f'User {user.uuid} signed up')
        headers = {'From': app_config['SMTP_SENDER_ADDRESS'], 'To': email}
        RegistrationMail().send(headers, url_for(
            '.activate', _external=True, email=email, token=token))
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
        current = form.current.data
        password = form.password.data
        if pwd_context.verify(current, current_user.password):
            current_user.password = pwd_context.hash(password)
            try:
                db.session.merge(current_user)
                db.session.commit()
                log.info(f'User {current_user.uuid} changed password')
                flash(PASSWORD_CHANGED, 'success')
                return redirect(url_for('.dashboard'))
            except SQLAlchemyError as e:
                log.error(f'Error changing your password: {e}')
        flash(PASSWORD_MISTYPED, 'warning')
        return render_template('quickform.html', form=form)


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
        user = request_loader(request)
        if user:
            uuid = user.uuid
            flask_login.logout_user()
            try:
                user.delete_characters()
                db.session.delete(user)
                db.session.commit()
                log.info(f'User {uuid} deleted account')
                flash(ACCOUNT_DELETED, 'success')
                return redirect(url_for('.index'))
            except SQLAlchemyError as e:
                log.error(f'Error deleting account: {e}')
        flash(ACCOUNT_DELETE_FAILED, 'danger')
        return redirect(url_for('.index'))


def flash_form_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(error, 'danger')


class Activate(MethodView):
    methods = ['GET']

    @staticmethod
    def get(email, token):
        user = user_loader(email)
        if user and user.activation_token == token:
            user.activation_token = ''
            user.level = user.valid_levels['default']
            try:
                db.session.merge(user)
                db.session.commit()
                log.info(f'User {user.uuid} activated account')
                flash('Your account is now active, please login.', 'success')
                return redirect(url_for('.login'))
            except SQLAlchemyError as e:
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


class Dashboard(MethodView):
    methods = ['GET']

    @flask_login.login_required
    def get(self):
        characters = character_list_loader(flask_login.current_user.uuid)
        auth_url, auth_state = EveSso().auth_url_state()
        return render_template(
            'dashboard.html',
            characters=sorted(characters, key=attrgetter('name')),
            auth_url=auth_url,
            auth_state=auth_state,
            config=app_config
        )


class Character(MethodView):
    methods = ['GET']

    @flask_login.login_required
    def get(self, character_id):
        api = swagger_client.CharacterApi()
        try:
            return render_template('character.html',
                                   character=esi.get_character(api,
                                                               character_id))
        except ApiException as e:
            return api_fail(e)


def refresh_token(api, current_character):
    es = EveSso(json.loads(current_character.token_str))
    rt = es.refresh_token()
    if rt.token_changed:
        current_character.set_token(rt.token)
        db.session.merge(current_character)
        db.session.commit()
    client = api.api_client
    client.set_default_header('User-Agent', app_config['USER_AGENT'])
    client.configuration.access_token = rt.token['access_token']
    return api


def mail_api(current_character):
    return refresh_token(swagger_client.MailApi(), current_character)


def skills_api(current_character):
    return refresh_token(swagger_client.SkillsApi(), current_character)


def api_fail(api_exception):
    flash('EVE Swagger Interface call failed: ' +
          api_exception.reason + '.', 'danger')
    return redirect(url_for('.index'))


class MailList(MethodView):
    methods = ['GET']

    @flask_login.login_required
    def get(self, character_id, label=None):
        cc = current_user.load_character(character_id)
        if cc:  # pragma: no cover (Needs live character)
            api = mail_api(cc)
            kwargs = {'labels': [label]} if isinstance(label, int) else {}
            try:
                labels = esi.get_mail_labels(api, character_id)
                mails = esi.get_mail_list(api, character_id, **kwargs)
                mail_ids = set()
                for mail in mails:
                    mail_ids.add(mail._from)
                eveCache.eve_characters(mail_ids)
            except ApiException as e:
                return api_fail(e)
            sl = sorted(labels.labels, key=attrgetter('label_id'))
            sm = sorted(mails, key=attrgetter('timestamp'), reverse=True)
            return render_template('maillist.html', eveCache=eveCache,
                                   character_id=character_id, labels=sl,
                                   maillist=sm)
        else:
            flash('Please select one of your characters.', 'warning')
        return redirect(url_for('.dashboard'))


class Mail(MethodView):
    methods = ['GET']

    @flask_login.login_required
    def get(self, character_id: int, mail_id: int):
        cc = current_user.load_character(character_id)
        if cc:
            api = mail_api(cc)
            try:
                rv = api.get_characters_character_id_mail_mail_id(
                    character_id, mail_id)
                return render_template('mail.html', eveCache=eveCache, mail=rv)
            except ApiException as e:
                return api_fail(e)
        else:
            flash('Please select one of your characters.', 'warning')
        return redirect(url_for('.dashboard'))


class RemoveMail(MethodView):
    methods = ['GET']

    @flask_login.login_required
    def get(self, character_id: int, mail_id: int):
        cc = current_user.load_character(character_id)
        if cc:  # pragma: no cover (Needs live character)
            api = mail_api(cc)
            try:
                api.delete_characters_character_id_mail_mail_id(
                    character_id, mail_id)
                flash('Mail has been deleted.', 'success')
            except ApiException as e:
                return api_fail(e)
            return redirect(url_for('.maillist', character_id=character_id))
        else:
            flash('Please select one of your characters.', 'warning')
        return redirect(url_for('.dashboard'))


class RemoveCharacter(MethodView):
    methods = ['GET']

    @flask_login.login_required
    def get(self, character_id):
        cc = current_user.load_character(character_id)
        if cc:
            db.session.delete(cc)
            db.session.commit()
            log.info(
                f'User {current_user.uuid} removed character {character_id}')
            flash('Character ' + cc.name + ' was removed.', 'success')
        else:
            flash('Please select one of your characters.', 'warning')
        return redirect(url_for('.dashboard'))


class Skills(MethodView):
    methods = ['GET']

    @flask_login.login_required
    def get(self, character_id):
        cc = current_user.load_character(character_id)
        if cc:  # pragma: no cover (Needs live character)
            api = skills_api(cc)
            try:
                rv = api.get_characters_character_id_skillqueue(character_id)
                return render_template('skillqueue.html', eveCache=eveCache,
                                       character_id=character_id,
                                       skillq=sorted(rv, key=attrgetter(
                                           'queue_position')))
            except ApiException as e:
                return api_fail(e)
        else:
            flash('Please select one of your characters.', 'warning')
        return redirect(url_for('.dashboard'))


blueprint = Blueprint('bs', __name__)
blueprint.add_url_rule(
    '/', view_func=RenderTemplate.as_view('index', template='index.html'))
blueprint.add_url_rule('/activate/<string:email>/<string:token>',
                       view_func=Activate.as_view('activate'))
blueprint.add_url_rule('/password',
                       view_func=ChangePassword.as_view('password'))
blueprint.add_url_rule('/dashboard', view_func=Dashboard.as_view('dashboard'))
blueprint.add_url_rule('/dashboard/rm/<int:character_id>',
                       view_func=RemoveCharacter.as_view('rmcharacter'))
blueprint.add_url_rule('/login', view_func=Login.as_view('login'))
blueprint.add_url_rule('/logout', view_func=Logout.as_view('logout'))
blueprint.add_url_rule('/signup', view_func=Signup.as_view('signup'))
blueprint.add_url_rule('/selfdestruct',
                       view_func=SelfDestruct.as_view('selfdestruct'))
blueprint.add_url_rule('/character/<int:character_id>',
                       view_func=Character.as_view('character'))
blueprint.add_url_rule(
    '/mail/<int:character_id>/<int:mail_id>', view_func=Mail.as_view('mail'))
blueprint.add_url_rule('/mail/rm/<int:character_id>/<int:mail_id>',
                       view_func=RemoveMail.as_view('rmmail'))
blueprint.add_url_rule('/maillist/<int:character_id>/<int:label>',
                       view_func=MailList.as_view('maillabel'))
blueprint.add_url_rule('/maillist/<int:character_id>',
                       view_func=MailList.as_view('maillist'))
blueprint.add_url_rule('/skillqueue/<int:character_id>',
                       view_func=Skills.as_view('skillqueue'))
