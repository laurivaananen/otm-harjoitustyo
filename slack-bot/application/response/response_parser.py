import requests


class JsonMessage(object):

    def __init__(self, headers, body):
        self.headers = headers
        self.body = body
        self.r = None

    def send_message(self, url):
        self.r = request.post(url, data=self.body, headers=self.headers)

    def get_status(self):
        return "Status code: {}, Status text: {}".format(self.r.status_code, self.r.text)