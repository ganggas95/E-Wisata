from flask import Flask
from .settings import *
from .extension import *

app = Flask(__name__)

app.config.from_object(Base)
app.config.from_object(Database)
app.config.from_object(UserBaseSetting)

db.init_app(app)
login.init_app(app)
migrate.init_app(app, db)
csrf.init_app(app)

login.login_view = app.config['USER_LOGIN_VIEW']