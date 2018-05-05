"""
Application views/routes are based on Flask's MethodView. All primary views are
combined into a Flask blueprint.
"""
__author__ = 'Ralph Seichter'

import json
import re
from operator import attrgetter
from urllib.parse import urljoin, urlparse
from uuid import uuid4

import flask_login
from flask import Blueprint, flash, redirect, request, url_for
from flask.templating import render_template
from flask.views import MethodView, View
from flask_login.utils import current_user

import swagger_client
from swagger_client.rest import ApiException
from .email import RegistrationMail
from .esi import IdNameCache
from .extensions import app_config, db, log, login_manager, pwd_context
from .forms import LoginForm, SignupForm
from .models import User, character_list_loader, user_loader
from .sso import EveSso

eveCache = IdNameCache()


class InvalidUsage(Exception):
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

    def get(self):
        return render_template('signup.html', form=SignupForm())

    def post(self):
        form = SignupForm()
        if not form.validate_on_submit():
            flash_form_errors(form)
            return render_template('signup.html', form=form)
        email = form.email.data.strip()
        password = form.password.data
        token = str(uuid4())
        user = User(email, password, str(uuid4()), level=User.valid_levels[
            'registered'], activation_token=token)
        db.session.add(user)
        db.session.commit()
        headers = {'From': app_config['SMTP_SENDER_ADDRESS'], 'To': email}
        RegistrationMail().send(headers, url_for(
            '.activate', _external=True, email=email, token=token))
        flash(
            'Registration successful. Please check your inbox for an activation email.',
            'success')
        return redirect(url_for('.index'))


def flash_form_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(error, 'danger')


class Activate(MethodView):
    methods = ['GET']

    def get(self, email, token):
        user = user_loader(email)
        if user and user.activation_token == token:
            user.activation_token = ''
            user.level = user.valid_levels['default']
            try:
                db.session.merge(user)
                db.session.commit()
                flash('Your account is now active, please login.', 'success')
                return redirect(url_for('.login'))
            except Exception as e:
                log.error('Account activation failed: {0}'.format(e))
        flash('Account activation failed.', 'danger')
        return redirect(url_for('.index'))


class Login(MethodView):
    methods = ['GET', 'POST']

    def get(self):
        return render_template('login.html', form=LoginForm())

    def post(self):
        form = LoginForm()
        if not form.validate_on_submit():
            flash_form_errors(form)
            return render_template('login.html', form=form)
        user = request_loader(request)
        if user:
            flask_login.login_user(user)
            nxt = request.args.get('next')
            if nxt:
                if not is_safe_url(nxt):
                    log.debug(nxt + ' is unsafe')
                    raise InvalidUsage('Naughty redirect attempted')
                log.debug(nxt + ' is safe')
            return redirect(nxt or url_for('.dashboard'))
        flash('Your login was not successful.', 'danger')
        return redirect(url_for('.login'))


class Logout(MethodView):
    methods = ['GET']

    @flask_login.login_required
    def get(self):
        flask_login.logout_user()
        flash('You are logged out.', 'success')
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
            rv = api.get_characters_character_id(character_id)
        except ApiException as e:
            return api_fail(e)
        return render_template('character.html', character=rv)


def refresh_token(api, cc):
    es = EveSso(json.loads(cc.token_str))
    token_dict, is_new_token = es.refresh_token()
    if is_new_token:  # pragma: no cover (Can't test without valid tokens)
        cc.set_token(token_dict)
        db.session.merge(cc)
        db.session.commit()
    client = api.api_client
    client.set_default_header('User-Agent', 'BootiniStar/0.0.1')
    client.configuration.access_token = token_dict['access_token']
    return token_dict


def api_fail(api_exception):
    flash('EVE Swagger Interface call failed: ' +
          api_exception.reason + '.', 'danger')
    return redirect(url_for('.index'))


