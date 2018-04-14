from application import app
from flask import request, jsonify
from application.request_parser import SlashCommandRequest, EventRequest, SlackRequest
from application.response_parser import SlashCommandResponse, WebAPIMessage, Attachment, Action
import requests

from application.request.request_parser import RequestParser

import json
import os



@app.route("/", methods=["GET", "POST"])
def index():

    request_parser = RequestParser(request)
    request_parser.parse_content()

    if request_parser.find_from_json("type") == "url_verification":
        return jsonify({"challenge":request_parser.find_from_json("challenge")})


    # print("\n\nPrinting event items\n\n")
    # for key, value in event.items():
    #     print("{}: {}".format(key, value))

    # print("\n\nPrinting file items\n\n")
    # for key, value in event["file"].items():
    #     print("{}: {}".format(key, value))

    # print("\n\n")

    # request_data = EventRequest(request)

    # request_data.print_request()

    # Verificating slack bot integration

    # if request_data.request["type"] == "url_verification":
    #     return jsonify({"challenge":request_data.request["challenge"]})


    # If the request is a message and not from a bot, send a message

    print("\n\n\n\n\n\n\n\n\n\n\n")

    print(request_parser.body)

    if request_parser.find_from_json("event"):
        print("RECIEVED A MESSAGE: {}".format(request_parser.body))









    # event = request_data.request["event"]

    # if event["type"] == "message" and not "bot_id" in event:
    #     request_text = event["text"]

    #     request_user = "<@{}>".format(event["user"])

    #     request_channel = event["channel"]

    #     message = WebAPIMessage()

    #     message_data = "User {} sent a message: {}".format(request_user, request_text)

    #     message.add_to_message("text", message_data)

    #     # message.send_message()

    #     send_message(token=os.environ["BOT_OAUTH"],
    #                  channel=request_channel,
    #                  message=message_data)

    #     return ""









    # event = request_data.request["event"]



    # if event and event["subtype"] == "file_share" and event["bot_id"] == None:
    #     print("Found file_share event")

    # print("\n\nStarting to download file\n\n")

    # file_download = event["file"]["url_private_download"]
    # file_name = event["file"]["name"]

    # r = requests.get(file_download)

    # print(r.status_code)

    # dirpath = os.getcwd()

    # print("\n\n{}\n\n".format(dirpath))

    # with open('{}/downloads/{}'.format(dirpath, file_name), 'wb') as f:  
    #     f.write(r.content)

        

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

    print("\nUnknown message type or a message from bot\n")
    return ""

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


def send_message(token, channel, message):

    url = "https://slack.com/api/chat.postMessage"

    headers = {"Content-type":"application/json; charset=utf-8",
               "Authorization":"Bearer {}".format(token)
               }

    data = {"channel":channel,
            "text":message
            }

    r = requests.post(url, headers=headers, json=data)

    print(">>> {}, {}".format(r.status_code, r.text))