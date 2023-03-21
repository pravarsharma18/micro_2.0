from conf.database import db


class Category(db.Model):

    __tablename__ = "product_category"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Coumn(db.String(150))


class Product(db.Model):

    __tablename__ = "product"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    category = db.Coumn(db.ForeignKey(Category.id))
