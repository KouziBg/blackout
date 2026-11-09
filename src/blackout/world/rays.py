# Auteur : Chamss
"""Calcul d'un rayon dans la grille, sans aucun affichage."""

from dataclasses import dataclass

from blackout.world.maze import Maze


@dataclass(frozen=True)
class RayHit:
    """Résultat d'un rayon.

    distance : distance brute entre l'origine et le mur touché.
    side : 0 si le rayon touche une face verticale, 1 pour une face horizontale.
    wall_x : position du point d'impact sur le mur, entre 0 et 1.
    """

    distance: float
    side: int
    wall_x: float


def cast_ray(maze: Maze, x: float, y: float, angle: float) -> RayHit:
    """Lance un rayon depuis (x, y) jusqu'au premier mur, avec l'algorithme DDA."""
    raise NotImplementedError
