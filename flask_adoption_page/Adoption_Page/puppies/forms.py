from flask.app import Flask
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import (StringField, SubmitField, BooleanField, 
                    DateField, RadioField, SelectField, 
                    TextField, TextAreaField)
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):

    pup = StringField("Name of Puppy: ")
    submit = SubmitField('Add Puppy!')


class DelForm(FlaskForm):

    id = IntegerField("Puppy's id to be Removed")
    submit = SubmitField('Remove Puppy!')