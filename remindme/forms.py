from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError
from remindme.models import User, Task

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username already exists!")

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError("Email already exists!")

    username = StringField(label="User Name:", validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label="Email:", validators=[DataRequired()])
    password1 = PasswordField(label="Password:", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label="Confirm Password:", validators=[EqualTo("password1"), DataRequired()])
    submit = SubmitField(label="Create Account")

class LoginForm(FlaskForm):
    username = StringField(label="User Name", validators=[DataRequired()])
    password = StringField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Login")
    
class CreateTask(FlaskForm):
    task_name = StringField(label="Task: ", validators=[Length(min=2, max=30), DataRequired()])
    description = StringField(label="Description: ", validators=[Length(min=2, max=250), DataRequired()])
    conclusion_date = DateField(label="Start Date: ", format= "%d=%m-%Y", validators =[DataRequired()])
    submit = SubmitField(label="Create")

class EditTask(FlaskForm):
    task_name = StringField(label="Task: ", validators=[Length(min=2, max=30), DataRequired()])
    description = StringField(label="Description: ", validators=[Length(min=2, max=250), DataRequired()])
    conclusion_date = DateField(label="Start Date: ", format= "%d=%m-%Y", validators =[DataRequired()])
    submit = SubmitField(label="Edit")

class DeleteTask(FlaskForm):
    submit = SubmitField(label="Delete")

