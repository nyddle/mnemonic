#!/usr/bin/env python

import os

import tornado.ioloop
import tornado.web
from tornroutes import route
from jinja2 import Environment, FileSystemLoader

import json

from NameGenerator import *


templates = Environment(loader=FileSystemLoader('templates'))
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
r = redis.from_url(redis_url)
ng = NameGenerator()

@route(r"/")
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(templates.get_template('index.html').render())


@route(r"/shorten_url") 
class ShortenUrlHandler(tornado.web.RequestHandler):
    def post(self):
	"""
        ip = self.request.remote_ip)
        tries = r.get(ip)
	"""

        name = self.get_argument('url', default=None, strip=True)
        shortened = make_unique_name(name, ng, r)

        if shortened is not None:
            return self.write(json.dumps({ "original" : name, "shortened" : shortened }))
        else:
            return self.write(json.dumps({ "error" : "smth went wrong" }))


@route(r"/([\w+\-]+)") 
class FollowLinkHandler(tornado.web.RequestHandler):
    def get(self, words):

        resolved = None
        normalized = check_custom_name(words)
        if (normalized is not None):
            resolved = r.get(normalized)
            print(resolved)
            if (resolved is not None):
                self.redirect(resolved)

        raise tornado.web.HTTPError(404)


if __name__ == "__main__":
    routes = route.get_routes()
    routes.append((r"/static/(.*)", tornado.web.StaticFileHandler, 
                {"path": "static"}))
    port = int(os.environ.get("PORT", 8888))
    app = tornado.web.Application(route.get_routes())
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

