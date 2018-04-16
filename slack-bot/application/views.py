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

    # print(json.dumps(request_parser.body, indent=4))

    

    if request_parser.find_from_json("type") == "url_verification":
        return jsonify({"challenge":request_parser.find_from_json("challenge")})

    


    message_event = request_parser.find_from_json("event")


    # Making sure a bot didn't send a message
    if "bot_id" not in message_event.keys() or message_event["bot_id"] == None:


        if "subtype" in message_event.keys() and message_event["subtype"] == "file_share":
            print("\n\nFILE SHARE:\n{}".format(json.dumps(message_event, indent=4)))
            bot.download_confirmation(message_event)
            # bot.download_image(message_event)

        if "subtype" not in message_event.keys() and message_event["type"] == "message":
            print("\n\nMESSAGE EVENT:\n{}".format(json.dumps(message_event, indent=4)))
            bot.download_confirmation(message_event)



    return ""


@app.route("/component", methods=["GET" ,"POST"])
def component():

    request_parser = RequestParser(request)
    request_parser.parse_content()

    payload_json = json.loads(request_parser.body["payload"][0])

    print("\n\nCOMPONEN PAYLOAD:\n{}".format(json.dumps(payload_json, indent=4)))

    bot.download_confirmation_update(payload_json)











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

# @app.route("/printer", methods=["GET", "POST"])
# def printer():

#     request_data = SlashCommandRequest(request)

#     request_data.print_request()
    
#     response_data = SlashCommandResponse()

#     response_data.add_text(request_data.text)



#     return response_data.return_json()


# @app.route("/interactive", methods=["GET", "POST"])
# def interactive():

#     interacive_request = SlackRequest(request)

#     interacive_request.print_request()

#     return ""


# def send_message(token, channel, message):

#     url = "https://slack.com/api/chat.postMessage"

#     headers = {"Content-type":"application/json; charset=utf-8",
#                "Authorization":"Bearer {}".format(token)
#                }

#     data = {"channel":channel,
#             "text":message
#             }

#     r = requests.post(url, headers=headers, json=data)

#     print(">>> {}, {}".format(r.status_code, r.text))