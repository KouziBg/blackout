# Auteur : Chamss
"""Dessin des murs en fausse 3D."""

import pygame

from blackout.entities.player import Player
from blackout.world.maze import Maze


def render_walls(surface: pygame.Surface, maze: Maze, player: Player) -> list[float]:
    """Dessine une colonne de mur par rayon.

    Renvoie la distance corrigée de l'effet fish-eye pour chaque colonne.
    Ce tableau sert ensuite à cacher les sprites derrière les murs.
    """
    raise NotImplementedError
