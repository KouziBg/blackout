# Auteur : Hamza
"""Boucle principale et états du jeu."""

from enum import Enum, auto

import pygame

from blackout import config


class GameState(Enum):
    MENU = auto()
    PLAYING = auto()
    VICTORY = auto()
    DEFEAT = auto()


class Game:
    """Crée la fenêtre et fait tourner le jeu."""

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(config.TITLE)
        self.window = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        self.frame = pygame.Surface((config.RENDER_WIDTH, config.RENDER_HEIGHT))
        self.clock = pygame.time.Clock()
        self.state = GameState.PLAYING
        self.running = True
        # TODO(Hamza) : créer ici le labyrinthe et le joueur.

    def run(self) -> None:
        """Répète entrées, logique et affichage jusqu'à la fermeture."""
        while self.running:
            dt = self.clock.tick(config.FPS) / 1000
            self.handle_events()
            self.update(dt)
            self.draw()
        pygame.quit()

    def handle_events(self) -> None:
        """Traite la fermeture de la fenêtre et la touche Échap."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def update(self, dt: float) -> None:
        """Avance la logique du jeu de dt secondes."""
        # TODO(Hamza) : lire le clavier et déplacer le joueur.

    def draw(self) -> None:
        """Dessine l'image basse résolution, puis l'agrandit dans la fenêtre."""
        self.frame.fill((0, 0, 0))
        # TODO(Hamza) : appeler render_walls et draw_minimap.
        pygame.transform.scale(self.frame, self.window.get_size(), self.window)
        pygame.display.flip()
