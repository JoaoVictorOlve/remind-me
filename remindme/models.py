from remindme import db, login_manager, bcrypt
from flask_login import UserMixin
from sqlalchemy.sql import func

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(length=30), unique=True, nullable=False)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    tasks = db.relationship("Task")

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode("utf-8")

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(150))
    description = db.Column(db.String(250))
    register_date = db.Column(db.DateTime(timezone=True), default=func.now())
    conclusion_date = db.Column(db.DateTime())
    done = db.Column(db.Boolean, nullable=False, default=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))


    