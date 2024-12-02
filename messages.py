from enum import Enum

class Message(Enum):
    # Etape 1: broadcast des données internes, mise en commun de toutes les informations dans le systeme
    BROADCAST_STATUS = 1 # Envoit à tout le monde l'état actuel de l'agent
    
    # Un agent passe à l'étape 2 s'il a au moins 2/3 des autres agents en mémoire
    # Etape 2: séléction du leader local:
    DEPENDANCY =  2# Chaque agent envoit DEPENDANCY à son voisin le plus énergétique
    ACK_DEPENDANCY = 3 # Si l'agent correspondant est le plus énergétique de son voisinage, 
                        # il envoit ACK_DEPENDANCY à ceux qui lui ont envoyé DEPENDANCY
    NACK_DEPENDANCY = 4 # Si l'agent correspondant n'est pas le plus énergétique de son voisinage, 
                        # il envoit NACK_DEPENDANCY à ceux qui lui ont envoyé DEPENDANCY
    
    #Etape 3: Election du leader global
    EXECUTE_LOCAL = 5 # Exécute le programme csp qui permet de déterminer le leader global en minimisant la somme des couts energetiques de transport 
                # et en maximisant l'energie du leader et de son voisinage.
    BROADCAST_LEADER = 6 # Envoit à tout le monde le leader global trouvé par le voisinage.
                        # Si un agent reçoit un leader qu'il a déjà dans sa mémoire il ne fait rien.
                        # Chaque agent change son leader global par vote majoritaire.
                        # Si égalité => possibilité de scission du réseau, pas grave, c'est fun.
    
    
    #Etape 4: Calcul de la route optimale de transport d'information
    # EXECUTE_LOCAL envoyé aux voisins du leader global par le leader global pour calculer la route optimale
    ROUTE = 7 # Envoit à tout le monde la route optimale trouvée par le leader global.
                        # Pour envoyer cette route, on utilise de proche en proche si il n'y a pas encore de route définie
                        # Ou on utilise la route définie si elle est déjà définie et on la met à jour.
    
    #Etape 5: Ordre de calcul des contraintes du système
    EXECUTE_GLOBAL = 8 # envoyé à tout les agents du réseau par le leader global pour calculer les contraintes du système
                        # en suivant la route calculée. On joint au message soit le programme csp et les contraintes à calculer, 
                        # ou dans le cadre de la simulation seulement le coût énergétique du calcul estimé.
    
    CHANGE = 9 # Envoit à tout le monde le changement de mémoire due à l'execution
    
    