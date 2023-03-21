from conf.database import db
from sqlalchemy import inspect


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(150))
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    is_superuser = db.Column(db.Boolean())
    is_active = db.Column(db.Boolean())

    def to_dict(self):
        """ return all attributes as json object """
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}
