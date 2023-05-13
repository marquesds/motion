import logging

from flask import Flask

logger = logging.getLogger(__name__)


def create_app() -> Flask:
    app = Flask(__name__)

    from motion.infra.http.server import server

    app.register_blueprint(server)

    return app
