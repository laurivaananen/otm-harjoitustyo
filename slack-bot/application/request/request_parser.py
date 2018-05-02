import json


class JsonParser(object):

    def __init__(self, json_obj):
        self.json_obj = json_obj

    def find_from_json(self, key):
        value = None

        try:
            value = self.json_obj[key]
        except KeyError:
            pass

        return value


class RequestParser(object):
    """
    Represents a message from Slack

    :param json request_obj: Message from Slack
    """

    def __init__(self, request_obj):
        self.request_obj = request_obj
        self.headers = self.request_obj.headers
        self.body = None

    def parse_content(self):
        """
        Tries to parse the contents
        """
        try:
            if self.headers["Content-Type"] == "application/json":
                self.body = self.request_obj.get_json()

            elif self.headers["Content-Type"] == "application/x-www-form-urlencoded":
                self.body = self.request_obj.form.to_dict(flat=False)

            else:
                self.body = None

        except KeyError:
            print("Couldn't read request")

    def find_from_json(self, key):
        """
        Tries to find the value by given key

        :param str key: The key to search by
        :return: The value fo the key
        :rtype: obj
        """
        value = None

        try:
            value = self.body[key]
        except KeyError:
            print("Couldn't read JSON")

        return value
