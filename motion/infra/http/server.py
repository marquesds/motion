from flask import Blueprint, render_template, request

from motion.infra.db.mongodb.repositories import (
    Connection,
    MongoBusLineRepository,
    MongoPostRepository,
)
from motion.subscriptions.entities import Passenger

server = Blueprint("server", __name__, url_prefix="/", template_folder="templates")


@server.route("/")
@server.route("/posts/")
def posts():
    data = {
        "name": "Foo Lano",
        "email": "foo.lano@gmail.com",
        "id": 6,
        "profile_image": "https://i.pravatar.cc/40",
    }
    passenger = Passenger(**data)

    repository = MongoPostRepository(connection=Connection())

    return render_template("posts.html", passenger=passenger, posts=repository.list(passenger))


@server.route("/search/", methods=["GET", "POST"])
def search():
    data = {
        "name": "Foo Lano",
        "email": "foo.lano@gmail.com",
        "id": 6,
        "profile_image": "https://i.pravatar.cc/40",
    }
    passenger = Passenger(**data)

    repository = MongoBusLineRepository(connection=Connection())
    if request.method == "POST":
        line = request.form["line"]
        lines = repository.list(passenger=passenger, line=line)
        return render_template("search.html", lines=lines)

    lines = repository.list(passenger=passenger)
    return render_template("search.html", lines=lines)
