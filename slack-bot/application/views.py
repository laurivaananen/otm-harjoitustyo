from application import app
from flask import request, jsonify

import json
import os

@app.route("/", methods=["GET", "POST"])
def index():

    # request_json = request.get_json()

    # print(request_json)

    # print("\n\n\n\n")
    # for key in request_json:
    #     print("Key: {}, value: {}".format(key, request_json[key]))

    print("\n\n\n")
    print(os.environ["CLIENT_ID"])
    print(os.environ["CLIENT_SECRET"])
    print("\n\n\n\n")

    # response_json = json.dumps({"challenge":request_json["challenge"]})

        

    return "Hello world"

@app.route("/printer", methods=["GET", "POST"])
def printer():

    print("\n\n\n")
    print(request)
    print("\n\n\n\n")
    print(request.form.get("text"))
    print("\n\n\n\n")
    for key, value in request.form.items():
        print("{}, {}".format(key, value))


    response_json = json.dumps({"text":"You said: {}".format(request.form.get("text"))})
    




    return jsonify({"text": "HeyWOrld", "attachments": [{"text":"Hello", "color":"good"}]})