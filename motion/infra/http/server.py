from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/posts/")
def posts():
    return render_template("posts.html")


@app.route("/search/")
def search():
    return render_template("search.html")
