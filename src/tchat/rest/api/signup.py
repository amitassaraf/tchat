from tchat.db.models import Team, User, Lead
from tchat.rest.api import api_views
from tchat.rest.utils import tchat_route

__author__ = 'amitassaraf'


############## Lead ##############

@tchat_route(api_views, '/signup.addLead')
def add_lead(data):
    new_lead = Lead(**data)
    new_lead.save()
    return True, {'lead_id': new_lead.id, 'email': data['email'], 'show_whitelist': False,
                  'require_email_confirmation': False}  # TODO: False here means we dont need to implement signup.confirmCode


############## User signup ##############

@tchat_route(api_views, '/signup.checkEmail')
def check_email(data):
    leads = Lead.filter(email=data['email'])
    if len(leads) > 0:
        return False, {'error': 'taken'}

    return True, {'email': data['email'], 'type': 'unknown', 'auth_url': ''}


@tchat_route(api_views, '/signup.checkUsername')
def check_username(data):
    users = User.filter(username=data['username'])
    if len(users) > 0:
        return False, {'error': 'taken'}

    return True, {}


@tchat_route(api_views, '/signup.checkPasswordComplexity')
def check_password_complexity(data):
    lead = Lead.get(id=data.pop('lead_id'))
    new_user = User(lead=lead, **data)
    new_user.save()
    return True, {}


############## Team signup ##############

@tchat_route(api_views, '/signup.checkUrl')
def check_url(data):
    teams = Team.filter(url=data['url'])
    if len(teams) > 0:
        return False, {'error': 'taken'}

    return True, {}


@tchat_route(api_views, '/signup.suggestUrl')
def suggest_url(data):
    return True, {'email': data['email'], 'available': [data['url'].lower().replace(' ', '-')],
                  'unavailable': []}


@tchat_route(api_views, '/signup.createTeam')
def create_team(data):
    user = User.get(username=data['username'])
    results = Team.filter(url=data['url'])
    if len(results) > 0:
        return False, {}

    new_team = Team(**data)
    new_team.save()
    return True, {
        'url': '/confirmed/{0}'.format(new_team.id),  # TODO
        'api_token': 'RANDOM-NON-SLACK-TOKEN',  # TODO
        "user_id": user.id,
        "team_id": new_team.id,
        'show_invite_step': True,
        'valid_signup_domain': False,
    }
