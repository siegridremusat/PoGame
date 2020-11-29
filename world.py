import random

from constants import *

def create_world():
    world = []


    for y in range(WORLD_HEIGHT): #cette boucle en 1e pour "finir par les colonnes
        for x in range(WORLD_WIDTH): #cette boucle en 2e pour "commencer" par les lignes
            #intégrer l'épée au hasard sur la map
            #for world[x]
            #for c in range((WORLD_HEIGHT/2, WORLD_HEIGHT), (WORLD_WIDTH/2, WORLD_WIDTH)):         
            #        world.append(["sword"])
            if random.randint(0, 9) == 0 and (x, y) != (0, 0):
                world.append(["monster"])
            if random.randint(0, 50) == 0 and (x, y) != (0, 0):
                world.append(["sword"]) #solution pas idéale mais allons y petit à petit
                #ca ajoute une ou plusieurs épées au hasard sur la map
                #comment ajouter une seule épée? comment contrôler la zone ou elle apparaît?     
            else:
                world.append([])
    
    return world


def get_index(x, y):
    return y * WORLD_WIDTH + x

def get_room(world, x, y):
    index = get_index(x, y)
    return world[index]