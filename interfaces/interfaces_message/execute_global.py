from itertools import *
from typing import *
from functools import *

# EXECUTE GLOBAL
@singledispatch
def program(self):
    """Donne le programme d'un message"""

@singledispatch
def set_program(self, program):
    """Met à jour le programme d'un message"""

@singledispatch
def constants(self):
    """Donne les constantes d'un message"""

@singledispatch
def set_constants(self, constants):
    """Met à jour les constantes d'un message"""
    
# RESULT GLOBAL
@singledispatch
def data(self):
    """Donne les données d'un message"""

@singledispatch
def set_data(self, data):
    """Met à jour les données d'un message"""