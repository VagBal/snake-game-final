import pytest
import pygame
from src.food.food_module import Food
from settings import FOOD_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, RED

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

    def test_food_draw_rectangle(self):
        # Arrange
        color = RED
        shape = "rectangle"
        food = Food(color, shape)
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # Act
        food.draw(screen)
        
        # Assert
        # Since we cannot directly test the drawing, we will check if the method runs without errors
        assert True  # If no exception is raised, the test passes

    def test_food_draw_circle(self):
        # Arrange
        color = RED
        shape = "circle"
        food = Food(color, shape)
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # Act
        food.draw(screen)
        
        # Assert
        # Since we cannot directly test the drawing, we will check if the method runs without errors
        assert True  # If no exception is raised, the test passes