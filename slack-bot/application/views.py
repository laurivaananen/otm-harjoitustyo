from application import app
from flask import request, jsonify
import requests

from application import bot

from application.request.request_parser import RequestParser
from application.response.response_parser import JsonMessage

from application import database

import json
import os
import re


@app.route("/", methods=["GET", "POST"])
def index_page():
    """
    Maps the route for messages coming from Slack
    """

    request_parser = RequestParser(request)
    request_parser.parse_content()

    if request_parser.find_from_json("type") == "url_verification":
        return jsonify({"challenge":
                        request_parser.find_from_json("challenge")})

    message_event = request_parser.find_from_json("event")

    # Making sure a bot didn't send a message
    if "bot_id" not in message_event.keys() or message_event["bot_id"] is None:

        if ("subtype" in message_event.keys() and
                message_event["subtype"] == "file_share"):

            bot.download_confirmation(message_event)

        if ("subtype" not in message_event.keys()
                and message_event["type"] == "message"):

            bot.match_trigger(message_event["text"], message_event["channel"])

    return ""


# If a user clicks on a button, this gets triggered
@app.route("/component", methods=["GET", "POST"])
def component():
    """
    Maps the route for component actions coming from Slack
    """

    request_parser = RequestParser(request)
    request_parser.parse_content()

    payload_json = json.loads(request_parser.body["payload"][0])

    bot.download_confirmation_update(payload_json)

    return ""
