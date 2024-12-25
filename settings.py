# Global game settings
from enum import Enum

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SNAKE_SIZE = 20
FOOD_SIZE = 20
SNAKE_SPEED = 15
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255,165,0)

class States(Enum):
    START = 0
    PLAYING = 1
    GAME_OVER = 2