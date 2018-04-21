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
    JWT_SECRET_KEY = "EL\xb0\x85\xea\x9f\xa0n\xf1\x95\x08\xb6 t"
    JWT_EXPIRED_IN_MIN = int(os.environ.get('JWT_EXPIRED_IN_MIN', 15))
    JWT_REFRESH_EXPIRED_IN_DAY = int(os.environ.get('JWT_REFRESH_EXPIRED_IN_DAY', 7))
    JWT_ALGOR = "HS256"

    # FCM
    FCM_APIKEY = os.environ.get("FCM_APIKEY", "AAAA7TP3TJM:APA91bHomfAYOUsxlJHd5yARtHsugQPAkh_mv5TOrf2ZsApyfIaKGJn2P5BQSTt2zn-3y8899CXJvzRaJr2GyRjXz3Uh8A7SsLsByayyRR-Qtme2aIRi2O6R-uIOEgNKwv4IYdMCTlPv")
    NOTI_BASE_URL = os.environ.get("NOTI_BASE_URL", "http://kebhom-dev.scbabacus-dev.com/kebhom/notification/redirect.html?")

    FCM_APIKEY = "AAAAVq9Fsj4:APA91bGC9arANWCFWYVX1DdjGNPPArIs7jv4SFKmIJ98l7GSVa7Fnp2iKOEcAEMd-3EAnrvl2MzvN3BdfNlR--U8GUfjWB1LLZ51fFQxMPDtdm9PFQG7Ubl_yCUR6pwyoxnacZ9uBEvm"
    # PARTY SERVICES
    #MASHUP_ENDPOINT = "https://host:port"
    #ML_ENDPOINT = "https://host:port"
    #MASHUP_ENDPOINT = "http://54.179.144.183:8080"
    MASHUP_ENDPOINT = "https://kebhom-dev.scbabacus.com"
    MASHUP_REQUEST_CERT_TUBPLE = (os.path.join(PROJECT_PATH, 'certificates/kebhom-as-dev.cert'),
                                  os.path.join(PROJECT_PATH, 'certificates/kebhom-as-dev.key')
                                 )
    ML_ENDPOINT = "http://13.229.118.217:34546"

    # Security
    AWS_KEYID = os.environ.get("AWS_KEYID", "AKIAIZWUM2EBE5NMGMSQ")
    AWS_SECRET_KEYID = os.environ.get("AWS_SECRET_KEYID", "e8bgSxZ88IIt4M5kSsLBvM8j37LDhFnNiuejF8gO")
    AWS_REGION = os.environ.get("AWS_REGION", 'ap-southeast-1')

    AWS_BUCKETNAME = os.environ.get("AWS_BUCKETNAME", "kebhom-dev-secretkey")
    AWS_SRC_FILENAME = os.environ.get("AWS_SRC_FILENAME", "dev/kebhom-dev.scbabacus-dev.com_private_encrypted.asc")

    ML_API_KEY = os.environ.get("ML_API_KEY", '123456')

    BYPASS_OTP = '' # set otp for bypasss

    # Flask-DebugToolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Sentry config
    SENTRY_DSN = os.environ.get('SENTRY_DSN', 'https://7cda48481ab14a45a5c8726eb1697caa:5de3c1d0c9084facb99389275814fc50@sentry.io/292488')
    JSON_AS_ASCII = False

    # Host string, used by fabric
    HOST_STRING_master = "ec2-user@54.179.144.183"
    HOST_STRING_sit = "ec2-user@54.169.67.38"

    # Audit
    #AUDIT_PATH = "path/to/audit"
    #AUDIT_MAX_FILE_SIZE = 4*1024*1024  # 4 GB
    #AUDIT_MAX_FILE_COUNT = 1000        # allow split to maximum 1000 files
