from flask import Blueprint, render_template

server = Blueprint("server", __name__, url_prefix="/", template_folder="templates")


@server.route("/")
@server.route("/posts/")
def posts():
    return render_template("posts.html")


@server.route("/search/")
def search():
    return render_template("search.html")
