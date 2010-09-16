#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import wsgiref.handlers
import yaml
from urllib import quote
from google.appengine.ext import webapp
from google.appengine.api.urlfetch import fetch

class MainHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write('Hello world!')

class GistRedirectHandler(webapp.RequestHandler):
  def get(self, id):
    self.redirect('/%s/' % id)

class GistViewHandler(webapp.RequestHandler):
  def get(self, id):
    raw = fetch('http://gist.github.com/api/v1/yaml/%s' % id)
    meta = yaml.load(raw.content)
    self.response.out.write("""
<!DOCTYPE html>
<html>
  <head>
    <title>bl.ocks.org - %s</title>
    <style type="text/css">

@import url("/static/style.css");

    </style>
  </head>
  <body>
    <div class="body">
      <a href="/static/about.html" class="about right">What&rsquo;s all this then?</a>
      <h1>block <a href="http://gist.github.com/%s">#%s</a></h1>
""" % (id, id, id))
    self.response.out.write('<iframe src=\"/d/%s/\"></iframe>' % id)
    for f in meta['gists'][0][':files']:
      self.response.out.write('<script src="http://gist.github.com/%s.js?file=%s"></script>' % (id, f))
    self.response.out.write("""
      <a href="/static/about.html" class="about">about bl.ocks.org</a>
    </div>
  </body>
</html>
""")

class GistDataHandler(webapp.RequestHandler):
  def get(self, id, file):
    if not file:
      file = 'index.html'
    raw = fetch('http://gist.github.com/raw/%s/%s' % (id, quote(file)))
    self.response.out.write(raw.content)

def main():
  application = webapp.WSGIApplication([
      ('/', MainHandler),
      ('/([0-9]+)', GistRedirectHandler),
      ('/([0-9]+)/', GistViewHandler),
      ('/d/([0-9]+)/(.*)', GistDataHandler)
      ], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
