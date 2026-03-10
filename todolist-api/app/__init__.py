from flask import Flask
from config import Config
from .extensions import db, migrate, api


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)
    else:
        app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    from .routes import blp
    api.register_blueprint(blp)

    return app