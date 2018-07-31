""" SETTING with object class """


class Base(object):
    DEBUG = True
    SECRET_KEY = 'b1sm1llah abcdefgh 1234567*&^%$()'
    PORT = 8001
    HOST = '0.0.0.0'
    ENV = 'development'


class Database(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:b1sm1llah@localhost/e_wisata_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class UserBaseSetting(object):
    # Flask-User settings
    USER_APP_NAME = "E-Wisata Application"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False      # Disable email authentication
    # USER_ENABLE_USERNAME = True    # Enable username authentication
    # USER_REQUIRE_RETYPE_PASSWORD = True    # Simplify register form
    USER_EMAIL_SENDER_EMAIL = 'subhannizar25@gmail.com'
    # USER_ENABLE_REGISTER = False
    USER_LOGIN_URL = '/login'
    USER_AFTER_LOGOUT_ENDPOINT="auth_blueprint.login_page"
    USER_AFTER_LOGIN_ENDPOINT="dashboard_blueprint.dashboard_page"
    USER_LOGIN_TEMPLATE = 'login_page.html'
    # USER_ENABLE_REMEMBER_ME=True
    USER_LOGIN_VIEW = 'auth_blueprint.login_page'
    