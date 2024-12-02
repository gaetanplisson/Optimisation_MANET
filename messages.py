from enum import Enum

class Message(Enum):
    BROADCAST_STATUS = 1 # Envoit à tout le monde l'état actuel de l'agent
    EXECUTE = 2  # Exécute un programme csp
    BROADCAST_ORDER = 3 # Envoit à tout le monde un ordre d'évolution du système, résultat d'une execution
    UPDATE_MEMORY = 4  # Met à jour la mémoire d'un agent
    