from itertools import *
from typing import *
from functools import *
from messages import *

# génériques de message
@singledispatch
def receive_and_deal_message(agent, message):
    """Reçoit et traite les messages"""
    pass

@singledispatch
def sender(self):
    """Donne l'envoyeur d'un message"""
    
# @singledispatch
# def value(self):
#     """Donne la valeur d'un message"""

# @singledispatch
# def set_value(self, value):
#     """Met à jour la valeur d'un message"""
