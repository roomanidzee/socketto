"""
Main file for system constructing
"""

__version__ = "0.0.1"
from socketto.services import *
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, join_room, emit, rooms

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
CORS(app)
ws = SocketIO(app, cors_allowed_origins="*")


@app.route("/document/<input_id>")
def get_document(input_id):
    return jsonify(get_document(input_id))


@ws.on("create")
def on_create(content):

    document_id = create_document(content)
    join_room(document_id)

    emit("document", get_document(document_id), room=document_id, json=True)


@ws.on("edit")
def on_edit(ident, content):

    my_rooms = rooms()
    my_rooms.remove(request.sid)

    edit_document(ident, content)

    emit("edit", get_document(ident), room=my_rooms[-1], json=True)
