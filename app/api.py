from flask import Blueprint, request, Response
from flask_login import current_user

from app.models.database import db
from app.models.fields import Field
from ast import literal_eval

bp_api = Blueprint("api", __name__, url_prefix="/api")


@bp_api.route("/pin_field", methods=["POST"])
def pin() -> Response:
    coords: list = literal_eval(request.form["field_coordinates"])[0]
    area = int(float(request.form["field_area"]))
    if not current_user.is_authenticated:
        return Response(
            "User is unauthorised",
            status=401)
    if coords[0] != coords[-1] or area > 10_000_000:
        return Response(
            "Invalid arguments",
            status=400)
    else:
        field = Field(
            polygon=request.form["field_coordinates"][1:-1],
            area=area,
            user_id=current_user.id)
        db.session.add(field)
        db.session.commit()
        return Response(
            {
                "ok": True,
                "index": field.id
            },
            status=200)
