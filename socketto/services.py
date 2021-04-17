import uuid
import time

all_docs = {}


def create_document(input_content):
    """

    Method for creating the input document

    Arguments:
        input_content: text for a new document

    Returns:
        identificator of new document

    """

    ident = str(uuid.uuid4())

    all_docs[ident] = {
        "id": ident,
        "content": input_content,
        "update_time": int(time.time()),
    }

    return ident


def edit_document(ident, content):
    """

    Method for document editing

    Arguments:
        ident: identificator of document to edit
        content: new content for a document

    Returns:
        identificator of edited document

    """

    doc = all_docs[ident]

    doc["content"] = content
    doc["update_time"] = int(time.time())

    all_docs[ident] = doc

    return ident


def get_document(ident):
    """

    Method for retrieving document information

    Arguments:
        ident: identificator of a document

    Returns:
        document information

    """

    return all_docs[ident]
