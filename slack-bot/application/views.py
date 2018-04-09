from application import app
from flask import request, jsonify
from application.request_parser import SlashCommandRequest, EventRequest
from application.response_parser import SlashCommandResponse

import json
import os

@app.route("/", methods=["GET", "POST"])
def index():

    request_data = EventRequest(request)

    request_data.print_request()

    response_data = SlashCommandResponse()
    response_data.add_text("Message received")

    # print(request_json)

    # print("\n\n\n\n")
    # for key in request_json:
    #     print("Key: {}, value: {}".format(key, request_json[key]))

    # print("\n\n\n")
    # print(os.environ["CLIENT_ID"])
    # print(os.environ["CLIENT_SECRET"])
    # print("\n\n\n\n")

        

    return response_data.return_json()

@app.route("/printer", methods=["GET", "POST"])
def printer():

    request_data = SlashCommandRequest(request)
    
    response_data = SlashCommandResponse()

    response_data.add_text(request_data.text)



    return response_data.return_json()