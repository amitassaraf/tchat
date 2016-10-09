from remodel.helpers import create_tables, create_indexes
from remodel.models import Model

__author__ = 'amitassaraf'


class Lead(Model):
    has_one = ('User',)

class User(Model):
    belongs_to = ('Lead',)

class Team(Model):
    pass


create_tables()
create_indexes()
