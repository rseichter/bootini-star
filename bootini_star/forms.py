"""
Flask forms for logging in and signing up.
"""
__author__ = 'Ralph Seichter'

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email address', validators=[
        Email(message='Valid email address is required.')])
    password = PasswordField('Password', validators=[
        DataRequired('Password is required.')])
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    email = StringField('Email address', validators=[
        Email(message='Valid email address is required.')])
    password = PasswordField('Password', validators=[
        DataRequired('Password is required.')])
    confirm = PasswordField('Confirm password', validators=[
        DataRequired('Password confirmation is required.'),
        EqualTo('password', message='Password and confirmation must match.')
    ])
    submit = SubmitField('Sign me up')
