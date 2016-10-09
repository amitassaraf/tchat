from tchat.rest.api import api_views
from tchat.rest.utils import tchat_route

__author__ = 'amitassaraf'


# TODO: Dummy
@tchat_route(api_views, '/experiments.getByLead')
def dummy(data):
    return True, {}
