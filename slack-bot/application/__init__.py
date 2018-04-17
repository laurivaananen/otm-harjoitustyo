from flask import Flask

import os
if "BOT_OAUTH" not in os.environ.keys():
    print("\n\nPLEASE SET BOT_OAUTH ENVIRONMENT VARIABLE CORRECTLY\n\n")

if "SLACK_OAUTH" not in os.environ.keys():
    print("\n\nPLEASE SET SLACK_OAUTH ENVIRONMENT VARIABLE CORRECTLY\n\n")

app = Flask(__name__)


from application import views