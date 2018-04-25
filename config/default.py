# coding: utf-8
import os


PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
class Config(object):
    """Base config class."""
    # Flask app config
    DEBUG = False
    TESTING = False

    SECRET_KEY = "\xa3\xbfN\xf3T\xd6\xa1S\xf6y\xd2@\xccnn\x87R\x9fNY\xb5^\xf2\xf8"
    # PERMANENT_SESSION_LIFETIME = 3600 * 24 * 7
    # SESSION_COOKIE_NAME = 'scb_abacus_session'

    # Root path of project
    PROJECT_PATH = PROJECT_PATH

    # Site domain
    # SITE_TITLE = "Pali Dictionary"
    # SITE_DOMAIN = "http://localhost:8000"

    # SQLAlchemy config
    # See:
    # https://pythonhosted.org/Flask-SQLAlchemy/config.html#connection-uri-format
    # http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#database-urls
    SQLALCHEMY_DATABASE_URI = "postgresql://user:password@host/database"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Security
    # https://pythonhosted.org/Flask-Security/configuration.html
    # SECURITY_PASSWORD_HASH
    # SECURITY_REGISTERABLE = True
    # SECURITY_SEND_REGISTER_EMAIL = False
    # SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
    # SECURITY_LOGIN_WITHOUT_CONFIRMATION = False
    # SECURITY_PASSWORD_SALT = '\xc7F\xcce\x03\xc3\x02_\x04\x1e@\x9fC\xf7'

    # JWT

    # FCM
    # PARTY SERVICES

    # Security

    # Flask-DebugToolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Sentry config
    JSON_AS_ASCII = False

    # Host string, used by fabric

    # Audit
    #AUDIT_PATH = "path/to/audit"
    #AUDIT_MAX_FILE_SIZE = 4*1024*1024  # 4 GB
    #AUDIT_MAX_FILE_COUNT = 1000        # allow split to maximum 1000 files
