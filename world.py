import random

from constants import *

def create_world():
    world = []


    for y in range(WORLD_HEIGHT): #cette boucle en 1e pour "finir par les colonnes
        for x in range(WORLD_WIDTH): #cette boucle en 2e pour "commencer" par les lignes
 
            if random.randint(0, 9) == 0 and (x, y) != (0, 0):
                world.append(["monster"])
    

#            if (x, y) == (random.randint(WORLD_WIDTH/2, WORLD_WIDTH - 1), random.randint(WORLD_HEIGHT/2, WORLD_HEIGHT - 1)):
#                world.append(["sword"])    


#            if (x, y) == (random.randint(1, WORLD_WIDTH/2), random.randint(1, WORLD_HEIGHT/2)):
#                world.append(["shield"])
               
                
            else:
                world.append([])
    
    
#    sword_x, sword_y = 0, 0
    s_x = random.randint(0, WORLD_WIDTH - 1)
    s_y = random.randint(0, WORLD_HEIGHT - 1)
    world[s_y * WORLD_WIDTH + s_x] = ["sword"]
    
    r_x = random.randint(0, WORLD_WIDTH - 1)
    r_y = random.randint(0, WORLD_HEIGHT - 1)
    world[r_y * WORLD_WIDTH + r_x] = ["shield"]
    
#    list((x, y)) == (random.randint(WORLD_WIDTH/2, WORLD_WIDTH - 1), random.randint(WORLD_HEIGHT/2, WORLD_HEIGHT - 1))
#    world.append("sword")
            
            
    return world


def get_index(x, y):
    return y * WORLD_WIDTH + x

def get_room(world, x, y):
    index = get_index(x, y)
    return world[index]
