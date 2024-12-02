from interfaces import *
from utils import *
def compute_leader(agent,csp_prog, constants):
    """Compute the leader of the network: l'agent depuis lequel la perte énergétique est minimale pour un broadcast
    Variables importantes:
    agent.get_memory(): list des agents en mémoire ( varie en fonction des agents)
    agent.energy(): énergie de l'agent
    agent.neighbors(): list des voisins de l'agent    
    """
    generic({ agent: [get_memory,energy,neighbors]})
    pass