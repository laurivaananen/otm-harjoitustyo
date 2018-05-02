import requests


class JsonMessage(object):
    """
    A message that can be sent to Slack

    :param dict headers: Headers of the http request
    :param dict body: The data of the https request
    :param list attachments: Attachments of the body
    """

    def __init__(self, headers={}, body={}, attachments=None):
        self.headers = headers
        self.body = body
        self.attachments = attachments
        self.r = None

    def send_message(self, url):
        """
        Sends this message to a given url

        :param str url: The url to send this message
        :return: Status code of the http request
        :rtype: str
        """
        if self.attachments:
            self.body["attachments"] = self.attachments

        self.r = requests.post(url, json=self.body, headers=self.headers)
        if self.r.status_code == 200:
            return self.r
        else:
            return None

    def get_status(self):
        """
        Returns a nicely formatted status text

        :return: Status code
        :rtype: str
        """
        return "Status code: {}, Status text: {}".format(self.r.status_code,
                                                         self.r.text)
