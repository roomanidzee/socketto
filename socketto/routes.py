from socketto.services import *
from flask import request, jsonify
from flask_socketio import join_room, emit, rooms
from socketto import app, ws


@app.route("/document/<input_id>")
def get_document(input_id):
    return jsonify(get_document(input_id))


@ws.on("create")
def on_create(content):
    document_id = create_document(content)

    emit("document", get_document(document_id), broadcast=True, json=True)


@ws.on("edit")
def on_edit(ident, content):
    edit_document(ident, content)

    emit("edit", get_document(ident), broadcast=True, include_self=False, json=True)
