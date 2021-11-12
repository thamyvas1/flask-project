from flask.app import Flask
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import (StringField, SubmitField, BooleanField, 
                    DateField, RadioField, SelectField, 
                    TextField, TextAreaField)
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired



class AddForm(FlaskForm):

    name = StringField("Name of Owner: ")
    pup_id = IntegerField("Puppy's id")
    submit = SubmitField('Add Owner!')  