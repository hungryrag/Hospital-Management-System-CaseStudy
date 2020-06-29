import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret_string"
    # Database Configuration
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "hospital.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
