import os
import urllib
import json

from google.appengine.api import users

import jinja2
import webapp2

import model


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
      os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class FrontPage(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    logout_url = users.create_logout_url('/')
    login_url = users.create_login_url('/')
    template = JINJA_ENVIRONMENT.get_template('index.html')
    self.response.write(template.render(
      {'user': user,
       'logout_url': logout_url,
       'login_url': login_url
      }))

  def post(self):
    user = users.get_current_user()
    if not user:
      self.abort(403)

    ep = self.request.get('endpoint', None)

    if not ep:
      self.abort(400)


app = webapp2.WSGIApplication([
  ('/', FrontPage),
  ], debug=True)