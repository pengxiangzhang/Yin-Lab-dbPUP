from flask_wtf import Form, RecaptchaField, Recaptcha
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError
from flask_wtf.file import FileField, FileRequired


class InputForm(Form):
    recaptcha = RecaptchaField(validators=[Recaptcha(message="Please complete the Recaptcha")])
