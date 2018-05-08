"""
Flask forms for logging in and signing up.
"""
__author__ = 'Ralph Seichter'

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

EMAIL_LABEL = 'Email address'
EMAIL_MSG = 'Valid email address is required.'
PW_LABEL = 'Password'
PW_MSG = 'Password is required.'


class LoginForm(FlaskForm):
    email = StringField(EMAIL_LABEL, validators=[Email(message=EMAIL_MSG)])
    password = PasswordField(PW_LABEL, validators=[DataRequired(PW_MSG)])
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    email = StringField(EMAIL_LABEL, validators=[Email(message=EMAIL_MSG)])
    password = PasswordField(PW_LABEL, validators=[DataRequired(PW_MSG)])
    confirm = PasswordField('Confirm password', validators=[
        DataRequired('Password confirmation is required.'),
        EqualTo('password', message='Password and confirmation must match.')
    ])
    submit = SubmitField('Sign me up')


class SelfDestructForm(FlaskForm):
    email = StringField(EMAIL_LABEL, validators=[Email(message=EMAIL_MSG)])
    password = PasswordField(PW_LABEL, validators=[DataRequired(PW_MSG)])
    # submit = SubmitField('Delete account')
