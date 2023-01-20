from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError

# Forms criado conforme o tutorial do site la.
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField, DateField, SearchField
# from wtforms.validators import Length, EqualTo, DataRequired, ValidationError, data_required

# class TodoForm(FlaskForm):
#     task_name = StringField('Name', validators=[DataRequired()])
#     description = StringField('Description', validators=[DataRequired()])
#     initial_date = DateField('Initial Date', validators=[DataRequired()])
#     due_date = DateField('Due Date', validators=[DataRequired()])
#     status = SearchField('Status', choices=[('Complete','Complete'),('Not Started', 'Not Started')])
#     submit = SubmitField('Add Task')