from interfaces import *
from utils import *
from messages import *



@receive_and_deal_message.register
def _(agent, message: Message.BROADCAST_LEADER):
    """Reçoit et traite les messages BROADCAST_ORDER"""
    generic({ agent: [] }) # A compléter en fonction du comportement attendu pour agent
    pass

@receive_and_deal_message.register
def _(agent, message: Message.BROADCAST_STATUS):
    """Reçoit et traite les messages BROADCAST_STATUS"""
    generic({ agent: [] }) # A compléter en fonction du comportement attendu pour agent
    pass

@receive_and_deal_message.register
def _(agent, message: Message.CHANGE):
    """Reçoit et traite les messages EXECUTE"""
    generic({ agent: [execute] }) # A compléter en fonction du comportement attendu pour agent
    pass

@receive_and_deal_message.register
def _(agent, message: Message.EXECUTE_GLOBAL):
    """Reçoit et traite les messages UPDATE_MEMORY"""
    generic({ agent: [set_memory] }) # A compléter en fonction du comportement attendu pour agent
    pass

@receive_and_deal_message.register
def _(agent, message: Message.EXECUTE_LOCAL):
    """Reçoit et traite les messages EXECUTE_LOCAL"""
    generic({ agent: [execute] })

@receive_and_deal_message.register
def _(agent, message: Message.ROUTE):
    """Reçoit et traite les messages ROUTE"""
    generic({ agent: [set_route] })
    
@receive_and_deal_message.register
def _(agent, message: Message.BROADCAST_LEADER):
    """Reçoit et traite les messages BROADCAST_LEADER"""
    generic({ agent: [set_global_leader] })
    
@receive_and_deal_message.register
def _(agent, message: Message.BROADCAST_STATUS):
    """Reçoit et traite les messages BROADCAST_STATUS"""
    generic({ agent: [] })
    



def start_non_informed_communication(agent):
    """Communication non informée"""
    generic({ agent: [neighbors, send] })
    pass

def start_informed_communication(agent):
    """Communication informée"""
    generic({ agent: [neighbors, get_memory, send, execute] })
    pass


    

    