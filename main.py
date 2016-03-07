#!/usr/bin/env python

import tornado.ioloop
import tornado.web
from tornroutes import route

from NameGenerator import *


@route(r"/")
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("INDEX")


@route(r"/([\w+\-]+)") 
class FollowLink(tornado.web.RequestHandler):
    def get(self, words):
        self.write("FOLLOW: " + words)


if __name__ == "__main__":
    app = tornado.web.Application(route.get_routes())
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

