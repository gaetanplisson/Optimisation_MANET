from itertools import *
from typing import *
from functools import *
from messages import *

# Génériques d'espace

@singledispatch
def positions(self):
    """Donne les positions possibles"""
    
@singledispatch
def graph_matgrix(self):
    """Donne le graphe des positions possibles"""

# Génériques d'agents

@singledispatch
def position(self):
    """Donne la position d'un objet"""
    
@singledispatch
def set_position(self, position):
    """Déplace un objet"""
    
@singledispatch
def position_graph(self):
    """Donne la position d'un objet sous forme de graphe"""
    
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
def get_memory(self):
    """Donne la mémoire d'un agent sous forme de dictionnaire
    qui est constituée de la position et de l'énergie des autres agents"""
    
@singledispatch
def add_memory(self, agent):
    """Ajoute un agent à la mémoire"""
    
@singledispatch
def del_memory(self, agent):
    """Supprime un agent de la mémoire"""

    
@singledispatch
def memory_size(self):
    """Donne la taille de la mémoire d'un agent"""
    

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
def set_global_leader(self, leader):
    """Met à jour le leader global"""
    
@singledispatch
def global_leader_votes(self):
    """Donne les votes pour le leader global"""

@singledispatch
def add_to_global_leader_votes(self, agent, proposed_leader):
    """Ajoute un vote pour le leader global. Renvoit un dictionnaire avec 
    comme clef l'agent et comme valeur le leader proposé"""
    
@singledispatch
def global_leader(self):
    """Donne le leader global"""

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
def set_local_leader(self, leader):
    """Met à jour le leader global"""
    
@singledispatch
def set_route(self, route):
    """Met à jour la route, route étant une liste d'agents voisin à qui transmettre le message"""
    
@singledispatch
def get_route(self):
    """Donne la route, soit une liste d'agents voisin à qui transmettre le message"""
    
@singledispatch
def route_predecessor(self):
    """Le prédécésseur dans l'arbre de communication"""
    
@singledispatch
def set_route_predecessor(self):
    """Définir le prédécésseur dans l'arbre de communication"""
    

    
