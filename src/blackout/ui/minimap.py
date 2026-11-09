# Auteur : Hamza
"""Mini-carte, utile pour vérifier les rayons et les déplacements."""

import pygame

from blackout.entities.player import Player
from blackout.world.maze import Maze


def draw_minimap(surface: pygame.Surface, maze: Maze, player: Player) -> None:
    """Dessine la grille et la position du joueur dans un coin de l'écran."""
    raise NotImplementedError
