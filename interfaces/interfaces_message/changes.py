from itertools import *
from typing import *
from functools import *

@singledispatch
def position(self, agent):
    """Donne la position d'un objet"""

@singledispatch
def set_position(self, agent,  position):
    """Déplace un objet"""
    
@singledispatch
def energy(self, agent):
    """Donne l'énergie d'un objet"""
    
@singledispatch
def set_energy(self, alban,  energy: float):
    """Met à jour l'énergie d'un objet"""