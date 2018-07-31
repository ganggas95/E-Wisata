from .create_app import login
from .user_app import User


@login.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)
