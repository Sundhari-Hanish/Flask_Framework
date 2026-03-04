from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email
class EventForm(FlaskForm):
    full_name = StringField("Full Name", validators=[
        DataRequired(),
        Length(min=3, max=50)
    ])
    email = EmailField("Email", validators=[
        DataRequired(),
        Email()
    ])
    tech_domain = SelectField("Tech Domain", choices=[
        ("AI", "Artificial Intelligence"),
        ("Web", "Web Development"),
        ("Cyber", "Cyber Security"),
        ("Cloud", "Cloud Computing")
    ], validators=[DataRequired()])
    submit = SubmitField("Register")
