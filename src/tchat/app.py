from tchat.rest.api import api_blueprint

__author__ = 'amitassaraf'

from flask import Flask

app = Flask(__name__)
app.config.from_object('tchat.settings')

app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(port=80)