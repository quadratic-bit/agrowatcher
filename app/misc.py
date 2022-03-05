from flask import Blueprint, render_template

bp_misc = Blueprint("misc", __name__)


@bp_misc.route("/article")
def article() -> str:
    return render_template("misc/article.html")


@bp_misc.route("/terms")
def terms() -> str:
    return render_template("misc/terms.html")


@bp_misc.route("/privacy")
def privacy() -> str:
    return render_template("misc/privacy.html")
