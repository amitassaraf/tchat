from tchat.db.connector import tchat_db
from tchat.db.models import Team
from tchat.rest.api import api_views
from tchat.rest.utils import tchat_route

__author__ = 'amitassaraf'


@tchat_route(api_views, '/signup.createTeam?_x_id=<x_id>')
def create_team(data, x_id):
    results = tchat_db.table(Team.__table__).filter({'url': data['url']}).run()
    if len(results) > 0:
        return False, {}

    new_team = Team(**data)

    tchat_db.table(Team.__table__).insert(new_team.serialize()).run()
    return True, {
        'url': '/confirmed/{0}'.format('random'),  # TODO
        'api_token': '{0}'.format('random'),  # TODO
        'show_invite_step': True,
        'valid_signup_domain': False,
    }
