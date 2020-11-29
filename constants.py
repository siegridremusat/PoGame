# Quelques constantes qui nous seront utiles pour garder notre programme lisible ...
WORLD_WIDTH = 16
WORLD_HEIGHT = 12
ROOM_SIZE = 54
PLAYER_SIZE = 16
MONSTER_RADIUS = 4 #TAILLE DES MONSTRES
ITEM_SIZE = 8 #TAILLE DES OBJETS

#penser à combien on en fait


#AJOUTS PAR SIEGRID
available_items = ['bow', 'key', 'potion', 'cape', 'magic hat', 'sword',
                       'treasure','pen']
#on enlève tous ces objets et on place 1 épée au hasard sur la map

#si on a le temps:
#placer un bouclier (protège mais ne tue pas les monstres) au hasard près de (0,0)
#placer une potion qui repousse les monstres pour 10 déplacements (coucou Pokémon)


#CONDITION DE VICTOIRE — IDÉES:
#faire une porte de sortie (en bas à droite)
#tuer tous les monstres (dans ce cas il faut faire un kill count, aka un inventaire bis)