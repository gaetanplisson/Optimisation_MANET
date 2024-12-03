from itertools import *
from typing import *
from functools import *

@singledispatch
def route(self):
    """Donne la route d'un message"""
    
@singledispatch
def set_route(self, route):
    """Met à jour la route d'un message"""