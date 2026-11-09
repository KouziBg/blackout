# Auteur : Hamza
"""Joueur."""

from dataclasses import dataclass

from blackout.world.maze import Maze


@dataclass
class Player:
    """Position en unités de grille et angle de vue en radians."""

    x: float
    y: float
    angle: float = 0.0

    def move(self, distance: float, maze: Maze) -> None:
        """Avance dans la direction du regard, ou recule si distance < 0.

        Le joueur glisse le long des murs : x et y sont testés séparément.
        """
        raise NotImplementedError

    def turn(self, delta: float) -> None:
        """Tourne le regard de delta radians."""
        raise NotImplementedError
