from flask import Blueprint

posts = Blueprint("posts", __name__, url_prefix="/posts")


@posts.route("/create", methods=["POST"])
def create_post():
    return "Post create, code 201"


@posts.route("/", methods=["GET"])
def get_all_posts():
    return "all posts"


@posts.route("/<int:id>", methods=["GET"])
def get_detail_post(id: int):
    return f"Post Id: {id}"


@posts.route("/<int:id>", methods=["PUT, UPDATE"])
def update_post(id: int):
    return f"Post {id} updated"


@posts.route("/<int:id>", methods=["DELETE"])
def delete_post(id: int):
    return f"Post {id} deleted"
