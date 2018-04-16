from application import app
from flask import request, jsonify
from application.request_parser import SlashCommandRequest, EventRequest, SlackRequest
from application.response_parser import SlashCommandResponse, WebAPIMessage, Attachment, Action
import requests

from application.request.request_parser import RequestParser
from application.response.response_parser import JsonMessage

import json
import os



@app.route("/", methods=["GET", "POST"])
def index():

    request_parser = RequestParser(request)
    request_parser.parse_content()

    print("\n\n\n\n\n\n\n\n\n\n\n")

    print(json.dumps(request_parser.body, indent=4))

    print("\n\n\n\n\n\n\n\n\n\n\n")

    

    if request_parser.find_from_json("type") == "url_verification":
        return jsonify({"challenge":request_parser.find_from_json("challenge")})

    


    message_event = request_parser.find_from_json("event")

    if message_event["subtype"] and message_event["subtype"] == "file_share":

        message_file = message_event["file"]
        message_file_url = message_file["url_private"]
        message_file_timestamp = message_file["timestamp"]
        message_file_filetype = message_file["filetype"]

        authorization_header = {"Authorization": "Bearer {}".format(os.environ["SLACK_OAUTH"])}

        message = JsonMessage(headers=authorization_header)
        response = message.send_message(url=message_file_url)

        if response:
            dirpath = os.getcwd()

            with open('{}/downloads/{}'.format(dirpath, "{}.{}".format(message_file_timestamp, message_file_filetype)), 'wb') as f:  
                f.write(response.content)
        










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