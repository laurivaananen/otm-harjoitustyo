from flask import jsonify

class SlashCommandResponse(object):

    def __init__(self):
        self.response = {}

    def add_text(self, text):
        self.response["text"] = text

    def return_json(self):
        return jsonify(self.response)