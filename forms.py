from flask_wtf import FlaskForm, RecaptchaField, Recaptcha
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError
from flask_wtf.file import FileField, FileRequired


class InputForm(FlaskForm):
    recaptcha = RecaptchaField(validators=[Recaptcha(message="Please complete the Recaptcha")])
