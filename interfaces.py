from itertools import *
from typing import *
from functools import *
from messages import *

# Génériques d'espace de mobilité

@singledispatch
def move_matrix(self):
    """Donne la matrice de déplacement de l'espace de mobilité"""

# Génériques d'agents

@singledispatch
def position(self):
    """Donne la position d'un objet"""
    
@singledispatch
def set_position(self, position):
    """Déplace un objet"""
    
@singledispatch
def energy(self):
    """Donne l'énergie d'un objet"""
    
@singledispatch
def set_energy(self, energy: float):
    """Met à jour l'énergie d'un objet"""
    
@singledispatch
def neighbors(self) -> List:
    """Donne les voisins d'un objet"""

@singledispatch
def execute(self, csp_program, constants):
    """Exécute un programme csp"""    

@singledispatch
def send(self, receiver, message):
    """Envoie un message"""
    
@singledispatch
def get_memory(self):
    """Donne la mémoire d'un agent sous forme de dictionnaire
    qui est constituée de la position et de l'énergie des autres agents"""
    
@singledispatch
def set_memory(self, agent, position, energy: float):
    """Met à jour la mémoire d'un agent"""
    
@singledispatch
def set_manet_agent_numbers(self, number):
    """Met à jour le nombre d'agents dans le MANET"""

@singledispatch
def set_local_leader(self, leader):
    """Met à jour le leader local"""
    
@singledispatch
def set_global_leader(self, leader):
    """Met à jour le leader global"""
    
@singledispatch
def set_route(self, route):
    """Met à jour la route, route étant une liste d'agents voisin à qui transmettre le message"""
    

    
# génériques d'images
@singledispatch
def receive_and_deal_message(agent, message):
    """Reçoit et traite les messages"""
    pass