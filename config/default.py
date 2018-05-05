# coding: utf-8
import os


PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
class Config(object):
    """Base config class."""
    # Flask app config
    DEBUG = False
    TESTING = False

    SECRET_KEY = "abcdef12345"

    # Root path of project
    PROJECT_PATH = PROJECT_PATH

    # SQLAlchemy config
    # See:
    # https://pythonhosted.org/Flask-SQLAlchemy/config.html#connection-uri-format
    # http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#database-urls
    SQLALCHEMY_DATABASE_URI = "postgresql://user:password@host/database"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-DebugToolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Sentry config
    JSON_AS_ASCII = False
