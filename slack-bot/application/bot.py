from application.request.request_parser import RequestParser
from application.response.response_parser import JsonMessage
import json
import os
import requests
from datetime import datetime
from application import database
import re


def download_image(url):
    """
    Downloads an image and saves it

    :param str url: url to the image
    """

    datetime_now = datetime.now().strftime("%Y%m%d-%H%M%S")

    file_type = url.split(".")[-1]

    authorization_header = {"Authorization": "Bearer {}"
                            .format(os.environ["SLACK_OAUTH"])}

    message = JsonMessage(headers=authorization_header)

    # File we got
    response = message.send_message(url=url)

    if response:
        dirpath = os.getcwd()

        file_path = '{}/downloads/{}'.format(dirpath, "{}.{}".
                                             format(datetime_now, file_type))

        if not os.path.exists('{}/downloads/'.format(dirpath)):
            os.makedirs('{}/downloads/'.format(dirpath))

        with open(file_path, 'wb') as f:
            f.write(response.content)

def match_trigger(text, channel):
    """
    If matches regular expression trigger, will respond with a message

    :param str text: The message to match against
    :param str channel: The channel to send the message
    """
    print("Received: {}".format(text))
    for command_pair in database.fetch_all_command_pairs().items():
        if re.match(command_pair[0], text):
            print("Triggered: {}".format(command_pair[0]))
            print("Sending: {}".format(command_pair[1]))
            send_message(body=command_pair[1],
                            channel=channel)


def send_message(body, channel):
    """Sends a message

    :param str body: The message to be sent
    :param str channel: The channel to send the message
    """
    url = "https://slack.com/api/chat.postMessage"

    bot_token = database.fetch_token("bot")

    headers = {"Authorization": "Bearer {}".format(bot_token)}
    headers["Content-Type"] = "application/json; charset=utf-8"

    body = {"text": body, "channel": channel}

    message = JsonMessage(headers=headers, body=body)
    response = message.send_message(url=url)
    if response.json()["ok"]:
        print("Message sent")
    else:
        print("Error sending message")


def download_confirmation(message_event):
    """
    Sends a download confirmation message

    :param json message_event: Message event got from slack
    """
    message_user = message_event["user"]
    message_channel = message_event["channel"]
    message_file_url = message_event["file"]["url_private"]

    headers = {"Authorization": "Bearer {}".format(os.environ["BOT_OAUTH"])}
    headers["Content-Type"] = "application/json; charset=utf-8"

    text = "<@{}> shared a file".format(message_user)

    file_name = message_event["file"]["name"]

    body = {"text": text, "channel": message_channel}

    attachments = [{
                    "text": file_name,
                    "fallback": "You are unable to download it",
                    "callback_id": "download_confirmation",
                    "color": "#3AA3E3",
                    "attachment_type": "default",
                    "actions": [
                        {
                            "name": "download_confirmation",
                            "text": "Download",
                            "type": "button",
                            "value": message_file_url
                        }]
                    }]

    url = "https://slack.com/api/chat.postMessage"

    message = JsonMessage(headers=headers, body=body, attachments=attachments)
    response = message.send_message(url=url)


def download_confirmation_update(message_payload):
    """
    Updates download confirmation message

    :param json message_payload: Message payload got from Slack
    """

    orig_message = message_payload["original_message"]
    orig_message_text = orig_message["text"]
    msg_url = orig_message["attachments"][0]["actions"][0]["value"]
    message_channel = message_payload["channel"]["id"]
    message_ts = message_payload["original_message"]["ts"]

    download_image(msg_url)

    body = {"text": orig_message_text,
            "channel": message_channel,
            "ts": message_ts}

    attachments = [{
                    "text": "Thanks for downloading",
                    "fallback": "You are unable to download it",
                    "color": "#3AA3E3",
                    }]

    headers = {"Authorization": "Bearer {}".format(os.environ["BOT_OAUTH"])}

    headers["Content-Type"] = "application/json; charset=utf-8"

    url = "https://slack.com/api/chat.update"

    message = JsonMessage(headers=headers, body=body, attachments=attachments)
    response = message.send_message(url=url)
