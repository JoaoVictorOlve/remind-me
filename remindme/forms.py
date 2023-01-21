from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, BooleanField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError
from datetime import datetime
from remindme.models import User, Task

today = datetime.today()

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username already exists!")

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError("Email already exists!")

    username = StringField(label="Usuário:", validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label="Email:", validators=[DataRequired()])
    password1 = PasswordField(label="Senha:", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label="Confirme a Senha:", validators=[EqualTo("password1"), DataRequired()])
    submit = SubmitField(label="Criar Conta")

class LoginForm(FlaskForm):
    username = StringField(label="Usuário", validators=[DataRequired()])
    password = StringField(label="Senha", validators=[DataRequired()])
    submit = SubmitField(label="Login")

class CreateTask(FlaskForm):
    task_name = StringField(label="Tarefa: ", validators=[Length(min=2, max=30), DataRequired()])
    description = StringField(label="Descrição: ", validators=[Length(min=2, max=250), DataRequired()])
    register_date = DateField(label="Data Cadastro: ", format= "%d=%m-%Y", validators =[DataRequired()], default=today)
    conclusion_date = DateField(label="Data Conclusão: ", format= "%d=%m-%Y", validators =[DataRequired()])
    done = BooleanField(label="Concluído?", validators=[DataRequired()])
    submit = SubmitField(label="Criar")

class EditTask(FlaskForm):
    task_name = StringField(label="Task: ", validators=[Length(min=2, max=30), DataRequired()])
    description = StringField(label="Description: ", validators=[Length(min=2, max=250), DataRequired()])
    conclusion_date = DateField(label="Start Date: ", format= "%d=%m-%Y", validators =[DataRequired()])
    submit = SubmitField(label="Edit")

class DeleteTask(FlaskForm):
    submit = SubmitField(label="Delete")

