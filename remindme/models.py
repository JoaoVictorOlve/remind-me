from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from remindme import db, login_manager
from remindme import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(150))
    description = db.Column(db.String(250))
    register_date = db.Column(db.DateTime(timezone=True), default=func.now())
    conclusion_date = db.Column(db.DateTime())
    done = db.Column(db.Boolean, nullable=False, default=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    tasks = db.relationship("Task", backref="owned_user", lazy=True)

    # Essa linha estava no tutorial do site mas ate o momento nao entendi a aplicação dela
    # todos = db.relationship('TodoItem', backref='owner')
