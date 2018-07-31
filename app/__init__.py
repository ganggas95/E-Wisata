from flask_user import UserManager

from .create_app import (
    app,
    db
)
from .user_app import (
    user_blueprint,
    User,
    Role,
    UsersRoles
)
from .auth_app import auth_blueprint
from .dashboard_app import dashboard_blueprint
from .wisata_app import wisata_blueprint
from .loader import *


user_manager = UserManager(app, db, User)

app.register_blueprint(user_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(dashboard_blueprint)
app.register_blueprint(wisata_blueprint)
