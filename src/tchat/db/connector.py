from rethinkdb.errors import ReqlOpFailedError
from tchat.settings import DB_PORT

__author__ = 'amitassaraf'

import rethinkdb

rethinkdb.connect('localhost', DB_PORT).repl()

# Try creating the database
try:
    rethinkdb.db_create('tchatdb').run()
except ReqlOpFailedError as exc:
    pass


tchat_db = rethinkdb.db('tchatdb')
