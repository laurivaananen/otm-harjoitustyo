class SlashCommandRequest(object):

    def __init__(self, request):
        self.request = request
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

    def find_from_form(self, key):
        value = None

        try:
            value = self.request.form.get(key)
        except:
            pass

        return value

import json

class EventRequest(object):

    def __init__(self, request):
        self.request = request.get_json()

    def print_request(self):
        for key, value in self.request.items():
            print("{}, {}".format(key, value))