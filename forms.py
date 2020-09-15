from flask_wtf import Form,RecaptchaField,Recaptcha
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

class ContactForm(Form):
    name = TextField("Name",[validators.Required("Please enter your name.")])
    email = TextField("Email",[validators.Required("Please enter your vaild email address."),validators.Email("Please enter your email address.")])
    subject = TextField("subject",[validators.Required("Please enter the subject.")])
    message = TextField("message",[validators.Required("Please enter the message.")])
    recaptcha = RecaptchaField(validators=[Recaptcha(message="Please complete the Recaptcha")])
    submit = SubmitField("submit")