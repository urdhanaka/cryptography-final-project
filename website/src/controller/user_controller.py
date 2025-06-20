from http import HTTPStatus
from flask import Blueprint, Response, json, request

from src.dto.user_dto import UserLoginDTO


user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/", methods=["POST"])
def handle_user_login() -> Response:
    data = request.json
    user_login_dto = UserLoginDTO(data)

    if not user_login_dto.is_valid():
        return Response(
            response=json.dumps({"status": "request is not valid"}),
            status=HTTPStatus.BAD_REQUEST,
            mimetype="application/json",
        )

    return Response(status=200)
