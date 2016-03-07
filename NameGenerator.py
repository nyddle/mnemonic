#!/usr/bin/env python
from random import choice, seed as rseed
import re
import redis

class NameGenerator(object):

    nouns = []
    adjectives = []

    def get_name(self):

        adjective = choice(self.adjectives)
        noun = choice(self.nouns)

        return "%s-%s" % (adjective, noun)

    def __init__(self):

        with open('./nouns.txt') as nouns:
            self.nouns = filter(len, map( lambda w: w.lower().strip(), nouns.readlines()))

        with open('./adjectives.txt') as adjectives:
            self.adjectives = filter(len, map( lambda w: w.lower().strip(), adjectives.readlines()))

def make_unique_name(original_link, ng, r):

   name = None 
   while ((name is None) or (not name_is_free(name, r))):
       name = ng.get_name()
   r.set(name, original_link)
   return name

def name_is_free(name, r):

    name = check_custom_name(name)

    if (name is None):
        return None
    else:
        res = r.get(name)
        if (res is None):
            return name
        else:
            return None

def check_custom_name(name):

    if (not is_valid_name(name)):
        return False
    return re.sub("\s+", "-", name)


def is_valid_name(name):

    return re.match("[a-z0-9\s\-]+", name)

if (__name__ == "__main__"):
    ng = NameGenerator()
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    print(ng.get_name())
    print(make_unique_name('http://yandex.ru', ng, r))
    print(is_valid_name("Hello-Kitty"))
    print(is_valid_name("hello-kitty"))
    print(is_valid_name("hello kitty"))
    print (check_custom_name("hello   there"))
"""
coolish-kilometer
"""

