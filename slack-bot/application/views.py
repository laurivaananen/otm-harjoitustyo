from application import app
from flask import request, jsonify
from application.request_parser import SlashCommandRequest, EventRequest, SlackRequest
from application.response_parser import SlashCommandResponse, WebAPIMessage

import json
import os

@app.route("/", methods=["GET", "POST"])
def index():

    request_data = EventRequest(request)

    request_data.print_request()

    print(request_data.event.file_id)

    message = WebAPIMessage()
    message.add_to_message("text", "Hi I received your message")

    print("\n\n\nHeaders: {}\n\n\n".format(message.headers))
    print("\n\n\nBody: {}\n\n\n".format(message.message))

    message.send_message()

    response_data = SlashCommandResponse()

    response_data.add_text("Message received")

        

    return jsonify({"text":"Helloworld"})

@app.route("/printer", methods=["GET", "POST"])
def printer():

    request_data = SlashCommandRequest(request)

    request_data.print_request()
    
    response_data = SlashCommandResponse()

    response_data.add_text(request_data.text)



    return response_data.return_json()