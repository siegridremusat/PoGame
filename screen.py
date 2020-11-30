import pygame

from constants import *
from world import get_room


def create_screen(world):
    # Initialise screen
    pygame.init()
    board_width = WORLD_WIDTH * ROOM_SIZE
    board_height = WORLD_HEIGHT * ROOM_SIZE
    #élargir l'écran à droite pour indiquer la sortie
    screen = pygame.display.set_mode((board_width + ITEM_SIZE, board_height + ITEM_SIZE * 3))
    pygame.display.set_caption("SciencesPo Game")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    for x in range(WORLD_WIDTH):
        for y in range(WORLD_HEIGHT):
            if bool(x % 2) == bool(y % 2):

                color = (200, 200, 200)
            else:
                color = (250, 250, 250)

            pygame.draw.rect(
                background,
                color,
                [
                    x * ROOM_SIZE,
                    y * ROOM_SIZE,
                    ROOM_SIZE,
                    ROOM_SIZE,
                ],
            )

    return screen, background


def update_screen(screen, background, world, player, inventory, inventory2):
    player_x, player_y = player
    screen.blit(background, (0, 0))

    # couleur (red, green, blue)
    #range 0-255 avec noir:(0, 0, 0) et blanc:(255, 255, 255)
    pygame.draw.rect(
        screen,
        (250, 40, 100), #couleur du personnage
        [
            player_x * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2,
            player_y * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2,
            PLAYER_SIZE,
            PLAYER_SIZE,
        ],
    )
    
    for y in range(WORLD_HEIGHT):
        for x in range(WORLD_WIDTH):
            if "monster" in get_room(world, x, y):
                pygame.draw.circle(
                    screen,
                    (124, 64, 164), #couleur du monstre dans le jeu
                    (
                        x * ROOM_SIZE + ROOM_SIZE - MONSTER_RADIUS * 2,
                        y * ROOM_SIZE + ROOM_SIZE - MONSTER_RADIUS * 2,
                    ),
                    MONSTER_RADIUS,
                )
    
    #épée.s
    for y in range(WORLD_HEIGHT):
        for x in range(WORLD_WIDTH):
            if "sword" in get_room(world, x, y):
                pygame.draw.circle( #si tu as le temps, fais un rectangle ou importe une épée
                    screen,
                    (124, 164, 124), #couleur de l'épée dans le jeu
                    (
                        x * ROOM_SIZE + ROOM_SIZE - ITEM_SIZE * 2,
                        y * ROOM_SIZE + ROOM_SIZE - ITEM_SIZE * 2,
                    ),
                    ITEM_SIZE,
                )
 
    #bouclier
    for y in range(WORLD_HEIGHT):
        for x in range(WORLD_WIDTH):
            if "shield" in get_room(world, x, y):
                pygame.draw.circle( #si tu as le temps, fais un triangle ou importe un bouclier
                    screen,
                    (124, 164, 224), #couleur du bouclier  dans le jeu
                    (
                        x * ROOM_SIZE + ROOM_SIZE - ITEM_SIZE * 2,
                        y * ROOM_SIZE + ROOM_SIZE - ITEM_SIZE * 2,
                    ),
                    ITEM_SIZE,
                )


    #inventaire (kill streak)
    x = 10 #position (abscisse) du 1er monstre tué à apparaître dans le kill streak
    for item in inventory:
        y = WORLD_HEIGHT * ROOM_SIZE + ITEM_SIZE * 1.5 #position (ordonnée) des monstres dans l'inventaire
        pygame.draw.circle(
            screen,
            (124, 64, 164), #couleur du monstre dans l'inventaire
            (x, y),
            MONSTER_RADIUS,
        )
        
        x += MONSTER_RADIUS * 4
    
    #inventaire2 (inventaire du personnage)
    x = WORLD_WIDTH * ROOM_SIZE - 10 #position (abscisse) du 1er objet ramassé
    for item in inventory2: 
        y = WORLD_HEIGHT * ROOM_SIZE + ITEM_SIZE * 1.5 #position (ordonnée) des items dans l'inventaire 2
        pygame.draw.circle(
            screen,
            (124, 164, 124), #couleur des objets dans l'inventaire
            (x, y),
            ITEM_SIZE,
        )
        
        x -= ITEM_SIZE * 3
        
    #porte de sortie:
    x = WORLD_WIDTH * ROOM_SIZE #position (abscisse) de la porte
    y = (WORLD_HEIGHT * ROOM_SIZE)/3
    pygame.draw.rect(
        screen,
        (55, 55, 55), #couleur de la porte
        [
            WORLD_WIDTH * ROOM_SIZE,
            WORLD_HEIGHT/3 * ROOM_SIZE,
            ROOM_SIZE,
            ROOM_SIZE,
        ],
        )
        
        
    # TODO en théorie, il faudrait utiliser les éléments du monde pour afficher d'autres choses sur notre écran ...

    pygame.display.flip()
