from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from Scrape.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, usernameToCheck):
        user = User.query.filter_by(username=usernameToCheck.data).first()
        if user:
            # print(f"user={user}")
            raise ValidationError(
                "Username taken. Please try a different one.")

    def validate_email(self, emailToCheck):
        emailAddress = User.query.filter_by(email=emailToCheck.data).first()
        print(f"emailAddress={emailAddress}")
        if emailAddress:
            # print(f"email={emailAddress}")
            raise ValidationError("Email taken. Please try a different one.")

    username = StringField(label='', validators=[
                           Length(min=2, max=30), DataRequired()])
    email = StringField(label='', validators=[Email(), DataRequired()])
    pwd1 = PasswordField(label='', validators=[Length(min=6), DataRequired()])
    pwd2 = PasswordField(label='', validators=[
                         EqualTo('pwd1'), DataRequired()])
    submit = SubmitField(label='Create Account')
