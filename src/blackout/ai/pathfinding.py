# Auteur : Noham
"""Recherche de chemin."""

from blackout.world.maze import Maze


def find_path(
    maze: Maze, start: tuple[int, int], goal: tuple[int, int]
) -> list[tuple[int, int]]:
    """Renvoie le plus court chemin avec A*, start et goal compris.

    Renvoie [start] si start == goal, et une liste vide s'il n'y a aucun chemin.
    Le voisinage vient uniquement de maze.neighbours().
    """
    raise NotImplementedError
