from itertools import *
from typing import *
from functools import *

@singledispatch
def proposed_leader(self):
    """Donne le leader proposé par un message"""

@singledispatch
def set_proposed_leader(self, leader):
    """Met à jour le leader proposé par un message"""