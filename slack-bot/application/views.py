from application import app
from flask import request, jsonify
import requests

from application import bot

from application.request.request_parser import RequestParser
from application.response.response_parser import JsonMessage

import json
import os


@app.route("/", methods=["GET", "POST"])
def index():

    request_parser = RequestParser(request)
    request_parser.parse_content()

    if request_parser.find_from_json("type") == "url_verification":
        return jsonify({"challenge": request_parser.find_from_json("challenge")})

    message_event = request_parser.find_from_json("event")

    # Making sure a bot didn't send a message
    if "bot_id" not in message_event.keys() or message_event["bot_id"] is None:

        if "subtype" in message_event.keys() and message_event["subtype"] == "file_share":
            bot.download_confirmation(message_event)

        if "subtype" not in message_event.keys() and message_event["type"] == "message":
            pass

    return ""


# If a user clicks on a button, this gets triggered
@app.route("/component", methods=["GET", "POST"])
def component():

    request_parser = RequestParser(request)
    request_parser.parse_content()

    payload_json = json.loads(request_parser.body["payload"][0])

    bot.download_confirmation_update(payload_json)

    return ""
