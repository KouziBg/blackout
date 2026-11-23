# Auteur : Hamza
"""Joueur."""

import math
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

        nouveau_x = self.x + math.cos(self.angle) * distance   #le nouveau x quon a apres le deplacement 
        nouveau_y = self.y + math.sin(self.angle) * distance   #le nouveau y quon a apres le deplacement 

        if not maze.is_wall(int(nouveau_x), int(self.y)): # on regarde si case du nouveau x c un mur ? 
            self.x = nouveau_x      #si ce n'est pas un mur, on accepte le nouveau x

        if not maze.is_wall(int(self.x), int(nouveau_y)): # on regarde si case du nouveau y c un mur ?
            self.y = nouveau_y     #si ce n'est pas un mur, on accepte le nouveau y


    def turn(self, delta: float) -> None:
        """Tourne le regard de delta radians."""
        self.angle += delta # ici on ajoute delta a l'angle de vue
