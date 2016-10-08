from flask.json import jsonify
from tchat.rest.api import api_blueprint
from tchat.rest.utils import tchat_route

__author__ = 'amitassaraf'


@tchat_route(api_blueprint, '/api.test?error=<error>')
def api_test(data, error):
    return jsonify({
        'ok': True,
        'args': {
            'error': ''
        }
    })
