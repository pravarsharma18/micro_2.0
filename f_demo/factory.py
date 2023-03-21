from flask import Flask
from flask_migrate import Migrate

from conf.database import db, bcrypt, ma, Config


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    Migrate(app, db)
    ma.init_app(app)

    from api.rest import users
    app.register_blueprint(users.USER_BLUEPRINT)
    with app.app_context():
        db.create_all()
    return app
