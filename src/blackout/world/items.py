# Auteur : Maximilien
"""Objets à ramasser dans le labyrinthe."""

from dataclasses import dataclass
from enum import Enum, auto


class ItemKind(Enum):
    FUSE = auto()
    BATTERY = auto()


@dataclass(frozen=True)
class Item:
    kind: ItemKind
