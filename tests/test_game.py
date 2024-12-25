import pytest
import pygame
from src.game.game_module import Game
from src.snake.snake_module import Snake
from src.food.food_module import Food
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, RED, SNAKE_SIZE

# Initialize Pygame
@pytest.fixture(scope="module", autouse=True)
def init_pygame():
    pygame.init()
    yield
    pygame.quit()

# Test class for Game
class TestGame:

    def test_initialization(self):
        # Act
        game = Game()
        
        # Assert
        assert isinstance(game.snake, Snake)  # Snake should be initialized
        assert isinstance(game.food, Food)  # Food should be initialized
        assert game.score.get_score() == 0  # Initial score should be 0

    def test_food_creation(self):
        # Act
        game = Game()
        
        # Assert
        assert game.food.position is not None  # Food should have a position
        assert 0 <= game.food.position[0] < SCREEN_WIDTH  # Food x position should be within bounds
        assert 0 <= game.food.position[1] < SCREEN_HEIGHT  # Food y position should be within bounds

    def test_snake_growth_on_food_collision(self):
        # Arrange
        game = Game()
        initial_length = len(game.snake.body)
        game.food.position = game.snake.body[0]  # Set food position to snake's head to simulate collision
        
        # Act
        game.snake.move()  # Move the snake to "eat" the food
        game.food.draw(game.screen)  # Draw food (not necessary for logic, but for completeness)
        game.snake.grow()

        # Assert
        assert len(game.snake.body) == initial_length + 1  # Snake should grow by 1

    def test_collision_with_wall(self):
        # Arrange
        game = Game()
        game.snake.body[0] = (SCREEN_WIDTH - SNAKE_SIZE, SCREEN_HEIGHT - SNAKE_SIZE)  # Position snake at bottom-right corner
        game.snake.direction = (SNAKE_SIZE, 0)  # Set direction to right
        
        # Act
        game.snake.move()  # Move the snake, which should cause a collision
        
        # Assert
        assert game.check_collisions()  # Collision should be detected

    def test_collision_with_self(self):
        # Arrange
        game = Game()
        # Set up a longer snake body to ensure it can collide with itself
        game.snake.body = [(220, 100), (200, 100), (180, 100), (160, 100), (140, 100), (120, 100), (100, 100), (80, 100), (60, 100), (40, 100), (20, 100)]  # Longer snake
        game.snake.direction = (SNAKE_SIZE, 0)  # Set direction to right
        
        # Act
        game.snake.move()  # Move the snake to the right
        game.snake.change_direction((0, -SNAKE_SIZE))  # Attempt to change direction to up
        game.snake.move()  # Move again to collide with itself
        game.snake.change_direction((-SNAKE_SIZE, 0))  # Attempt to change direction to left
        game.snake.move()
        game.snake.change_direction((0, SNAKE_SIZE))  # Attempt to change direction to down
        game.snake.move()

        # Assert
        assert game.check_collisions()  # Collision with itself should be detected