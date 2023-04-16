''' This module defines the Paths class '''

from os.path import dirname, join

class Paths:
    ''' Paths class '''

    OUTPUT_DIRPATH = join(dirname(__file__), 'output')
