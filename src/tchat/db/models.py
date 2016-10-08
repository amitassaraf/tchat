import jsonpickle
from rethinkdb.errors import ReqlOpFailedError

from connector import tchat_db

__author__ = 'amitassaraf'


class TChatModel(object):
    def serialize(self):
        """
        Serialize the model to json
        """
        return jsonpickle.encode(self)


class Team(TChatModel):
    __table__ = 'teams'

    def __init__(self, url=None, email=None, team_name=None, username=None, lead_id=None, email_misc=False, tz=None,
                 real_name=None, password=None, code=None):
        self.url = url
        self.email = email
        self.team_name = team_name
        self.username = username
        self.lead_id = lead_id
        self.email_misc = email_misc
        self.tz = tz
        self.real_name = real_name
        self.password = password
        self.code = code


tables = [cls for cls in vars()['TChatModel'].__subclasses__()]
tables = map(lambda tb: tb.__table__, tables)

# Create Tables
for table in tables:
    # Try creating table create
    try:
        tchat_db.table_create(table).run()
    except ReqlOpFailedError as exc:
        pass
