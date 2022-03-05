from flask import Blueprint, render_template

bp_auth = Blueprint("auth", __name__, url_prefix="/auth")


@bp_auth.route("/login")
def login() -> str:
    return render_template("auth/login.html")


@bp_auth.route("/signup")
def signup() -> str:
    return render_template("auth/signup.html")
