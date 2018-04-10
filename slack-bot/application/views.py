from application import app
from flask import request, jsonify
from application.request_parser import SlashCommandRequest, EventRequest, SlackRequest
from application.response_parser import SlashCommandResponse, WebAPIMessage, Attachment, Action
import requests

import json
import os

@app.route("/", methods=["GET", "POST"])
def index():

    # request_data = EventRequest(request)

    # request_data.print_request()

    # if request_data.challenge != None:
    #     return jsonify({"challenge":request_data.challenge})

    request_data = SlackRequest(request)

    event = request_data.request["event"]

    print("\n\nPrinting event items\n\n")
    for key, value in event.items():
        print("{}: {}".format(key, value))

    print("\n\nPrinting file items\n\n")
    for key, value in event["file"].items():
        print("{}: {}".format(key, value))

    if event and event["subtype"] == "file_share" and event["bot_id"] == None:
        print("Found file_share event")

    print("\n\nStarting to download file\n\n")

    file_download = event["file"]["url_private_download"]
    file_name = event["file"]["name"]

    r = requests.get(file_download)

    print(r.status_code)

    dirpath = os.getcwd()

    print("\n\n{}\n\n".format(dirpath))

    with open('{}/downloads/{}'.format(dirpath, file_name), 'wb') as f:  
        f.write(r.content)

        

    # message = WebAPIMessage()
    # message.add_to_message("text", "Someone uploaded a file")

    # attachment = Attachment()

    # attachment.add_to_attachment("text", "Do you want to download this file?")
    # attachment.add_to_attachment("fallback", "You are unable to download this file")
    # attachment.add_to_attachment("callback_id", "download_file")

    # action = Action("download", "Download", "button", "download")


    # attachment.add_to_attachment("actions", [action.action])

    # message.add_to_message("attachments", [attachment.attachment])

    


    # message.send_message()

    return jsonify({"text":"Message received"})

@app.route("/printer", methods=["GET", "POST"])
def printer():

    request_data = SlashCommandRequest(request)

    request_data.print_request()
    
    response_data = SlashCommandResponse()

    response_data.add_text(request_data.text)



    return response_data.return_json()


@app.route("/interactive", methods=["GET", "POST"])
def interactive():

    interacive_request = SlackRequest(request)

    interacive_request.print_request()

    return ""