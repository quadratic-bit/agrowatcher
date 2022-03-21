from flask import Blueprint, request, Response
from ast import literal_eval

bp_api = Blueprint("api", __name__, url_prefix="/api")


@bp_api.route("/pin_field", methods=["POST"])
def pin() -> Response:
    coords: list = literal_eval(request.form["field_coordinates"])
    area = float(request.form["field_area"])
    print(coords)
    print(area)
    if coords[0] != coords[-1] or area > 10_000_000:
        return Response(
            "Invalid arguments",
            status=400)
    return Response(
        "ok",
        status=200)
