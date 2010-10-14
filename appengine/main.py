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

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import wsgiref.handlers
import yaml
import re
from cgi import escape
from urllib import quote
from markdown import markdown
from google.appengine.ext import webapp
from google.appengine.api.urlfetch import fetch
from google.appengine.dist import use_library

use_library('django', '1.1')
from django.utils.encoding import smart_unicode

class GistRedirectHandler(webapp.RequestHandler):
  def get(self, id):
    self.redirect('/%s' % id)

class GistViewHandler(webapp.RequestHandler):
  def get(self, id):
    raw = fetch('http://gist.github.com/api/v1/yaml/%s' % id)
    meta = yaml.load(raw.content)['gists'][0]
    owner = meta[':owner'] or ""
    description = meta[':description'] or ""
    files = meta[':files'] or []
    time = meta[':created_at']
    title = "%s - %s" % (id, escape(description)) if description else id

    self.response.out.write("""
<!DOCTYPE html>
<html>
  <head>
    <title>bl.ocks.org - %s</title>
    <style type="text/css">

@import url("/style.css");

    </style>
  </head>
  <body>
    <div class="body">
      <a href="/" class="about right">What&rsquo;s all this then?</a>
      <h1>block <a href="http://gist.github.com/%s">#%s</a></h1>
      <h2>
        <span class="description">%s</span>
        by <a href="http://github.com/%s" class="owner">%s</a>
      </h2>
      <iframe marginwidth="0" marginheight="0" scrolling="no" src=\"/d/%s/\"></iframe>
      <div class="readme">
""" % (title, id, id, escape(description), quote(owner), escape(owner), id))

    # display the README
    for f in files:
      if re.match("^readme\.(md|mkd|markdown)$", f, re.I):
        html = markdown(smart_unicode(fetch('http://gist.github.com/raw/%s/%s' % (id, quote(f))).content))
      elif re.match("^readme(\.txt)?$", f, re.I):
        html = "<pre>%s</pre>" % escape(fetch('http://gist.github.com/raw/%s/%s' % (id, quote(f))).content)
      else:
        html = None
      if html:
        self.response.out.write(html)

    # display the creation time
    if time:
      self.response.out.write("<p class=\"time\">Created at %s.</p>" % time)

    self.response.out.write("</div>")

    # display the other files as source
    for f in files:
      if not re.match("^readme(\.[a-z]+)?$", f, re.I):
        self.response.out.write('<script src="http://gist.github.com/%s.js?file=%s"></script>' % (id, f))

    self.response.out.write("""
      <a href="/" class="about">about bl.ocks.org</a>
    </div>
  </body>
</html>
""")

class GistDataHandler(webapp.RequestHandler):
  def get(self, id, file):
    if not file:
      file = 'index.html'
    raw = fetch('http://gist.github.com/raw/%s/%s' % (id, quote(file)))
    if re.search("\.css$", file):
      self.response.headers["Content-Type"] = "text/css"
    elif re.search("\.js$", file):
      self.response.headers["Content-Type"] = "text/javascript"
    elif re.search("\.json$", file):
      self.response.headers["Access-Control-Allow-Origin"] = "*"
      self.response.headers["Content-Type"] = "application/json"
    elif re.search("\.txt$", file):
      self.response.headers["Content-Type"] = "text/plain"
    self.response.out.write(raw.content)

def main():
  application = webapp.WSGIApplication([
      ('/([0-9]+)', GistViewHandler),
      ('/([0-9]+)/', GistRedirectHandler),
      ('/d/([0-9]+)/(.*)', GistDataHandler)
      ], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
