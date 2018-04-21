# encoding: utf-8
import os
from .default import Config


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "{connector}://{user}:{password}@{h    ost}:{port}/{dbname}".format(
                connector=os.environ.get('PALI_DICT_DB_CONNECTOR', 'mysql+mysqlconnector'),
                user=os.environ.get('PALI_DICT_DB_USER', 'palidb'),
                password=os.environ.get('PALI_DICT_DB_PASSWORD', 'password'),
                host=os.environ.get('PALI_DICT_DB_HOST', 'localhost'),
                port=os.environ.get('PALI_DICT_DB_PORT', '3306'),
                dbname=os.environ.get('PALI_DICT_DB_NAME', 'dictionary'),
                  )
