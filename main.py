#!/usr/bin/env python

import tornado.ioloop
import tornado.web
from tornroutes import route
from jinja2 import Environment, FileSystemLoader

from NameGenerator import NameGenerator


templates = Environment(loader=FileSystemLoader('templates'))


@route(r"/")
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(templates.get_template('index.html').render())


@route(r"/shorten_url") 
class ShortenUrlHandler(tornado.web.RequestHandler):
    def post(self):
        return self.write("OK")


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

