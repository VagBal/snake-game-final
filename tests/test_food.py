import pytest
import pygame
from unittest.mock import MagicMock, patch
from src.food.food_module import Food
from settings import *

# Initialize Pygame
@pytest.fixture(scope="module", autouse=True)
def init_pygame():
    pygame.init()
    yield
    pygame.quit()

# Test class for Food
class TestFood:

    def test_food_initialization(self):
        # Arrange
        color = RED
        shape = "rectangle"
        
        # Act
        food = Food(color, shape)
        
        # Assert
        assert food.color == color
        assert food.shape == shape
        assert isinstance(food.position, tuple)
        assert len(food.position) == 2  # Position should be a tuple of (x, y)

    def test_random_position_within_bounds(self):
        # Arrange
        color = RED
        shape = "rectangle"
        
        # Act
        food = Food(color, shape)
        x, y = food.position
        
        # Assert
        assert 0 <= x < SCREEN_WIDTH
        assert 0 <= y < SCREEN_HEIGHT

    @patch('pygame.draw.rect')  # Mock the draw.rect method
    def test_food_draw_rectangle(self, mock_draw_rect):
        # Arrange
        color = RED
        shape = "rectangle"
        food = Food(color, shape)
        screen = pygame.Surface((800, 800))  # Create a real surface for the screen
        
        # Act
        food.draw(screen)  # Call the draw method with the real screen
        
        # Assert
        # Verify that the draw.rect method was called with the correct parameters
        mock_draw_rect.assert_called_once_with(screen, color, (*food.position, FOOD_SIZE, FOOD_SIZE))

    @patch('pygame.draw.circle')  # Mock the draw.circle method
    def test_food_draw_circle(self, mock_draw_circle):
        # Arrange
        color = ORANGE
        shape = "circle"
        food = Food(color, shape)
        screen = pygame.Surface((800, 800))  # Create a real surface for the screen
        
        # Act
        food.draw(screen)  # Call the draw method with the real screen
        
        # Assert
        # Verify that the draw.circle method was called with the correct parameters
        mock_draw_circle.assert_called_once()