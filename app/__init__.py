import os

from flask import Flask, render_template
from flask_login import current_user

from app.auth import bp_auth
from app.dashboard import bp_dashboard
from app.misc import bp_misc
from app.api import bp_api
from app.models.database import db, lm
from app.models.users import User


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.urandom(12).hex(),
        SQLALCHEMY_DATABASE_URI="sqlite:///data/main.sqlite3",
        SQLALCHEMY_TRACK_MODIFICATIONS=True)

    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_misc)
    app.register_blueprint(bp_dashboard)
    app.register_blueprint(bp_api)

    db.init_app(app)
    lm.init_app(app)

    @app.route("/")
    def home() -> str:
        return render_template("index.html", is_auth=current_user.is_authenticated)

    return app
