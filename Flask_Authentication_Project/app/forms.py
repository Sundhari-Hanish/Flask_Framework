from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User
from app import db
import sqlalchemy as sa
class LoginForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired()])
    password=PasswordField("Password", validators=[DataRequired()])
    remember_me=BooleanField("Remember Me")
    submit=SubmitField("Sign In")
class RegistrationForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired()])
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField('Repeat Password',validators=[DataRequired(), EqualTo('password', message="Passwords must match")])
    submit=SubmitField("Register")
    def validate_username(self,username):
        user=db.session.scalar(sa.select(User).where(User.username==username.data))
        if user:
            raise ValidationError("Username already exists")
    def validate_email(self,email):
        user=db.session.scalar(sa.select(User).where(User.email==email.data))
        if user:
            raise ValidationError("Email alreay exists")
