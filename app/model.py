import datetime
from google.appengine.ext import ndb


DEFAULT_MSG_KEY=ndb.Key("msg", "public")


class User(ndb.Model):
  email = ndb.StringProperty(required=True)
  endpoints = ndb.StringProperty(repeated=True)
  timestamp = ndb.DateTimeProperty(auto_now_add=True)
