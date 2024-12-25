import pytest
import pygame
from src.snake.snake_module import Snake
from unittest.mock import patch, MagicMock
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

    @patch('pygame.draw')  # Mock the pygame.draw module
    def test_draw(self, mock_draw):
        # Arrange
        mock_surface = MagicMock()  # Create a mock surface to draw on
        snake = Snake()  # Create an instance of the Snake class
        
        # Set the initial position of the snake
        snake.body = [(100, 100), (90, 100), (80, 100)]  # Example body segments
        
        # Act
        snake.draw(mock_surface)  # Call the draw method with the mock surface
        
        # Assert
        # Check that the draw.rect method was called for each segment of the snake
        for segment in snake.body:
            mock_draw.rect.assert_any_call(mock_surface, (0, 255, 0), (*segment, SNAKE_SIZE, SNAKE_SIZE))