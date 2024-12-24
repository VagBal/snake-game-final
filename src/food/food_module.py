import pygame
import random
from settings import FOOD_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

class Food:
    def __init__(self):
        self.position = self.random_position()
    
    def random_position(self):
        x = random.randint(0, (SCREEN_WIDTH - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE # explain
        y = random.randint(0, (SCREEN_WIDTH - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE # explain
        return (x, y)
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (*self.position, FOOD_SIZE, FOOD_SIZE))