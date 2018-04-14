import json



class JsonParser(object):

    def __init__(self, json_obj):
        self.json_obj = json_obj

    def find_from_json(self, key):
        value = None

        try:
            value = self.json_obj[key]
        except:
            pass

        return value

class RequestParser(object):

    def __init__(self, request_obj):
        self.request_obj = request_obj
        self.headers = self.request_obj.headers
        self.body = None

    def parse_content(self):
        try:
            if self.headers["Content-Type"] == "application/json":
                self.body = self.request_obj.get_json()

            elif self.headers["Content-Type"] == "application/x-www-form-urlencoded":
                self.body = self.request_obj.form

            else:
                self.body = None

        except:
            pass

    def find_from_json(self, key):
        value = None

        try:
            value = self.body[key]
        except:
            pass

        return value

