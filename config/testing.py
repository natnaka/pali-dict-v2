# encoding: utf-8
from .default import Config

class TestingConfig(Config):
    # App config
    TESTING = True

    # Disable csrf while testing
    WTF_CSRF_ENABLED = False

    # Db config, for in-memory db
    SQLALCHEMY_DATABASE_URI = "sqlite://"

    USE_STUB = True
