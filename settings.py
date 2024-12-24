# Global game settings
from enum import Enum

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SNAKE_SIZE = 20
FOOD_SIZE = 20
SNAKE_SPEED = 15

class States(Enum):
    START = 0
    PLAYING = 1
    GAME_OVER = 2