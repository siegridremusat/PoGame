import pygame
import random

from constants import *
from screen import create_screen, update_screen
from world import create_world, get_room


def transfer_item(source, target, item):
    if item in source:
        source.remove(item)
        target.append(item)
    return source, target

def move_monster_y(monster):
    monster_x, monster_y = monster
    r = random.randint(-1, 1)
    while monster_y + r < 0 or monster_y + r >= WORLD_HEIGHT:
        r = random.randint(-1, 1)
    return [monster_x, monster_y]

def move_monster_x(monster):
    monster_x, monster_y = monster
    r = random.randint(-1, 1)
    while monster_x + r < 0 or monster_x + r >= WORLD_WIDTH:
        r = random.randint(-1, 1)
    return [monster_x, monster_y]



def main():
    # Création du "monde" tel que nous le définissons
    world = create_world()
    # Création des surfaces de dessin
    screen, background = create_screen(world)
    # Création d'une horloge
    clock = pygame.time.Clock()
    # Coordonnées [x, y] du joueur
    position = [0, 0]
    inventory = []
    inventory2 = []
    monster = [5, 5]
    

    # Les variables qui nous permettent de savoir si notre programme est en cours d'exécution ou s'il doit se terminer.
    alive = True
    running = True

    # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
    update_screen(screen, background, world, position, inventory, inventory2, monster)
    clock.tick()

    # Boucle "quasi" infinie, qui s'arrêtera si le joueur est mort, ou si l'arrêt du programme est demandé.
    while alive and running:
        # À chaque itération, on demande à pygame quels "évènements" se sont passés. Ces évènements sont l'interface
        # qui permet d'interragir avec l'extérieur du programme, et en particulier l'utilisateur (qui utilisera son
        # clavier, par exemple).
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # L'utilisateur souhaite fermer la fenêtre ou quitter par un autre moyen (menus ...).
                # À la prochaine itération de notre boucle principale, la condition sera fausse et le programme va se
                # terminer.
                running = False
            elif event.type == pygame.KEYDOWN:
                # Une touche du clavier a été pressée.
                if event.key == pygame.K_q:
                    # L'utilisateur a appuyé sur "Q", pour Quitter.
                    # À la prochaine itération de notre boucle principale, la condition sera fausse et le programme va
                    # se terminer.
                    running = False
#C'EST ICI QU'ON DÉPLACE LE JOUEUR!
#Pour l'instant le joueur "tue" les monstres en leur passant dessus.
#rajouer la condition épée
#rajouter la condition bouclier
#rajouter la condition potion?
                elif event.key == pygame.K_LEFT:
                    if position[0] > 0:
                        position = (position[0] - 1, position[1]) #déplacement du joueur
                        monster = move_monster_x(monster) #déplacement du monstre
                        
                        room = get_room(world, position[0], position[1])
                        if len(room) > 0 and "sword" in room or "shield" in room:
                            item = room[0]
                            room, inventory2 = transfer_item(room, inventory2, item)
                        
                        if monster == position:
                            if "sword" in inventory2:
                                inventory.append("monster")
                            elif "shield" in inventory2:
                                pass
                            else:
                                running = False
                            
                        elif len(room) > 0 and "monster" in room:
                            if "sword" in inventory2:
                                item = room[0]
                                room, inventory = transfer_item(room, inventory, item)
                            elif "shield" in inventory2:
                                pass                                
                            else:
                                running = False
                       

                elif event.key == pygame.K_RIGHT:
                    if position[0] < WORLD_WIDTH - 1: 
                        position = (position[0] + 1, position[1])
                        monster = move_monster_x(monster)
                        room = get_room(world, position[0], position[1])
                        if len(room) > 0 and "sword" in room or "shield" in room:
                            item = room[0]
                            room, inventory2 = transfer_item(room, inventory2, item)
                        elif len(room) > 0 and "monster" in room:
                            if "sword" in inventory2:
                                item = room[0]
                                room, inventory = transfer_item(room, inventory, item)
                            elif "shield" in inventory2:
                                pass
                            else:
                                running = False
                    #ajout d'une sortie
                    elif position[0] == WORLD_WIDTH - 1 and position[1] == WORLD_HEIGHT/3:
                        running = False

                elif event.key == pygame.K_UP:
                    if position[1] > 0:
                        position = (position[0], position[1] - 1)
                        monster = move_monster_y(monster)
                        room = get_room(world, position[0], position[1])
                        if len(room) > 0 and "sword" in room or "shield" in room:
                            item = room[0]
                            room, inventory2 = transfer_item(room, inventory2, item)
                        elif len(room) > 0 and "monster" in room:
                            if "sword" in inventory2:
                                item = room[0]
                                room, inventory = transfer_item(room, inventory, item)
                            elif "shield" in inventory2:
                                pass
                            else:
                                running = False
                            
                elif event.key == pygame.K_DOWN:
                    if position[1] < WORLD_HEIGHT - 1:
                        position = (position[0], position[1] + 1)
                        monster = move_monster_y(monster)
                        room = get_room(world, position[0], position[1])
                        if len(room) > 0 and "sword" in room or "shield" in room:
                            item = room[0]
                            room, inventory2 = transfer_item(room, inventory2, item)
                        elif len(room) > 0 and "monster" in room:
                            if "sword" in inventory2:
                                item = room[0]
                                room, inventory = transfer_item(room, inventory, item)
                            elif "shield" in inventory2:
                                pass
                            else:
                                running = False
                
                
                            

#ESSAYER DE FAIRE UNE TOUCHE TÉLÉPORTER?
                elif event.key == pygame.K_t:
                    position = [random.randint(0, WORLD_WIDTH - 1), random.randint(0, WORLD_HEIGHT - 1)]
                    room = get_room(world, position[0], position[1])
                    if len(room) > 0 and "sword" in room or "shield" in room:
                        item = room[0]
                        room, inventory2 = transfer_item(room, inventory2, item)
                    elif len(room) > 0 and "monster" in room:
                        if "sword" in inventory2:
                            item = room[0]
                            room, inventory = transfer_item(room, inventory, item)
                        elif "shield" in inventory2:
                            pass
                        else:
                            break
                elif event.key == pygame.K_SPACE:
                    room = get_room(world, position[0], position[1])
                    if len(room) > 0:
                        item = room[0]
                        room, inventory = transfer_item(room, inventory, item)
            elif event.type == pygame.KEYUP:
                # Une touche du clavier a été relachée.
                pass
            
            #tentative de faire bouger les monstres
#            for y in range(WORLD_HEIGHT - 1):
#                for x in range(WORLD_WIDTH - 1):
#                    room = [x, y]
#                    room2 = [random.randint(x - 1, x + 1), random.randint(y - 1, y + 1)]
 #                   if "monster" in room:
 #                       transfer_item(room, room2, "monster")
                        #position[x] = random.randint(x - 1, x + 1)
                        #position[y] = random.randint(y - 1, y + 1)
                        
            for y in range(WORLD_HEIGHT - 1):
                for x in range(WORLD_WIDTH - 1):
                    room = [x, y]
                    room2 = [random.randint(x - 1, x + 1), random.randint(y - 1, y + 1)]
                    item = "monster"
                    if "monster" in get_room(world, x, y):
                        transfer_item(room, room2, item)
                                      
                        
        # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
        update_screen(screen, background, world, position, inventory, inventory2, monster)
        clock.tick()
        
        if len(inventory) >= 10:
            #trouver d'autres moyens plus cool d'afficher la victoire
            break


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
