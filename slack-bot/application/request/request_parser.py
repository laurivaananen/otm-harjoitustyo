



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
