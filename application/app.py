from flask import Flask
# Blueprints import
from application.blueprints.users import user
from application.blueprints.posts import mypost
from application.extensions import db,login_manager,migrate

#Models import
from application.blueprints.users.models import User
from application.blueprints.posts.models import Post
from application.blueprints.follows.models import Follow


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(user)
    app.register_blueprint(mypost)
    #app.register_blueprint(follow)
    extensions(app)
    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app,db)
    

    return None