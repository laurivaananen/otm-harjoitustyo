from application.request.request_parser import JsonParser
import pytest

@pytest.fixture
def json_data():
    return JsonParser({'text':'Hello World!'})


def test_find_text(json_data):
    assert "Hello World!" == json_data.find_from_json("text")

def test_return_none_if_not_found(json_data):
    assert None == json_data.find_from_json("message")