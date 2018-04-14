from application.request.request_parser import JsonParser, RequestParser
import pytest
import json

class FakeRequest(object):

    def __init__(self, headers= {"Content-Type":"application/json"}, body={"text":"HelloWorld!"}):
        self.headers = headers
        self.body = body

@pytest.fixture
def json_data():
    return JsonParser({'text':'Hello World!'})

@pytest.fixture
def request_data():
    fake_request = FakeRequest()
    request_parser = RequestParser(fake_request)
    request_parser.body = {"text":"HelloWorld!"}

    return request_parser

def test_find_headers(request_data):
    assert {"Content-Type":"application/json"} == request_data.headers

def test_correct_body_json(request_data):
    print("\n\n\n")
    print(request_data.body)
    assert {"text":"HelloWorld!"} == request_data.body

def test_parse_json_body(request_data):
    assert "HelloWorld!" == request_data.find_from_json("text")

def test_find_text(json_data):
    assert "Hello World!" == json_data.find_from_json("text")

def test_return_none_if_not_found(json_data):
    assert None == json_data.find_from_json("message")