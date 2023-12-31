#inicializar
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os






app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] =os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = "5edace8fdc83b69d050b20fb890bec722dc5b8254ffd5abb3cfe5b05e4b838dd"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

from fakepinterest import routes