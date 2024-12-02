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
def neighbors(self):
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
def set_memory(self, agent, value):
    """Met à jour la mémoire d'un agent"""
    
@singledispatch
def memory_size(self):
    """Donne la taille de la mémoire d'un agent"""
    
@singledispatch
def del_memory(self, agent):
    """Supprime un agent de la mémoire"""

@singledispatch
def broadcast_agents_memory_buffer(self):
    """Buffer qui permet l'oubli de certains agents"""

@singledispatch
def add_to_broadcast_agents_memory_buffer(self, agent):
    """Ajoute un agent au buffer de mémoire"""

@singledispatch
def empty_broadcast_agents_memory_buffer(self):
    """Vide le buffer de mémoire"""

@singledispatch
def set_manet_agent_numbers(self, number):
    """Met à jour le nombre d'agents dans le MANET"""
    
@singledispatch
def get_manet_agent_numbers(self):
    """Donne le nombre d'agents dans le MANET"""

@singledispatch
def set_local_leader(self, leader):
    """Met à jour le leader local"""
    
@singledispatch
def local_leader_votes(self):
    """Donne les votes pour le leader local"""

@singledispatch
def add_to_local_leader_votes(self, agent, proposed_leader):
    """Ajoute un vote pour le leader local. Renvoit un dictionnaire avec 
    comme clef l'agent et comme valeur le leader proposé"""
    
@singledispatch
def local_leader(self):
    """Donne le leader local"""

@singledispatch
def excluded_agents_from_leader_list(self, leader):
    """Donne la liste des agents exclus de la liste des leaders"""  
    
@singledispatch
def add_to_excluded_agents_from_leader_list(self, agent):
    """Ajoute un agent à la liste des exclusions de la liste des leaders"""  

@singledispatch
def add_to_local_dependants(self, agent):
    """Ajoute un agent à la liste des dépendants locaux"""
    
@singledispatch
def set_global_leader(self, leader):
    """Met à jour le leader global"""
    
@singledispatch
def set_route(self, route):
    """Met à jour la route, route étant une liste d'agents voisin à qui transmettre le message"""
    
@singledispatch
def get_route(self):
    """Donne la route, soit une liste d'agents voisin à qui transmettre le message"""
    

    
# génériques de message
@singledispatch
def receive_and_deal_message(agent, message):
    """Reçoit et traite les messages"""
    pass

@singledispatch
def value(self):
    """Donne la valeur d'un message"""

@singledispatch
def set_value(self, value):
    """Met à jour la valeur d'un message"""
    
@singledispatch
def sender(self):
    """Donne l'envoyeur d'un message"""