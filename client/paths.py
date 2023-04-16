''' This module defines the Paths class '''

from os.path import dirname, join

class Paths:
    ''' Paths class '''

    INPUT_FILEPATH = join(dirname(__file__), 'input', 'posts.json')
