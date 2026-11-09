# Auteur : Noham
"""Machine à états du monstre."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

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
    """Le monstre poursuit le joueur."""

    def update(
        self, monster: Monster, player: Player, maze: Maze, dt: float
    ) -> MonsterState:
        raise NotImplementedError


class SearchState(MonsterState):
    """Le monstre fouille la dernière position connue du joueur."""

    def update(
        self, monster: Monster, player: Player, maze: Maze, dt: float
    ) -> MonsterState:
        raise NotImplementedError
