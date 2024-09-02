from flask import Blueprint, render_template, request
from .models import PostModel, db

posts = Blueprint("posts", __name__, url_prefix="/posts", template_folder="templates")


@posts.route("/new", methods=["GET"])
def new_post():
    all_posts = PostModel.query.all()
    return render_template("create_post.html", all_posts=all_posts)


@posts.route("/create", methods=["POST"])
def create_post():
    title = request.form.get("title")
    author = request.form.get("author")
    contain = request.form.get("contain")

    post = PostModel(title=title, author=author, contain=contain)

    db.session.add(post)
    db.session.commit()

    return "201"


@posts.route("/", methods=["GET"])
def get_all_posts():
    all_posts = PostModel.query.all()
    return str(all_posts)


@posts.route("/<int:id>", methods=["GET"])
def get_detail_post(id: int):
    return f"Post Id: {id}"


@posts.route("/<int:id>", methods=["PUT, UPDATE"])
def update_post(id: int):
    return f"Post {id} updated"


@posts.route("/<int:id>", methods=["DELETE"])
def delete_post(id: int):
    return f"Post {id} deleted"
