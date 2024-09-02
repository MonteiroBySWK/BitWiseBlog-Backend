from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./data.db"

    db.init_app(app)

    from .posts.views import posts
    from .users.views import users

    app.register_blueprint(posts)
    app.register_blueprint(users)

    migrate = Migrate(app, db)

    return app
