from itertools import *
from typing import *
from functools import *

# EXECUTE_LOCAL
@singledispatch
def order(agent):
    """renvoit soit compute_leader() soit compute_route()""" 

@singledispatch
def set_order(agent, order):
    """Met à jour l'ordre de l'agent""" 
    
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
    
# RESULT_LOCAL
@singledispatch
def data(self):
    """Donne le résultat d'un message"""
    
@singledispatch
def set_data(self, result):
    """Met à jour le résultat d'un message"""

# on réutilise set_order
    
