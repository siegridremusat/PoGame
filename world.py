import random

from constants import *

def create_world():
    world = []
    # TODO Il faut remplir notre terrain ici, en fonction de la taille choisie préalablement.
    #bon ben go hein
#    world(range(WORLD_WIDTH * WORLD_HEIGHT - 1))
    
    n = int
    for n in range(0, WORLD_WIDTH * WORLD_HEIGHT - 1):
        world[n] = random.choices(available_items, k= random.randint(0, len(available_items)))
        #chaque élément world[n] de la master liste world est une liste contenant un nombre
        #aléatoire d'éléments (de zéro à tous) issus de la liste des objets possibles qui est
        #dans les constantes

    return world

def get_index(x, y):
    return y * WORLD_WIDTH + x

def transfer_item(source, target, item):
    if item in source:
        source.remove(item)
        target.append(item)
    return source, target
    
def run_game(available_items):
    ground = random.choices(available_items, k=5)
    #choisit 5 items au pif dans la liste d'objets dispo
    inventory = []
    
    while True:
        print("sol :", ground, "inventaire :", inventory)
        ordre = input(
            "Do you want to: TAKE <objet> (press T) , PUT <objet> DOWN (press P) or CONTINUE (press C) > "
        ).split() #split transforme l'ordre "prendre ratatouille" en une liste ["prendre", "ratatouille"]
        
        if ordre[0].lower().startswith("cont"):
            break      
#event.key == pygame.K_LEFT:
        if ordre[0].lower().startswith("pre"):
            ground, inventory = transfer_item(ground, inventory, ordre[1]) #ordre[1] = objet que tu veux prendre. Patate.
        elif ordre[0].lower().startswith("pos"):
            inventory, ground = transfer_item(inventory, ground, ordre[1])

