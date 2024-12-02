from interfaces import *
from utils import *
from messages import *
from csp_leader import compute_leader
from csp_compute_route import compute_route


@receive_and_deal_message.register
def _(agent, message: Message.BROADCAST_STATUS):
    """Reçoit et traite les messages BROADCAST_STATUS et commence les dépendances locales"""
    generic({ agent: [neighbors, send, add_memory, memory_size,get_memory, del_memory,  get_manet_agent_numbers, \
        add_to_broadcast_agents_memory_buffer, empty_broadcast_agents_memory_buffer, broadcast_agents_memory_buffer, \
            set_manet_agent_numbers], \
        message: [value, sender] }) # A compléter en fonction du comportement attendu pour agent
    neighbors = agent.neighbors()
    sender = message.sender()
    add_memory(agent, sender)
    set_manet_agent_numbers(agent, len(get_memory(agent).keys()))
    add_to_broadcast_agents_memory_buffer(agent, sender)
    if len(broadcast_agents_memory_buffer(agent)) >= memory_size(agent)*2/3: # 2/3 des agents en mémoire
        for other_agent in get_memory(agent).keys():
            if other_agent not in broadcast_agents_memory_buffer(agent):
                del_memory(agent, other_agent)
        empty_broadcast_agents_memory_buffer(agent)
    
    for neighbor in neighbors:
        send(sender, neighbor, message)
    
    if memory_size(agent) >= get_manet_agent_numbers(agent)*4/5:
        max_energetic_neighbor = max(neighbors, key=lambda x: x.energy)
        send(agent, max_energetic_neighbor, Message.DEPENDANCY)
    pass

@receive_and_deal_message.register
def _(agent, message: Message.DEPENDANCY):
    """Reçoit et traite les messages DEPENDANCY"""
    generic({ agent: [send, neighbors, add_to_local_dependants], message: [value, sender, set_value] })
    sender = message.sender()
    neighbors = agent.neighbors()
    if agent.energy > max(neighbors, key=lambda x: x.energy).energy:
        send(agent, sender, Message.ACK_DEPENDANCY)
        add_to_local_dependants(agent, sender)
        exec_message: Message.EXECUTE_LOCAL = Message.EXECUTE_LOCAL() # A changer avec le programme csp à executer
        exec_message.set_value({'func': compute_leader, 'csp': None, 'constants': None})
        send(agent, sender, exec_message)
    else:
        send(agent, sender, Message.NACK_DEPENDANCY)

@receive_and_deal_message.register
def _(agent, message: Message.ACK_DEPENDANCY):
    """Reçoit et traite les messages ACK_DEPENDANCY"""
    generic({ agent: [set_local_leader], message: [sender] })
    agent.set_local_leader(message.sender())
    
@receive_and_deal_message.register
def _(agent, message: Message.NACK_DEPENDANCY):
    """Reçoit et traite les messages NACK_DEPENDANCY"""
    generic({ agent: [send, add_to_excluded_agents_from_leader_list, excluded_agents_from_leader_list, neighbors], message: [sender] })
    add_to_excluded_agents_from_leader_list(agent, message.sender())
    neighbors = agent.neighbors()
    sorted_neighbors = sorted(neighbors, key=lambda x: x.energy, reverse=True)
    for neighbor in sorted_neighbors:
        if neighbor not in excluded_agents_from_leader_list(agent):
            send(agent, neighbor, Message.DEPENDANCY)
            return
    
@receive_and_deal_message.register
def _(agent, message: Message.EXECUTE_LOCAL):
    """Reçoit et traite les messages EXECUTE_LOCAL"""
    generic({ agent: [execute] , message: [sender, value] })
    value = message.value()
    sender = message.sender()
    if value['func'] == compute_leader:
        compute_leader(agent, value['csp'], value['constants'])
    elif value['func'] == compute_route:
        compute_route(agent, value['csp'], value['constants'])
        
@receive_and_deal_message.register
def _(agent, message: Message.BROADCAST_LEADER):
    """Reçoit et traite les messages BROADCAST_LEADER"""
    generic({ agent: [send, neighbors, set_local_leader, global_leader, set_local_leader ,global_leader_votes, \
        add_to_global_leader_votes, get_manet_agent_numbers], message: [value, sender] })
    # A compléter en fonction du comportement attendu pour agent
    sender = message.sender()
    proposed_leader = message.value()
    if proposed_leader not in global_leader_votes(agent):
        add_to_global_leader_votes(agent, sender, proposed_leader)
        for neighbor in agent.neighbors():
            send(agent, neighbor, message)
    if len(global_leader_votes(agent)) >= ( 4/5 )*get_manet_agent_numbers(agent):
        set_local_leader(agent, max(global_leader_votes(agent), key=lambda x: len([ leader for leader in global_leader_votes(agent) if leader == x ])))
        if agent == global_leader(agent):
            pass # A compléter en fonction du comportement attendu pour global leader
    pass

@receive_and_deal_message.register
def _(agent, message: Message.ROUTE):
    """Reçoit et traite les messages ROUTE, dont la valeur est un dict tel que {agent: [suceceurs_neighbours]}"""
    generic({ agent: [set_route,get_route, neighbors, send, set_route_predecessor], message: [value] })
    neighbors = agent.neighbors()
    routes = value(message)
    agent.set_route(routes[agent])
    agent.set_route_predecessor()
    for neighbor in neighbors:
        send(agent, neighbor, message)
        
        
    
@receive_and_deal_message.register
def _(agent, message: Message.EXECUTE_GLOBAL):
    """Reçoit et traite les messages UPDATE_MEMORY"""
    generic({ agent: [execute] }) # A compléter en fonction du comportement attendu pour agent
    
    pass

@receive_and_deal_message.register
def _(agent, message: Message.CHANGE):
    """Reçoit et traite les messages EXECUTE"""
    generic({ agent: [execute] }) # A compléter en fonction du comportement attendu pour agent
    pass




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


    

    