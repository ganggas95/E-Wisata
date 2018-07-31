from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    validators
)


class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[validators.DataRequired()],
        render_kw={
            'class': 'form-control',
            'placeholder': 'Username',
            'required': True
        }
    )
    password = PasswordField(
        'Password',
        validators=[validators.DataRequired()],
        render_kw={
            'class': 'form-control',
            'placeholder': 'Password',
            'required': True
        }
    )
    remember = BooleanField(
        'Remember me!'
    )
    