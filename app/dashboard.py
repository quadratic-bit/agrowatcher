from pathlib import Path

from flask import Blueprint, render_template, redirect, Response
from flask_login import current_user

import os.path
from app.utils.retriever import colour_ndvi
from ast import literal_eval

from app.models.fields import Field

bp_dashboard = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@bp_dashboard.route("/")
def home() -> str | Response:
    if not current_user.is_authenticated:
        return redirect("/auth/login")
    return render_template("dashboard/select.html", user=current_user,
                           fields=get_user_fields(current_user.id))


@bp_dashboard.route("/view/<int:index>")
def view(index: int) -> str | Response:
    if not current_user.is_authenticated:
        return redirect("/auth/login")
    field = Field.query.filter_by(id=index).first()
    if not field:
        return render_template("dashboard/field_not_found.html")
    filename = f"static/field_data/field{field.id}.jpg"
    if not os.path.isfile(Path(__file__).parent.joinpath(filename)):
        polygon: list[list[float]] = literal_eval(field.polygon)
        print(polygon)
        colour_ndvi(output_=filename, polygon=polygon)
    return render_template("dashboard/field.html", filename=f"field_data/field{field.id}.jpg",
                           fields=get_user_fields(current_user.id))


def get_user_fields(user_id: int) -> list[Field]:
    return Field.query.filter_by(user_id=user_id).all()
