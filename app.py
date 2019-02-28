from flask import Flask, render_template
from flask_socketio import SocketIO
import logging
from logging.config import dictConfig


dictConfig({
    "version": 1,
    "formatters": {"default": {
        "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
    }},
    "handlers": {"wsgi": {
        "class": 'logging.StreamHandler',
        "stream": "ext://flask.logging.wsgi_errors_stream",
        "formatter": "default"
    }},
    "root": {
        "level": "WARNING",
        "handlers": ["wsgi"]
    }
})


app = Flask(__name__)
socketIo = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@socketIo.on("user-connect")
def connectionHandler(message):
    logging.warning("[EVENT] User connected")


@socketIo.on("user-chat")
def messageHandler(message, methods=["GET", "POST"]):
	logging.warning("[EVENT] User message " + str(message))
	socketIo.emit("response", message)


if __name__ == "__main__":
    socketIo.run(app, debug=True)

    