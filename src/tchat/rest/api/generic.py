from flask.globals import request
from tchat.rest.api import api_views
from tchat.rest.utils import tchat_route

__author__ = 'amitassaraf'


@tchat_route(api_views, '/api.test')
def api_test(data):
    error = request.args.get('error')
    return True, {
        'args': {
            'error': error
        }
    }


@tchat_route(api_views, '/')
def index(data):
    return True, {}
