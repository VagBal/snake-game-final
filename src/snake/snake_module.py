import pygame
from settings import SNAKE_SIZE, GREEN

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)] # Initial snake position is 3 segment
        self.direction = (SNAKE_SIZE, 0) # Initial snake direction (moving right), SNAKE_SIZE on the x, 0 on the y axis
    
    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def change_direction(self, new_direction):
       # Calculate the opposite direction
        opposite_direction = (new_direction[0] * -1, new_direction[1] * -1)
        
        # Check if the new direction is not the opposite of the current direction
        if opposite_direction != self.direction:
            # Update the direction to the new direction
            self.direction = new_direction

    def grow(self):
        self.body.append(self.body[-1]) # Duplicate the last segment

    def draw(self, sceen):
        for segment in self.body:
            pygame.draw.rect(sceen, GREEN, (*segment, SNAKE_SIZE, SNAKE_SIZE))