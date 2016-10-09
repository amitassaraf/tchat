from flask.ext.compress import Compress
from tchat.rest.api import api_views
from settings import DEBUG

__author__ = 'amitassaraf'

from flask import Flask

app = Flask(__name__)

Compress(app)

app.debug = DEBUG
app.config.from_object('tchat.settings')

app.register_blueprint(api_views)
