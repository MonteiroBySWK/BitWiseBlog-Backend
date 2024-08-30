from flask import Blueprint

users = Blueprint("users", __name__, url_prefix="/user")


@users.route("/create", methods=["POST"])
def create_user():
    return ""


@users.route("/", methods=["GET"])
def get_all_users():
    return ""


@users.route("/<int:id>", methods=["GET"])
def get_detail_user(id: int):
    return ""


@users.route("/<int:id>", methods=["PUT", "UPDATE"])
def update_user(id: int):
    return ""


@users.route("/<int:id>", methods=["DELETE"])
def delete_user(id: int):
    return ""
