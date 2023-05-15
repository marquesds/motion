from flask import Blueprint, jsonify, render_template, request

from motion.infra.db.mongodb.repositories import (
    Connection,
    MongoBusLineRepository,
    MongoPostRepository,
    MongoSubscriptionRepository,
)
from motion.subscriptions.entities import Passenger

server = Blueprint("server", __name__, url_prefix="/", template_folder="templates")


data = {
    "name": "Foo Lano",
    "email": "foo.lano@gmail.com",
    "id": 6,
    "profile_image": "https://i.pravatar.cc/40",
}

passenger = Passenger(**data)


@server.route("/")
@server.route("/posts/")
def posts():
    repository = MongoPostRepository(connection=Connection())

    return render_template("posts.html", passenger=passenger, posts=repository.list(passenger))


@server.route("/search/", methods=["GET", "POST"])
def search():
    repository = MongoBusLineRepository(connection=Connection())
    if request.method == "POST":
        line = request.form.get("line")
        lines = repository.list(passenger=passenger, line=line)
        return render_template("search.html", lines=lines)

    lines = repository.list(passenger=passenger)
    return render_template("search.html", lines=lines)


@server.route("/follow/", methods=["POST"])
def follow():
    repository = MongoSubscriptionRepository(connection=Connection())
    repository.follow(passenger=passenger, bus=request.form["bus_line"])
    return jsonify({"status": "ok"}), 200


@server.route("/unfollow/", methods=["POST"])
def unfollow():
    repository = MongoSubscriptionRepository(connection=Connection())
    repository.unfollow(passenger=passenger, bus=request.form["bus_line"])
    return jsonify({"status": "ok"}), 200
