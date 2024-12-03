from itertools import *
from typing import *
from functools import *
from utils import *
from interfaces import *

def start_non_informed_communication(agent):
    """Communication non informée"""
    generic({ agent: [neighbors, send] })
    pass

def start_informed_communication(agent):
    """Communication informée"""
    generic({ agent: [neighbors, get_memory, send, execute] })
    pass