class MailList(MethodView):
    methods = ['GET']

    @flask_login.login_required
    def get(self, character_id):
        cc = current_user.load_character(character_id)
        if cc:  # pragma: no cover (Never true without valid tokens in DB)
            api = swagger_client.MailApi()
            refresh_token(api, cc)
            try:
                rv = api.get_characters_character_id_mail(character_id)
                return render_template('maillist.html', eveCache=eveCache,
                                       character_id=character_id,
                                       maillist=sorted(rv, key=attrgetter(
                                           'timestamp'), reverse=True))
            except ApiException as e:
                return api_fail(e)
        else:
            flash('Please select one of your characters.', 'warning')
        return redirect(url_for('.dashboard'))


class Mail(MethodView):
    methods = ['GET']

    @flask_login.login_required
    def get(self, args):
        x = args.split(',')
        character_id = int(x[0])
        mail_id = int(x[1])
        cc = current_user.load_character(character_id)
        if cc:
            api = swagger_client.MailApi()
            refresh_token(api, cc)
            try:  # pragma: no cover (Needs valid tokens)
                rv = api.get_characters_character_id_mail_mail_id(
                    character_id, mail_id)
                return render_template('mail.html', eveCache=eveCache, mail=rv)
            except ApiException as e:  # pragma: no cover (Needs valid tokens)
                return api_fail(e)
        else:
            flash('Please select one of your characters.', 'warning')
        return redirect(url_for('.dashboard'))


class RemoveMail(MethodView):
    methods = ['GET']

    @flask_login.login_required
    def get(self, args):
        x = args.split(',')
        character_id = int(x[0])
        mail_id = int(x[1])
        cc = current_user.load_character(character_id)
        if cc:  # pragma: no cover (Needs valid tokens)
            api = swagger_client.MailApi()
            refresh_token(api, cc)
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
            flash('Character ' + cc.name + ' was removed.', 'success')
        else:
            flash('Please select one of your characters.', 'warning')
        return redirect(url_for('.dashboard'))


class Skills(MethodView):
    methods = ['GET']

    @flask_login.login_required
    def get(self, character_id):
        cc = current_user.load_character(character_id)
        if cc:  # pragma: no cover (Needs valid tokens)
            api = swagger_client.SkillsApi()
            refresh_token(api, cc)
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
blueprint.add_url_rule('/dashboard', view_func=Dashboard.as_view('dashboard'))
blueprint.add_url_rule('/dashboard/rm/<int:character_id>',
                       view_func=RemoveCharacter.as_view('rmcharacter'))
blueprint.add_url_rule('/login', view_func=Login.as_view('login'))
blueprint.add_url_rule('/logout', view_func=Logout.as_view('logout'))
blueprint.add_url_rule('/signup', view_func=Signup.as_view('signup'))
blueprint.add_url_rule('/character/<int:character_id>',
                       view_func=Character.as_view('character'))
blueprint.add_url_rule('/mail/<string:args>', view_func=Mail.as_view('mail'))
blueprint.add_url_rule('/mail/rm/<string:args>',
                       view_func=RemoveMail.as_view('rmmail'))
blueprint.add_url_rule('/maillist/<int:character_id>',
                       view_func=MailList.as_view('maillist'))
blueprint.add_url_rule('/skillqueue/<int:character_id>',
                       view_func=Skills.as_view('skillqueue'))


@login_manager.request_loader
def request_loader(req):
    email = req.form.get('email')
    user = user_loader(email)
    if user:
        if user.may_login():
            if req.form['password']:
                if pwd_context.verify(req.form['password'], user.password):
                    log.info("User '%s' (level %d) logged in" %
                             (user.email, user.level))
                    return user
                else:
                    log.warning("User '%s' password mismatch" % user.email)
            else:
                log.error('No password in request object')
        else:
            log.warning("User '%s' may not login (level %d)" %
                        (user.email, user.level))
    elif email:
        log.warning("Unknown user '%s'" % email)
    return None
