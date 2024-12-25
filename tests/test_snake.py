import pytest
import pygame
from src.snake.snake_module import Snake
from settings import *

# Test class for Snake
class TestSnake:

    def test_initialization(self):
        # Act
        snake = Snake()
        
        # Assert
        assert len(snake.body) == 3  # Initial length of the snake
        assert snake.body == [(100, 100), (80, 100), (60, 100)]  # Initial position
        assert snake.direction == (SNAKE_SIZE, 0)  # Initial direction (moving right)

    def test_move(self):
        # Arrange
        snake = Snake()
        
        # Act
        snake.move()
        
        # Assert
        assert snake.body[0] == (120, 100)  # New head position after moving right
        assert len(snake.body) == 3  # Length should remain the same after moving

    def test_change_direction(self):
        # Arrange
        snake = Snake()
        
        # Act
        snake.change_direction((0, -SNAKE_SIZE))  # Change direction to up
        snake.move()  # Move the snake
        
        # Assert
        assert snake.body[0] == (100, 80)  # New head position after moving up
        assert snake.direction == (0, -SNAKE_SIZE)  # Direction should be updated

    def test_change_direction_opposite(self):
        # Arrange
        snake = Snake()
        
        # Act
        snake.change_direction((0, -SNAKE_SIZE))  # Change direction to up
        snake.change_direction((0, SNAKE_SIZE))  # Attempt to change direction to down (opposite)
        
        # Assert
        assert snake.direction == (0, -SNAKE_SIZE)  # Direction should not change to opposite

    def test_grow(self):
        # Arrange
        snake = Snake()
        
        # Act
        snake.grow()  # Grow the snake
        
        # Assert
        assert len(snake.body) == 4  # Length should increase by 1
        assert snake.body[-1] == (60, 100)  # Last segment should be the same as the previous last segment

    def test_draw(self):
        # Arrange
        snake = Snake()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Placeholder, as we cannot test drawing directly
        
        # Act
        # Since we cannot directly test the drawing, we will check if the method runs without errors
        try:
            snake.draw(screen)  # This should run without errors
            assert True  # If no exception is raised, the test passes
        except Exception:
            assert False  # If an exception is raised, the test fails