from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .posts.views import posts
from .users.views import users

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./data.db"
    db.init_app(app)

    # Routes in here

    migrate = Migrate(app, db)
    app.register_blueprint(posts)
    app.register_blueprint(users)

    return app
