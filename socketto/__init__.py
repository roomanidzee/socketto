"""
Main file for system constructing
"""

__version__ = "0.0.1"

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
CORS(app)
ws = SocketIO(app, cors_allowed_origins="*")

from socketto.routes import *
