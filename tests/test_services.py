from socketto.services import *


def test_create():
    new_doc_id = create_document("test_doc")

    new_doc = get_document(new_doc_id)

    assert new_doc["id"] == new_doc_id
    assert new_doc["content"] == "test_doc"


def test_edit():

    edit_doc_id = create_document("edit_doc")

    new_content = "new_content"

    edit_document(edit_doc_id, new_content)

    editted_doc = get_document(edit_doc_id)

    assert editted_doc["id"] == edit_doc_id
    assert editted_doc["content"] == "new_content"


def test_document_retrieve():

    simple_doc_id = create_document("simple_doc")

    simple_doc = get_document(simple_doc_id)

    assert simple_doc["id"] == simple_doc_id
    assert simple_doc["content"] == "simple_doc"
