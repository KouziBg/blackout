# Auteur : Noham
"""Monstre."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from blackout.ai.states import MonsterState
    from blackout.entities.player import Player
    from blackout.world.maze import Maze


@dataclass
class Monster:
    """Position, vitesse, état courant et chemin à suivre."""

    x: float
    y: float
    state: MonsterState
    speed: float = 1.5
    path: list[tuple[int, int]] = field(default_factory=list)

    def update(self, player: Player, maze: Maze, dt: float) -> None:
        """Laisse l'état courant agir (déplacement compris), puis passe à l'état suivant."""
        self.state = self.state.update(self, player, maze, dt)

    def can_see(self, player: Player, maze: Maze) -> bool:
        """Indique si aucun mur ne sépare le monstre du joueur, avec cast_ray."""
        raise NotImplementedError
