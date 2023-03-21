from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
bcrypt = Bcrypt()
ma = Marshmallow()


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:trootech1234@localhost/flask_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET_KEY = "0lldqz1iPvbPe4K6gId5nXschFYwKdrruWt_8Q9Mn0g"
    RABBIT_HOST = 'localhost'
    RABBIT_PORT = 5672
    RABBIT_EXCHANGE = 'flask_exchange'
