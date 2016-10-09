from tchat.db.connector import tchat_db
from tchat.db.models import Team, User, Lead
from tchat.rest.api import api_views
from tchat.rest.utils import tchat_route

__author__ = 'amitassaraf'


############## Lead ##############

@tchat_route(api_views, 'signup.addLead')
def add_lead(data):
    new_lead = Lead(**data)
    new_lead.save()
    return True, {'lead_id': new_lead.id, 'email': data['email'], 'show_whitelist': False,
                  'require_email_confirmation': False}  # TODO: False here means we dont need to implement signup.confirmCode


############## User signup ##############

@tchat_route(api_views, 'signup.checkEmail')
def check_email(data):
    results = tchat_db.table(Lead.table).filter({'email': data['email']}).run()
    if len(results) > 0:
        return False, {'error': 'taken'}

    return True, {'email': data['email'], 'type': 'unknown', 'auth_url': ''}


@tchat_route(api_views, 'signup.checkUsername')
def check_username(data):
    results = tchat_db.table(User.table).filter({'username': data['username']}).run()
    if len(results) > 0:
        return False, {'error': 'taken'}

    return True, {}


@tchat_route(api_views, 'signup.checkPasswordComplexity')
def check_password_complexity(data):
    lead = tchat_db.table(Lead.table).get(data.pop('lead_id')).run()
    new_user = User(lead=Lead(**lead), **data)
    new_user.save()
    return True, {}


############## Team signup ##############

@tchat_route(api_views, 'signup.checkUrl')
def check_url(data):
    results = tchat_db.table(Team.table).filter({'url': data['url']}).run()
    if len(results) > 0:
        return False, {'error': 'taken'}

    return True, {}


@tchat_route(api_views, 'signup.suggestUrl')
def suggest_url(data):
    return True, {'email': data['email'], 'available': [data['url'].lower().replace(' ', '-')],
                  'unavailable': []}


@tchat_route(api_views, '/signup.createTeam')
def create_team(data):
    user = tchat_db.table(User.table).filter({'username': data['username']}).run()[0]
    results = tchat_db.table(Team.table).filter({'url': data['url']}).run()
    if len(results) > 0:
        return False, {}

    new_team = Team(**data)
    new_team.save()
    return True, {
        'url': '/confirmed/{0}'.format(new_team.id),  # TODO
        'api_token': 'xoxs-87934118566-87950840930-87939742837-5ea2b31377',  # TODO
        "user_id": user.id,  # TODO
        "team_id": new_team.id,  # TODO
        'show_invite_step': True,
        'valid_signup_domain': False,
    }
