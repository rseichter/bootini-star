"""
Callback view for EVE SSO.
"""
__author__ = 'Ralph Seichter'

import flask_login
from flask import Blueprint, redirect, request, url_for
from flask.helpers import flash
from flask.views import MethodView
from flask_login import current_user

from .extensions import db
from .models import Character
from .sso import EveSso


class Callback(MethodView):
    methods = ['GET']

    @flask_login.login_required
    def get(self):
        es = EveSso()
        try:
            auth_token = es.auth_token(request.args.get('code'))
        except:
            flash('Error obtaining authentication token.', 'danger')
            return redirect(url_for('bs.dashboard'))
        """
        The rest of this method is not covered by automated unit tests because
        it would require user interaction to authorise a character.
        """
        resp = es.auth_verify()  # pragma: no cover
        if resp.ok:  # pragma: no cover
            json = resp.json()
            character = Character(
                current_user.uuid,
                json['CharacterID'],
                json['CharacterName'],
                json['CharacterOwnerHash']
            )
            character.set_token(auth_token)
            db.session.merge(character)
            db.session.commit()
            flash('Verification successful.', 'success')
            return redirect(url_for('bs.dashboard'))
        else:  # pragma: no cover
            flash('Verification failed.', 'error')
            return redirect(url_for('bs.index'))


blueprint = Blueprint('sso', __name__)
blueprint.add_url_rule('/sso/callback', view_func=Callback.as_view('callback'))
