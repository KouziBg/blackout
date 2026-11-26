# Auteur : Hamza
"""Mini-carte, utile pour vérifier les rayons et les déplacements."""

import pygame
import math

from blackout.entities.monster import Monster
from blackout.entities.player import Player
from blackout.world.maze import Maze

TAILLE_CASE = 4  #taille d'une case de la mini carte en pixel
COULEUR_MUR = (40, 40, 40)   # couleur du mur
COULEUR_SOL = (200, 200, 200)   # couleur du sol
COULEUR_JOUEUR = (255, 0, 0)   # couleur du point du joueur
COULEUR_MONSTRE = (0, 170, 0)   # couleur du point du monstre (Noham)


def draw_minimap(
    surface: pygame.Surface, maze: Maze, player: Player, monster: Monster | None = None
) -> None:
    """Dessine la grille et la position du joueur dans un coin de l'écran."""
    ## dessin de la grille : 
    nb_lignes = len(maze.cells) #nombre de lignne de la grille

    for y in range(nb_lignes):  
        nb_colonnes = len(maze.cells[y])  # nombre de colonne 

        for x in range(nb_colonnes): 
            if maze.is_wall(x, y):  #si la case x, y est un mur 
                color = COULEUR_MUR # on la dessine en noir 
            else: #sinon c'est du sol 
                color = COULEUR_SOL 

            pygame.draw.rect(surface, color, (x * TAILLE_CASE, y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

    #convertir la position du joueur en pixel     
    pos_x = player.x * TAILLE_CASE
    pos_y = player.y * TAILLE_CASE

    #dessin du joueur
    pygame.draw.circle(surface, COULEUR_JOUEUR, (int(pos_x), int(pos_y)), 2)

    # calculer le trait du regard du joueur
    bout_x = pos_x + math.cos(player.angle) * 6
    bout_y = pos_y + math.sin(player.angle) * 6

    pygame.draw.line(surface, COULEUR_JOUEUR, (pos_x, pos_y), (bout_x, bout_y), 1)

    # on dessine le monstre en point vert, s'il y en a un (Noham)
    if monster is not None:
        monstre_x = int(monster.x * TAILLE_CASE)
        monstre_y = int(monster.y * TAILLE_CASE)
        pygame.draw.circle(surface, COULEUR_MONSTRE, (monstre_x, monstre_y), 2)
     





