from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.auth import bp_auth
from app.misc import bp_misc
from app.dashboard import bp_dashboard
import os


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.urandom(12).hex(),
        SQLALCHEMY_DATABASE_URI="sqlite:///data/main.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=True)
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_misc)
    app.register_blueprint(bp_dashboard)

    db = SQLAlchemy(app)

    @app.route("/")
    @app.route("/index")
    def home() -> str:
        return render_template("index.html")

    return app
