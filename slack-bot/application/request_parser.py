

import json




class SlackRequest(object):

    def __init__(self,request):
        self.request = request
        try:
            content_type = request.headers['Content-Type']
        except:
            print("\nNo Content_type found\n")

        if content_type == "application/json":
            self.request = request.get_json()
        elif content_type == "application/x-www-form-urlencoded":
            self.request = request.form
        else:
            self.request = None

    def find_from_form(self, key):
        value = None

        try:
            value = self.request[key]
        except:
            pass

        return value

    def print_request(self):
        for key, value in self.request.items():
            print("\n{}, {}".format(key, value))

class FileShared(SlackRequest):

    def __init__(self, event):
        self.request = event
        self.type = self.find_from_form("type")
        self.file_id = self.find_from_form("file_id")
        self.user_id = self.find_from_form("user_id")
        self.file = self.find_from_form("file")
        self.event_ts = self.find_from_form("event_ts")

class SlashCommandRequest(SlackRequest):

    def __init__(self, request):
        self.token = self.find_from_form("token")
        self.team_id = self.find_from_form("team_id")
        self.team_domain = self.find_from_form("team_domain")
        self.channel_id = self.find_from_form("channel_id")
        self.channel_name = self.find_from_form("channel_name")
        self.user_id = self.find_from_form("user_id")
        self.user_name = self.find_from_form("user_name")
        self.command = self.find_from_form("command")
        self.text = self.find_from_form("text")
        self.response_url = self.find_from_form("response_url")
        self.trigger_id = self.find_from_form("trigger_id")

class EventRequest(SlackRequest):

    def __init__(self, request):

        self.request = request.get_json()

        self.token = self.find_from_form("token")
        self.team_id = self.find_from_form("team_id")
        self.api_app_id = self.find_from_form("api_app_id")
        self.event = self.find_from_form("event")
        self.type = self.find_from_form("type")
        self.event_id = self.find_from_form("event_id")
        self.event_time = self.find_from_form("event_time")
        self.authed_users = self.find_from_form("authed_users")

        if self.event["type"] == "file_shared":
            self.event = FileShared(self.event)
    


