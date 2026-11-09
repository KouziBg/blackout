# Auteur : Hamza
"""Dessin du monstre et des objets dans la vue 3D."""

from dataclasses import dataclass

import pygame

from blackout.entities.player import Player


@dataclass
class Sprite:
    """Image placée dans le monde, en unités de grille."""

    x: float
    y: float
    image: pygame.Surface
    height: float = 1.0


def render_sprites(
    surface: pygame.Surface,
    sprites: list[Sprite],
    player: Player,
    depth: list[float],
) -> None:
    """Dessine les sprites du plus loin au plus proche, cachés par les murs."""
    raise NotImplementedError
