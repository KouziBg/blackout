# Auteur : Maximilien
"""Contenu d'un étage."""

from __future__ import annotations

from dataclasses import dataclass, field

from blackout.world.items import Item
from blackout.world.maze import Maze


@dataclass
class Level:
    """Un étage : son labyrinthe, ses objets et sa sortie."""

    number: int
    maze: Maze
    start: tuple[int, int]
    exit: tuple[int, int]
    items: dict[tuple[int, int], Item] = field(default_factory=dict)

    @classmethod
    def create(cls, number: int, seed: int | None = None) -> Level:
        """Génère un étage de plus en plus grand selon son numéro."""
        raise NotImplementedError
