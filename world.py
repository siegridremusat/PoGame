import random

from constants import *

def create_world():
    world = []
    # TODO Il faut remplir notre terrain ici, en fonction de la taille choisie préalablement.
    #bon ben go hein
    world(range(WORLD_WIDTH * WORLD_HEIGHT - 1))
    
    n = int
    for n in range(0, WORLD_WIDTH * WORLD_HEIGHT - 1):
        world[n] = random.choices(available_items, k= random.randint(0, len(available_items)))

    return world


#imprimer la liste autant de fois qu'il y a de valeurs:
for i in range(len(l)):
    print(l[i])#imprimer la liste autant de fois qu'il y a de valeurs:
for i in range(len(l)):
    print(l[i])