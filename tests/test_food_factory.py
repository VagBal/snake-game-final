import pytest
from src.food.food_factory_module import FoodFactory
from src.food.food_module import Food
from settings import RED, ORANGE

# Test class for FoodFactory
class TestFoodFactory:

    def test_create_food_rectangle(self):
        # Arrange
        color = RED
        shape = "rectangle"
        
        # Act
        food = FoodFactory.create_food(color, shape)
        
        # Assert
        assert isinstance(food, Food)
        assert food.color == color
        assert food.shape == shape

    def test_create_food_circle(self):
        # Arrange
        color = ORANGE
        shape = "circle"
        
        # Act
        food = FoodFactory.create_food(color, shape)
        
        # Assert
        assert isinstance(food, Food)
        assert food.color == color
        assert food.shape == shape

    def test_food_position_randomness(self):
        # Arrange
        color = RED
        shape = "rectangle"
        
        # Act
        food1 = FoodFactory.create_food(color, shape)
        food2 = FoodFactory.create_food(color, shape)
        
        # Assert
        assert food1.position != food2.position  # Check that positions are different