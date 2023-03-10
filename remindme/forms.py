from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField, TextAreaField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError, InputRequired, Email
from datetime import datetime
from remindme.models import User

today = datetime.today()

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Nome de usuário já existe!")

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError("Email já existe!")

    username = StringField(label="Usuário:", validators=[InputRequired(), Length(min=2, max=30), DataRequired()])
    email_address = EmailField(label="Email:", validators=[InputRequired(), Length(min=6,max=30), DataRequired(), Email()])
    password1 = PasswordField(label="Senha:", validators=[InputRequired(), Length(min=6,max=30), DataRequired()])
    password2 = PasswordField(label="Confirme a Senha:", validators=[EqualTo("password1"), DataRequired()])
    submit = SubmitField(label="Criar Conta")

class LoginForm(FlaskForm):
    username = StringField(label="Usuário", validators=[InputRequired(), Length(min=2,max=30), DataRequired()])
    password = PasswordField(label="Senha", validators=[InputRequired(), Length(min=6,max=30), DataRequired()])
    submit = SubmitField(label="Login")

class CreateTask(FlaskForm):
    task_name = StringField(label="Tarefa: ", validators=[InputRequired(), Length(min=2, max=30), DataRequired()])
    description = TextAreaField(label="Descrição: ", validators=[InputRequired(), Length(min=2, max=250), DataRequired()])
    submit = SubmitField("Nova Tarefa")

class EditTask(FlaskForm):
    task_name = StringField(label="Tarefa: ", validators=[InputRequired(), Length(min=2, max=30), DataRequired()])
    description = TextAreaField(label="Descrição: ", validators=[InputRequired(), Length(min=2, max=250), DataRequired()])
    submit = SubmitField("Editar")

class EditDoneTask(FlaskForm):
    done_submit = SubmitField(label="Feito")
    undone_submit = SubmitField(label="Pendente")

class DeleteTask(FlaskForm):
    submit = SubmitField("Deletar")