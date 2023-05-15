import logging

from flask import Flask
from flask_pymongo import PyMongo

from motion.config import Config

logger = logging.getLogger(__name__)


mongo = PyMongo()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)

    from motion.infra.http.server import server

    app.register_blueprint(server)

    from motion.infra.db.mongodb.repositories import Connection

    conn = Connection()
    conn.load_database()

    return app
