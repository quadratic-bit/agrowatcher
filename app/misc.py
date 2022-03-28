from flask import Blueprint, render_template
from flask_login import current_user

bp_misc = Blueprint("misc", __name__)


@bp_misc.route("/article")
def article() -> str:
    return render_template("misc/article.html", is_auth=current_user.is_authenticated)


@bp_misc.route("/terms")
def terms() -> str:
    return render_template("misc/terms.html", is_auth=current_user.is_authenticated)


@bp_misc.route("/privacy")
def privacy() -> str:
    return render_template("misc/privacy.html", is_auth=current_user.is_authenticated)
