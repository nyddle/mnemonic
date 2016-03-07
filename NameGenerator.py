#! /usr/bin/python
from random import choice, seed as rseed

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

ng = NameGenerator()
print(ng.get_name())
