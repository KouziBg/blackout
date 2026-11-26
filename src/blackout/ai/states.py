# Auteur : Noham
"""Machine à états du monstre."""

from __future__ import annotations

import math
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from blackout.ai.pathfinding import find_path

if TYPE_CHECKING:
    from blackout.entities.monster import Monster
    from blackout.entities.player import Player
    from blackout.world.maze import Maze


class MonsterState(ABC):
    """Un comportement du monstre."""

    @abstractmethod
    def update(
        self, monster: Monster, player: Player, maze: Maze, dt: float
    ) -> MonsterState:
        """Applique le comportement et renvoie l'état suivant."""


class PatrolState(MonsterState):
    """Le monstre se déplace entre des cases choisies au hasard."""

    def update(
        self, monster: Monster, player: Player, maze: Maze, dt: float
    ) -> MonsterState:
        raise NotImplementedError


class ChaseState(MonsterState):
    """Le monstre poursuit le joueur en suivant le chemin donné par A*."""

    def __init__(self) -> None:
        # Retient la case du joueur au dernier calcul, None au départ parce qu'on n'a encore jamais calculé de chemin.
        self.player_cell: tuple[int, int] | None = None

    def update(
        self, monster: Monster, player: Player, maze: Maze, dt: float
    ) -> MonsterState:
        """Recalcule le chemin si besoin, avance d'un pas, et reste en poursuite."""
        monster_cell = (int(monster.x), int(monster.y))
        player_cell = (int(player.x), int(player.y))

        # On relance A* seulement quand le joueur change de case ou que le chemin est vide.
        # Sinon on le calculerait 60 fois par seconde pour trouver le même chemin.
        if player_cell != self.player_cell or not monster.path:
            monster.path = find_path(maze, monster_cell, player_cell)
            self.player_cell = player_cell
            # On retire la première case du chemin parce que le monstre est déjà dessus.
            if monster.path and monster.path[0] == monster_cell:
                monster.path.pop(0)

        if monster.path:
            self._move_towards_next_cell(monster, dt)

        return self

    def _move_towards_next_cell(self, monster: Monster, dt: float) -> None:
        """Avance vers le centre de la prochaine case, à la vitesse du monstre."""
        cell_x, cell_y = monster.path[0]
        target_x = cell_x + 0.5
        target_y = cell_y + 0.5

        dx = target_x - monster.x
        dy = target_y - monster.y
        distance = math.hypot(dx, dy)
        step = monster.speed * dt

        if distance <= step:
            # Il arrive au centre de la case : on le pose dessus et on enlève la case du chemin.
            monster.x = target_x
            monster.y = target_y
            monster.path.pop(0)
        else:
            # Il avance d'un pas vers la case sans se téléporter.
            # Diviser par distance garde seulement la direction, step donne la longueur du pas.
            monster.x += dx / distance * step
            monster.y += dy / distance * step


class SearchState(MonsterState):
    """Le monstre fouille la dernière position connue du joueur."""

    def update(
        self, monster: Monster, player: Player, maze: Maze, dt: float
    ) -> MonsterState:
        raise NotImplementedError
