# Auteur : Hamza
"""Boucle principale et états du jeu."""

from enum import Enum, auto

import pygame

from blackout import config
from blackout.entities.player import Player #classe du joueur 
from blackout.ui.minimap import draw_minimap #fonction qui dessine la carte 
from blackout.world.maze import Maze #classe du labyrinthe


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
        
        self.maze = Maze.from_file(config.TEST_MAP)  #charge la carte de test
        self.player = Player(1.5, 1.5)     #joueur au centtre de la case (1, 1)
    


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

        keys = pygame.key.get_pressed() # on recupere les touches du clavier


        if keys[pygame.K_z] or keys[pygame.K_UP]: #si Z ou flecheHAUT enfoncée
            self.player.move(config.PLAYER_SPEED * dt, self.maze)  # avancer avec vitesse x temps ecoulé ( dt ) 

        if keys[pygame.K_s] or keys[pygame.K_DOWN]: #si S ou fleche du bas enfoncée 
            self.player.move(-config.PLAYER_SPEED * dt, self.maze) # on recule donc distance negative 

        if keys[pygame.K_q] or keys[pygame.K_LEFT]: # si q ou fleche gauche enfoncé 
            self.player.turn(-config.PLAYER_TURN_SPEED * dt)  #tourner vers la gauche 

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:    #si d ou fleche droite enfoncée
            self.player.turn(config.PLAYER_TURN_SPEED * dt)   # tourner vers la droite

    def draw(self) -> None:
        """Dessine l'image basse résolution, puis l'agrandit dans la fenêtre."""
        self.frame.fill((0, 0, 0))
        #render_walls(self.frame, self.maze, self.player)
        draw_minimap(self.frame, self.maze, self.player)
        pygame.transform.scale(self.frame, self.window.get_size(), self.window)
        pygame.display.flip()
