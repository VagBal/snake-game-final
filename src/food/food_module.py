import pygame
import random
from settings import FOOD_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, RED

class Food:
    def __init__(self):
        self.position = self.random_position()
    
    def random_position(self):
        # Calculate the maximum number of food items that can fit horizontally
        max_x = (SCREEN_WIDTH - FOOD_SIZE) // FOOD_SIZE
        
        # Calculate the maximum number of food items that can fit vertically
        max_y = (SCREEN_HEIGHT - FOOD_SIZE) // FOOD_SIZE
        
        # Generate a random x-coordinate within the allowed range
        x = random.randint(0, max_x) * FOOD_SIZE
        
        # Generate a random y-coordinate within the allowed range
        y = random.randint(0, max_y) * FOOD_SIZE
        
        # Return the position as a tuple (x, y)
        return (x, y)
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (*self.position, FOOD_SIZE, FOOD_SIZE))