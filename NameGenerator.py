#! /usr/bin/python
from random import choice, seed as rseed

class NameGenerator(object):

    nouns = []
    adjectives = []

    def get_name(self):
	    if seed:
		rseed(seed)

	    if tokenhex:
		tokenchars = '0123456789abcdef'

	    adjective = choice(ADJECTIVES)
	    noun = choice(NOUNS)
	    token = ''.join(choice(tokenchars) for _ in range(tokenlength))

	    sections = [adjective, noun, token]
	    return delimiter.join(filter(None, sections))
        return "%s-%s" % ('dv', 'dv')


    def __init__(self):
        print("hello there")
        nouns = [ "grass", "world" ]
        adjectives = [ "green", "innocent" ]


ng = NameGenerator()
print(ng.get_name())
