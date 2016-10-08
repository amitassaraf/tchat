from functools import partial

from flask import request

__author__ = 'amitassaraf'


def tchat_route(blueprint, url):
    def wrapper(func):
        func = blueprint.route(url, methods=['POST'])(func)

        def wrp(func, *args, **kwargs):
            return func(request.json, *args, **kwargs)

        return partial(wrp, func)

    return wrapper
