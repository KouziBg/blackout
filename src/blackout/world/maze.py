# Auteur : Maximilien
"""Grille du labyrinthe, partagée par le rendu, la génération et l'IA."""

from __future__ import annotations

import random
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
        # On découpe en lignes et on ignore les lignes vides.
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        if not lines:
            raise ValueError("Le texte du labyrinthe est vide.")

        width = len(lines[0])
        if any(len(line) != width for line in lines):
            raise ValueError("Toutes les lignes doivent avoir la même longueur.")

        symbols = {"#": Cell.WALL, ".": Cell.FLOOR}
        cells = []
        for line in lines:
            row = []
            for char in line:
                if char not in symbols:
                    raise ValueError(f"Caractère inconnu : {char!r}")
                row.append(symbols[char])
            cells.append(row)

        return cls(width, len(lines), cells)

    @classmethod
    def from_file(cls, path: Path) -> Maze:
        """Crée un labyrinthe depuis un fichier texte."""
        text = Path(path).read_text(encoding="utf-8")
        return cls.from_text(text)

    @classmethod
    def generate(cls, width: int, height: int, seed: int | None = None) -> Maze:
        """Génère un labyrinthe par parcours en profondeur (DFS).

        width et height doivent être impairs et supérieurs ou égaux à 5,
        sinon la fonction lève ValueError. Le contour est entièrement en murs,
        et toutes les cases de sol sont reliées. Une même graine donne
        toujours le même labyrinthe.
        """
        if width < 5 or height < 5 or width % 2 == 0 or height % 2 == 0:
            raise ValueError("width et height doivent être impairs et au moins 5.")

        # Même graine = même suite de choix aléatoires = même labyrinthe.
        rng = random.Random(seed)

        # Au départ, tout est en murs (une liste par ligne, pas partagée).
        cells = [[Cell.WALL for _ in range(width)] for _ in range(height)]

        # On creuse la case de départ et on la met dans la pile.
        cells[1][1] = Cell.FLOOR
        stack = [(1, 1)]

        while stack:
            x, y = stack[-1]

            # Voisines à 2 cases, encore en murs et loin du bord.
            candidates = []
            for dx, dy in ((2, 0), (-2, 0), (0, 2), (0, -2)):
                nx, ny = x + dx, y + dy
                if (
                    1 <= nx <= width - 2
                    and 1 <= ny <= height - 2
                    and cells[ny][nx] == Cell.WALL
                ):
                    candidates.append((nx, ny))

            if not candidates:
                # Impasse : on revient en arrière.
                stack.pop()
            else:
                nx, ny = rng.choice(candidates)
                # On creuse la case du milieu puis la voisine choisie.
                cells[(y + ny) // 2][(x + nx) // 2] = Cell.FLOOR
                cells[ny][nx] = Cell.FLOOR
                stack.append((nx, ny))

        return cls(width, height, cells)

    def is_wall(self, x: int, y: int) -> bool:
        """Indique si la case est un mur. Hors de la grille, c'est un mur."""
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return True
        return self.cells[y][x] == Cell.WALL

    def neighbours(self, x: int, y: int) -> list[tuple[int, int]]:
        """Renvoie les cases de sol voisines, sans les diagonales."""
        result = []
        # Ordre : droite, gauche, bas, haut.
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if not self.is_wall(x + dx, y + dy):
                result.append((x + dx, y + dy))
        return result

    def wall_positions(self) -> list[tuple[int, int]]:
        """Renvoie les coordonnées (x, y) de tous les murs."""
        return [
            (x, y)
            for y in range(self.height)
            for x in range(self.width)
            if self.cells[y][x] == Cell.WALL
        ]
