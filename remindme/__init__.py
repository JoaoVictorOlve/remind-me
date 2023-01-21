from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.app_context().push()
app.config["SECRET_KEY"] = "dfbb233fe4b817c1070d47c9"

#string conexao
app.config['SQLALCHEMY_DATABASE_URI'] = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'postgresql',
    usuario = "remind",
    senha = "123456",
    servidor = "localhost:5435",
    database = "postgres"
)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from remindme import routes

