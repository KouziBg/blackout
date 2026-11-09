# Auteur : Maximilien
"""Grille du labyrinthe, partagée par le rendu, la génération et l'IA."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class Cell(Enum):
    FLOOR = 0
    WALL = 1


@dataclass
class Maze:
    """Grille de cases, lue avec cells[y][x]."""

    width: int
    height: int
    cells: list[list[Cell]]

    @classmethod
    def from_text(cls, text: str) -> Maze:
        """Crée un labyrinthe depuis un texte ('#' = mur, '.' = sol).

        Lève ValueError si les lignes n'ont pas toutes la même longueur.
        """
        raise NotImplementedError

    @classmethod
    def from_file(cls, path: Path) -> Maze:
        """Crée un labyrinthe depuis un fichier texte."""
        raise NotImplementedError

    @classmethod
    def generate(cls, width: int, height: int, seed: int | None = None) -> Maze:
        """Génère un labyrinthe par parcours en profondeur (DFS).

        width et height doivent être impairs et supérieurs ou égaux à 5,
        sinon la fonction lève ValueError. Le contour est entièrement en murs,
        et toutes les cases de sol sont reliées. Une même graine donne
        toujours le même labyrinthe.
        """
        raise NotImplementedError

    def is_wall(self, x: int, y: int) -> bool:
        """Indique si la case est un mur. Hors de la grille, c'est un mur."""
        raise NotImplementedError

    def neighbours(self, x: int, y: int) -> list[tuple[int, int]]:
        """Renvoie les cases de sol voisines, sans les diagonales."""
        raise NotImplementedError

    def wall_positions(self) -> list[tuple[int, int]]:
        """Renvoie les coordonnées (x, y) de tous les murs."""
        raise NotImplementedError
