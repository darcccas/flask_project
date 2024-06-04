from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [Email(message=('Incorrect address')), DataRequired()])
    body = TextAreaField('Your message', [DataRequired(),
                                        Length(min=10,
                                        message=('To short text.'))])
    submit = SubmitField('Submit')