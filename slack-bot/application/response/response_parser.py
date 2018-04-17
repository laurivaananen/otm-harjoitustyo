import requests


class JsonMessage(object):

    def __init__(self, headers={}, body={}, attachments=None):
        self.headers = headers
        self.body = body
        self.attachments = attachments
        self.r = None

    def send_message(self, url):
        if self.attachments:
            self.body["attachments"] = self.attachments

        self.r = requests.post(url, json=self.body, headers=self.headers)
        if self.r.status_code == 200:
            return self.r
        else:
            return None

    def get_status(self):
        return "Status code: {}, Status text: {}".format(self.r.status_code, self.r.text)
