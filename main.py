#!/usr/bin/env python

import tornado.ioloop
import tornado.web
from tornroutes import route
from jinja2 import Environment, FileSystemLoader

import json

from NameGenerator import *


templates = Environment(loader=FileSystemLoader('templates'))
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r = redis.StrictRedis(host='95.85.22.116', port=6379, db=0)
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
        self.write("FOLLOW: " + words)


if __name__ == "__main__":
    routes = route.get_routes()
    routes.append((r"/static/(.*)", tornado.web.StaticFileHandler, 
                {"path": "static"}))

    app = tornado.web.Application(route.get_routes())
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

