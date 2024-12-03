from itertools import *
from typing import *
from functools import *

# génériques de message
@singledispatch
def receive_and_deal_message(agent, message):
    """Reçoit et traite les messages"""
    pass

@singledispatch
def sender(self):
    """Donne l'envoyeur d'un message"""
    
