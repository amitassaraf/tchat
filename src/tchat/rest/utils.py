from functools import wraps

from flask.json import jsonify

from flask import request

__author__ = 'amitassaraf'


def tchat_route(blueprint, url):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            success, json = f(request.json, *args, **kwargs)
            json['ok'] = success
            return jsonify(json)

        return blueprint.route(url, methods=['POST'])(decorated_function)
    return decorator
