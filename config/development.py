# encoding: utf-8
from .default import Config

class DevelopmentConfig(Config):
    # App config
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///../db/dictionary.sqlite3"
