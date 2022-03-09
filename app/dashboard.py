from flask import Blueprint, render_template

bp_dashboard = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@bp_dashboard.route("/")
def home() -> str:
    return render_template("dashboard/base.html")
