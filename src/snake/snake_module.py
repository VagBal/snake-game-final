import pygame
from settings import SNAKE_SIZE

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)] # Initial snake position
        self.direction = (SNAKE_SIZE, 0) # Initial snake direction (moving right)
    
    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1]) # explain
        self.body.insert(0, new_head)
        self.body.pop()

    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1 != self.direction): # explain
            self.direction = new_direction

    def grow(self):
        self.body.append(self.body[-1]) # Duplicate the last segment

    def draw(self, sceen):
        for segment in self.body:
            pygame.draw.rect(sceen, (0, 255, 0), (*segment, SNAKE_SIZE, SNAKE_SIZE))