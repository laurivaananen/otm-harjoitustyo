from flask import jsonify
import requests
import json

class SlashCommandResponse(object):

    def __init__(self):
        self.response = {}

    def add_text(self, text):
        self.response["text"] = text

    def return_json(self):
        return jsonify(self.response)


class WebAPIMessage(object):


    def __init__(self):
        self.url = "https://hooks.slack.com/services/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"
        self.message = {}
        self.headers = {}
        self.add_to_headers("Content-type","application/json; charset=utf-8")

    def add_to_message(self, key, value):
        self.message[key] = value

    def add_to_headers(self, key, value):
        self.headers[key] = value

    def send_message(self):
        r = requests.post(self.url, data=json.dumps(self.message), headers=self.headers)
        print(r.status_code)
        print(r.text)


class Attachment(object):

    def __init__(self):
        self.attachment = {}
        self.actions = []

    def add_to_attachment(self, key, value):
        self.attachment[key] = value


class Action(object):

    def __init__(self, name, text, _type, value):
        self.action = {}

        self.action["name"] = name
        self.action["text"] = text
        self.action["type"] = _type
        self.action["value"] = value

