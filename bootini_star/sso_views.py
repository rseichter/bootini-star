"""
Callback view for EVE SSO.
"""
__author__ = 'Ralph Seichter'

import flask_login
from flask import Blueprint, redirect, request, url_for
from flask.helpers import flash
from flask.views import MethodView
from flask_login import current_user

from .extensions import log
from .models import Character, save_user
from .sso import EveSso


class Callback(MethodView):
    methods = ['GET']

    @flask_login.login_required
    def get(self):
        es = EveSso()
        # noinspection PyBroadException,PyPep8
        try:
            auth_token = es.auth_token(request.args.get('code'))
        except:
            flash('Error obtaining authentication token.', 'danger')
            return redirect(url_for('bs.dashboard'))
        """
        The rest of this method is not covered by automated unit tests because
        it would require user interaction to authorise a character.
        """
        resp = es.auth_verify()
        if resp.ok:
            json = resp.json()
            character = Character()
            character.id = json['CharacterID']
            character.name = json['CharacterName']
            character.set_token(auth_token)
            current_user.characters.append(character)
            save_user(current_user)
            log.info(
                f'User {current_user.email} added character {character.id}')
            flash('Verification successful.', 'success')
            return redirect(url_for('bs.dashboard'))
        else:
            flash('Verification failed.', 'error')
            return redirect(url_for('bs.index'))


blueprint = Blueprint('sso', __name__)
blueprint.add_url_rule('/sso/callback', view_func=Callback.as_view('callback'))
