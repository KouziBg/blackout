"""Réglages du jeu."""

from math import pi
from pathlib import Path

ASSETS_DIR = Path(__file__).parent / "assets"
MAPS_DIR = ASSETS_DIR / "maps"
TEXTURES_DIR = ASSETS_DIR / "textures"
SOUNDS_DIR = ASSETS_DIR / "sounds"
TEST_MAP = MAPS_DIR / "test.txt"

TITLE = "Blackout"
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540
RENDER_WIDTH = 320
RENDER_HEIGHT = 180
FPS = 60

FIELD_OF_VIEW = pi / 3

PLAYER_SPEED = 2.5
PLAYER_TURN_SPEED = 2.4
PLAYER_RADIUS = 0.2
