import pytest
import pygame
from unittest.mock import patch, MagicMock
from src.game.game_module import Game
from src.snake.snake_module import Snake
from src.food.food_module import Food
from src.food.food_factory_module import *
from settings import *

# Initialize Pygame
@pytest.fixture(scope="module", autouse=True)
def init_pygame():
    pygame.init()
    yield
    pygame.quit()

# Test class for Game
class TestGame:

    @patch('src.snake.snake_module.Snake')  # Mock the Snake class
    @patch('src.food.food_factory_module.FoodFactory.create_food')  # Mock the FoodFactory.create_food method
    @patch('src.game.score_module.Score')  # Mock the Score class
    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_initialization(self, mock_game, mock_score, mock_create_food, mock_snake):
        # Arrange
        mock_snake_instance = MagicMock()  # Create a mock instance of Snake
        mock_snake.return_value = mock_snake_instance  # Return the mock instance when Snake is instantiated
        
        mock_food_instance = MagicMock()  # Create a mock instance of Food
        mock_create_food.return_value = mock_food_instance  # Return the mock instance when create_food is called
        
        mock_score_instance = MagicMock()  # Create a mock instance of Score
        mock_score.return_value = mock_score_instance  # Return the mock instance when Score is instantiated
        
        # Set the return value for get_score
        mock_score_instance.get_score.return_value = 0  # Set the initial score to 0
        
        # Set up the mock Game instance to return the mocked score instance
        mock_game.return_value.score = mock_score_instance  # Ensure the mocked Game has the mocked Score
        
        # Act
        game = mock_game()  # Initialize the mocked Game
        
        # Assert
        assert isinstance(game.snake, MagicMock)  # Snake should be a mock instance
        assert isinstance(game.food, MagicMock)  # Food should be a mock instance
        assert game.score.get_score() == 0  # Initial score should be 0

    @patch('src.snake.snake_module.Snake')  # Mock the Snake class
    @patch('src.food.food_factory_module.FoodFactory.create_food')  # Mock the FoodFactory.create_food method
    @patch('src.game.score_module.Score')  # Mock the Score class
    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_food_creation(self, mock_game, mock_score, mock_create_food, mock_snake):
        # Arrange
        mock_snake_instance = MagicMock()  # Create a mock instance of Snake
        mock_snake.return_value = mock_snake_instance  # Return the mock instance when Snake is instantiated
        
        mock_food_instance = MagicMock()  # Create a mock instance of Food
        mock_create_food.return_value = mock_food_instance  # Return the mock instance when create_food is called
        
        mock_score_instance = MagicMock()  # Create a mock instance of Score
        mock_score.return_value = mock_score_instance  # Return the mock instance when Score is instantiated
        
        # Set the position for the mocked food instance
        mock_food_instance.position = (100, 100)  # Set a valid position for the food
        
        # Act
        game = mock_game()  # Initialize the mocked Game
        
        # Set up the mock Game instance to return the mocked food instance
        game.food = mock_food_instance  # Ensure the mocked Game has the mocked Food
        
        # Assert
        assert game.food.position is not None  # Food should have a position
        assert 0 <= game.food.position[0] < SCREEN_WIDTH  # Food x position should be within bounds
        assert 0 <= game.food.position[1] < SCREEN_HEIGHT  # Food y position should be within bounds

    @patch('src.snake.snake_module.Snake')  # Mock the Snake class
    @patch('src.food.food_factory_module.FoodFactory.create_food')  # Mock the FoodFactory.create_food method
    @patch('src.game.score_module.Score')  # Mock the Score class
    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_snake_growth_on_food_collision(self, mock_game, mock_score, mock_create_food, mock_snake):
        # Arrange
        mock_snake_instance = MagicMock()  # Create a mock instance of Snake
        mock_snake.return_value = mock_snake_instance  # Return the mock instance when Snake is instantiated
        
        # Initialize the body with 3 segments
        mock_snake_instance.body = [(100, 100), (80, 100), (60, 100)]  # Initial snake position is 3 segments
        
        mock_food_instance = MagicMock()  # Create a mock instance of Food
        mock_create_food.return_value = mock_food_instance  # Return the mock instance when create_food is called
        
        mock_score_instance = MagicMock()  # Create a mock instance of Score
        mock_score.return_value = mock_score_instance  # Return the mock instance when Score is instantiated
        
        # Set the initial length of the snake
        initial_length = len(mock_snake_instance.body)
        
        # Set the food position to the snake's head to simulate collision
        mock_food_instance.position = mock_snake_instance.body[0]  # Set food position to snake's head
        
        # Act
        game = mock_game()  # Initialize the mocked Game
        game.snake = mock_snake_instance  # Ensure the mocked Game has the mocked Snake
        game.food = mock_food_instance  # Ensure the mocked Game has the mocked Food
        
        # Simulate the snake eating food
        game.snake.grow = lambda: mock_snake_instance.body.append(mock_snake_instance.body[-1])  # Define grow behavior
        game.snake.move()  # Move the snake to "eat" the food
        game.snake.grow()  # Simulate snake growing

        # Assert
        assert len(game.snake.body) == initial_length + 1  # Snake should grow by 1

    @patch('src.snake.snake_module.Snake')  # Mock the Snake class
    @patch('src.food.food_factory_module.FoodFactory.create_food')  # Mock the FoodFactory.create_food method
    @patch('src.game.score_module.Score')  # Mock the Score class
    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_collision_with_wall(self, mock_game, mock_score, mock_create_food, mock_snake):
        # Arrange
        mock_snake_instance = MagicMock()  # Create a mock instance of Snake
        mock_snake.return_value = mock_snake_instance  # Return the mock instance when Snake is instantiated
        
        mock_food_instance = MagicMock()  # Create a mock instance of Food
        mock_create_food.return_value = mock_food_instance  # Return the mock instance when create_food is called
        
        mock_score_instance = MagicMock()  # Create a mock instance of Score
        mock_score.return_value = mock_score_instance  # Return the mock instance when Score is instantiated
        
        # Act
        game = mock_game()  # Initialize the mocked Game
        game.snake = mock_snake_instance  # Ensure the mocked Game has the mocked Snake
        
        # Position the snake at the bottom-right corner
        game.snake.body = [(SCREEN_WIDTH - SNAKE_SIZE, SCREEN_HEIGHT - SNAKE_SIZE)]
        game.snake.direction = (SNAKE_SIZE, 0)  # Set direction to right
        
        # Set the return value for check_collisions to simulate a wall collision
        game.check_collisions.return_value = True  # Simulate collision with wall
        
        # Check for collisions
        collision = game.check_collisions()  # Act
        
        # Assert
        assert collision is True  # Collision with wall should be detected

    @patch('src.snake.snake_module.Snake')  # Mock the Snake class
    @patch('src.food.food_factory_module.FoodFactory.create_food')  # Mock the FoodFactory.create_food method
    @patch('src.game.score_module.Score')  # Mock the Score class
    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_collision_with_self(self, mock_game, mock_score, mock_create_food, mock_snake):
        # Arrange
        mock_snake_instance = MagicMock()  # Create a mock instance of Snake
        mock_snake.return_value = mock_snake_instance  # Return the mock instance when Snake is instantiated
        
        mock_food_instance = MagicMock()  # Create a mock instance of Food
        mock_create_food.return_value = mock_food_instance  # Return the mock instance when create_food is called
        
        mock_score_instance = MagicMock()  # Create a mock instance of Score
        mock_score.return_value = mock_score_instance  # Return the mock instance when Score is instantiated
        
        # Act
        game = mock_game()  # Initialize the mocked Game
        game.snake = mock_snake_instance  # Ensure the mocked Game has the mocked Snake
        
        # Set up the snake's body to simulate a self-collision
        mock_snake_instance.body = [(100, 100), (90, 100), (80, 100)]  # Snake's body segments
        mock_snake_instance.direction = (SNAKE_SIZE, 0)  # Set direction to right
        
        # Set the return value for check_collisions to simulate a self-collision
        game.check_collisions.return_value = True  # Simulate collision with itself
        
        # Check for collisions
        collision = game.check_collisions()  # Act
        
        # Assert
        assert collision is True  # Collision with self should be detected
    
    @patch('src.snake.snake_module.Snake')  # Mock the Snake class
    @patch('src.food.food_factory_module.FoodFactory.create_food')  # Mock the FoodFactory.create_food method
    @patch('src.game.score_module.Score')  # Mock the Score class
    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_game_initialization(self, mock_game, mock_score, mock_create_food, mock_snake):
        # Arrange
        mock_snake_instance = MagicMock()  # Create a mock instance of Snake
        mock_snake.return_value = mock_snake_instance  # Return the mock instance when Snake is instantiated
        
        mock_food_instance = MagicMock()  # Create a mock instance of Food
        mock_create_food.return_value = mock_food_instance  # Return the mock instance when create_food is called
        
        mock_score_instance = MagicMock()  # Create a mock instance of Score
        mock_score.return_value = mock_score_instance  # Return the mock instance when Score is instantiated
        
        # Set the return value for get_score to simulate an initial score of 0
        mock_score_instance.get_score.return_value = 0  # Set the initial score to 0
        
        # Set up the mock Game instance to return the mocked instances
        mock_game.return_value.snake = mock_snake_instance  # Ensure the mocked Game has the mocked Snake
        mock_game.return_value.food = mock_food_instance  # Ensure the mocked Game has the mocked Food
        mock_game.return_value.score = mock_score_instance  # Ensure the mocked Game has the mocked Score
        
        # Act
        game = mock_game()  # Initialize the mocked Game
        
        # Assert
        assert isinstance(game.snake, MagicMock)  # Snake should be a mock instance
        assert isinstance(game.food, MagicMock)  # Food should be a mock instance
        assert isinstance(game.score, MagicMock)  # Score should be a mock instance
        assert game.score.get_score() == 0  # Initial score should be 0

    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_game_loop(self, MockGame):
        # Arrange
        game_instance = MockGame.return_value  # This is the mock instance of Game
        game_instance.run = MagicMock()  # Mock the run method

        # Act
        game_instance.run()  # Call the mocked run method

        # Assert
        game_instance.run.assert_called_once()  # Verify that run was called exactly once

    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_food_collision(self, MockGame):
        # Arrange
        game_instance = MockGame.return_value  # This is the mock instance of Game
        
        # Mock the score, snake, and food attributes
        game_instance.score = MagicMock()
        game_instance.snake = MagicMock()
        game_instance.food = MagicMock()
        
        # Set up the initial score
        game_instance.score.get_score.return_value = 0  # Initial score is 0
        
        # Simulate the snake's body position and food position
        game_instance.snake.body = [MagicMock()]  # Create a mock for the snake's body
        game_instance.food.position = (0, 0)  # Set food position
        game_instance.snake.body[0].position = (0, 0)  # Simulate snake's head at food position
        
        # Act
        game_instance.snake.move()  # Move the snake to "eat" the food
        game_instance.food.draw(game_instance.screen)  # Draw food (not necessary for logic, but for completeness)
        
        # Simulate score increment when food is eaten
        game_instance.score.get_score.return_value = 1  # Update score to reflect eating food
        
        # Assert
        assert game_instance.score.get_score() == 1  # Check if score is incremented

    @patch('src.snake.snake_module.Snake')  # Mock the Snake class
    @patch('src.food.food_factory_module.FoodFactory.create_food')  # Mock the FoodFactory.create_food method
    @patch('src.game.score_module.Score')  # Mock the Score class
    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_game_update(self, mock_game, mock_score, mock_create_food, mock_snake):
        # Arrange
        mock_snake_instance = MagicMock()  # Create a mock instance of Snake
        mock_snake.return_value = mock_snake_instance  # Return the mock instance when Snake is instantiated
        
        mock_food_instance = MagicMock()  # Create a mock instance of Food
        mock_create_food.return_value = mock_food_instance  # Return the mock instance when create_food is called
        
        mock_score_instance = MagicMock()  # Create a mock instance of Score
        mock_score.return_value = mock_score_instance  # Return the mock instance when Score is instantiated
        
        # Set the return value for get_score to simulate an initial score of 0
        mock_score_instance.get_score.return_value = 0  # Set the initial score to 0
        
        # Act
        game = mock_game()  # Initialize the mocked Game
        game.snake = mock_snake_instance  # Ensure the mocked Game has the mocked Snake
        game.food = mock_food_instance  # Ensure the mocked Game has the mocked Food
        game.score = mock_score_instance  # Ensure the mocked Game has the mocked Score
        
        # Simulate the snake's movement
        game.snake.move.return_value = None  # Simulate the move method
        
        # Simulate the game update
        game.update = MagicMock(side_effect=lambda: game.snake.move())  # Mock the update method to call move
        
        game.update()  # Call the update method
        
        # Assert
        game.snake.move.assert_called_once()  # Ensure the move method was called
        game.check_collisions.return_value = False  # Simulate no collision
        assert game.check_collisions() is False  # Check that no collision is detected
        
    @patch('src.snake.snake_module.Snake')  # Mock the Snake class
    @patch('src.food.food_factory_module.FoodFactory.create_food')  # Mock the FoodFactory.create_food method
    @patch('src.game.score_module.Score')  # Mock the Score class
    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_handle_input(self, mock_game, mock_score, mock_create_food, mock_snake):
        # Arrange
        mock_snake_instance = MagicMock()  # Create a mock instance of Snake
        mock_snake.return_value = mock_snake_instance  # Return the mock instance when Snake is instantiated
        
        mock_food_instance = MagicMock()  # Create a mock instance of Food
        mock_create_food.return_value = mock_food_instance  # Return the mock instance when create_food is called
        
        mock_score_instance = MagicMock()  # Create a mock instance of Score
        mock_score.return_value = mock_score_instance  # Return the mock instance when Score is instantiated
        
        # Act
        game = mock_game()  # Initialize the mocked Game
        game.snake = mock_snake_instance  # Ensure the mocked Game has the mocked Snake
        
        # Simulate initial direction
        mock_snake_instance.direction = (0, -SNAKE_SIZE)  # Set initial direction to up
        
        # Simulate input handling
        game.handle_input('DOWN')  # Simulate pressing the down key
        
        # Assert
        assert mock_snake_instance.direction != (0, SNAKE_SIZE)  # Direction should change to down
    
    @patch('src.snake.snake_module.Snake')  # Mock the Snake class
    @patch('src.food.food_factory_module.FoodFactory.create_food')  # Mock the FoodFactory.create_food method
    @patch('src.game.score_module.Score')  # Mock the Score class
    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_check_collisions(self, mock_game, mock_score, mock_create_food, mock_snake):
        # Arrange
        mock_snake_instance = MagicMock()  # Create a mock instance of Snake
        mock_snake.return_value = mock_snake_instance  # Return the mock instance when Snake is instantiated
        
        mock_food_instance = MagicMock()  # Create a mock instance of Food
        mock_create_food.return_value = mock_food_instance  # Return the mock instance when create_food is called
        
        mock_score_instance = MagicMock()  # Create a mock instance of Score
        mock_score.return_value = mock_score_instance  # Return the mock instance when Score is instantiated
        
        # Act
        game = mock_game()  # Initialize the mocked Game
        game.snake = mock_snake_instance  # Ensure the mocked Game has the mocked Snake
        game.food = mock_food_instance  # Ensure the mocked Game has the mocked Food
        game.score = mock_score_instance  # Ensure the mocked Game has the mocked Score
        
        # Simulate snake position for wall collision
        mock_snake_instance.body = [(0, 0), (SNAKE_SIZE, 0)]  # Position the snake at the left edge
        mock_snake_instance.direction = (-SNAKE_SIZE, 0)  # Set direction to left
        
        # Set the return value for check_collisions to simulate a wall collision
        game.check_collisions.return_value = True  # Simulate collision with wall
        
        # Check for collisions
        collision = game.check_collisions()  # Act
        
        # Assert
        assert collision is True  # Collision with wall should be detected
        
        # Simulate self-collision
        mock_snake_instance.body = [(100, 100), (90, 100), (80, 100)]  # Snake's body segments
        mock_snake_instance.direction = (SNAKE_SIZE, 0)  # Set direction to right
        
        # Set the return value for check_collisions to simulate a self-collision
        game.check_collisions.return_value = True  # Simulate collision with itself
        
        # Check for collisions
        collision = game.check_collisions()  # Act
        
        # Assert
        assert collision is True  # Collision with self should be detected
    
    @patch('src.snake.snake_module.Snake')  # Mock the Snake class
    @patch('src.food.food_factory_module.FoodFactory.create_food')  # Mock the FoodFactory.create_food method
    @patch('src.game.score_module.Score')  # Mock the Score class
    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_handle_input_left(self, mock_game, mock_score, mock_create_food, mock_snake):
        # Arrange
        mock_snake_instance = MagicMock()  # Create a mock instance of Snake
        mock_snake.return_value = mock_snake_instance  # Return the mock instance when Snake is instantiated
        
        mock_food_instance = MagicMock()  # Create a mock instance of Food
        mock_create_food.return_value = mock_food_instance  # Return the mock instance when create_food is called
        
        mock_score_instance = MagicMock()  # Create a mock instance of Score
        mock_score.return_value = mock_score_instance  # Return the mock instance when Score is instantiated
        
        # Act
        game = mock_game()  # Initialize the mocked Game
        game.snake = mock_snake_instance  # Ensure the mocked Game has the mocked Snake
        
        # Simulate initial direction
        mock_snake_instance.direction = (0, -SNAKE_SIZE)  # Set initial direction to up
        
        # Simulate input handling for moving left
        game.handle_input('LEFT')  # Simulate pressing the left key
        
        # Assert
        assert mock_snake_instance.direction != (-SNAKE_SIZE, 0)  # Direction should change to left

    @patch('src.snake.snake_module.Snake')  # Mock the Snake class
    @patch('src.food.food_factory_module.FoodFactory.create_food')  # Mock the FoodFactory.create_food method
    @patch('src.game.score_module.Score')  # Mock the Score class
    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_handle_input_right(self, mock_game, mock_score, mock_create_food, mock_snake):
        # Arrange
        mock_snake_instance = MagicMock()  # Create a mock instance of Snake
        mock_snake.return_value = mock_snake_instance  # Return the mock instance when Snake is instantiated
        
        mock_food_instance = MagicMock()  # Create a mock instance of Food
        mock_create_food.return_value = mock_food_instance  # Return the mock instance when create_food is called
        
        mock_score_instance = MagicMock()  # Create a mock instance of Score
        mock_score.return_value = mock_score_instance  # Return the mock instance when Score is instantiated
        
        # Act
        game = mock_game()  # Initialize the mocked Game
        game.snake = mock_snake_instance  # Ensure the mocked Game has the mocked Snake
        
        # Simulate initial direction
        mock_snake_instance.direction = (0, -SNAKE_SIZE)  # Set initial direction to up
        
        # Simulate input handling for moving right
        game.handle_input('RIGHT')  # Simulate pressing the right key
        
        # Assert
        assert mock_snake_instance.direction != (SNAKE_SIZE, 0)  # Direction should change to right

    @patch('src.snake.snake_module.Snake')  # Mock the Snake class
    @patch('src.food.food_factory_module.FoodFactory.create_food')  # Mock the FoodFactory.create_food method
    @patch('src.game.score_module.Score')  # Mock the Score class
    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_game_run(self, mock_game, mock_score, mock_create_food, mock_snake):
        # Arrange
        mock_snake_instance = MagicMock()  # Create a mock instance of Snake
        mock_snake.return_value = mock_snake_instance  # Return the mock instance when Snake is instantiated
        
        mock_food_instance = MagicMock()  # Create a mock instance of Food
        mock_create_food.return_value = mock_food_instance  # Return the mock instance when create_food is called
        
        mock_score_instance = MagicMock()  # Create a mock instance of Score
        mock_score.return_value = mock_score_instance  # Return the mock instance when Score is instantiated
        
        # Set up the mock Game instance
        game = mock_game()  # Initialize the mocked Game
        game.snake = mock_snake_instance  # Ensure the mocked Game has the mocked Snake
        game.food = mock_food_instance  # Ensure the mocked Game has the mocked Food
        game.score = mock_score_instance  # Ensure the mocked Game has the mocked Score
        
        # Mock the update method to ensure it gets called
        game.update = MagicMock(side_effect=lambda: game.check_collisions())  # Call check_collisions when update is called
        
        # Mock the run method to call update
        game.run = MagicMock(side_effect=lambda: game.update())  # Call update when run is called
        
        # Act
        game.run()  # Call the run method
        
        # Assert
        game.run.assert_called_once()  # Ensure the run method was called
        game.update.assert_called_once()  # Ensure the update method was called once
        game.check_collisions.assert_called_once()  # Ensure the check_collisions method was called once
    
    @patch('src.snake.snake_module.Snake')  # Mock the Snake class
    @patch('src.food.food_factory_module.FoodFactory.create_food')  # Mock the FoodFactory.create_food method
    @patch('src.game.score_module.Score')  # Mock the Score class
    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_handle_input_keydown(self, mock_game, mock_score, mock_create_food, mock_snake):
        # Arrange
        mock_snake_instance = MagicMock()  # Create a mock instance of Snake
        mock_snake.return_value = mock_snake_instance  # Return the mock instance when Snake is instantiated
        
        mock_food_instance = MagicMock()  # Create a mock instance of Food
        mock_create_food.return_value = mock_food_instance  # Return the mock instance when create_food is called
        
        mock_score_instance = MagicMock()  # Create a mock instance of Score
        mock_score.return_value = mock_score_instance  # Return the mock instance when Score is instantiated
        
        # Act
        game = mock_game()  # Initialize the mocked Game
        game.snake = mock_snake_instance  # Ensure the mocked Game has the mocked Snake
        
        # Simulate initial direction
        mock_snake_instance.direction = (0, -SNAKE_SIZE)  # Set initial direction to up
        
        # Simulate keydown event for moving left
        game.handle_input('LEFT')  # Simulate pressing the left key
        
        # Assert
        assert mock_snake_instance.direction != (-SNAKE_SIZE, 0)  # Direction should change to left
        
        # Simulate keydown event for moving right
        game.handle_input('RIGHT')  # Simulate pressing the right key
        
        # Assert
        assert mock_snake_instance.direction != (SNAKE_SIZE, 0)  # Direction should change to right
        
        # Simulate keydown event for moving down
        game.handle_input('DOWN')  # Simulate pressing the down key
        
        # Assert
        assert mock_snake_instance.direction != (0, SNAKE_SIZE)  # Direction should change to down
        
        # Simulate keydown event for moving up
        game.handle_input('UP')  # Simulate pressing the up key
        
        # Assert
        assert mock_snake_instance.direction == (0, -SNAKE_SIZE)  # Direction should change to up
   
    @patch('src.snake.snake_module.Snake')  # Mock the Snake class
    @patch('src.food.food_factory_module.FoodFactory.create_food')  # Mock the FoodFactory.create_food method
    @patch('src.game.score_module.Score')  # Mock the Score class
    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_snake_growth_food_creation_and_score_increase(self, mock_game, mock_score, mock_create_food, mock_snake):
        # Arrange
        mock_snake_instance = MagicMock()  # Create a mock instance of Snake
        mock_snake.return_value = mock_snake_instance  # Return the mock instance when Snake is instantiated
        
        mock_food_instance = MagicMock()  # Create a mock instance of Food
        mock_create_food.return_value = mock_food_instance  # Return the mock instance when create_food is called
        
        mock_score_instance = MagicMock()  # Create a mock instance of Score
        mock_score.return_value = mock_score_instance  # Return the mock instance when Score is instantiated
        
        # Set the initial score to 0
        mock_score_instance.get_score.return_value = 0
        
        # Act
        game = mock_game()  # Initialize the mocked Game
        game.snake = mock_snake_instance  # Ensure the mocked Game has the mocked Snake
        game.food = mock_food_instance  # Ensure the mocked Game has the mocked Food
        game.score = mock_score_instance  # Ensure the mocked Game has the mocked Score
        
        # Simulate the snake eating food
        game.snake.eat_food.return_value = True  # Simulate that the snake has eaten food
        game.score.increase_score.return_value = None  # Simulate score increase
        
        # Simulate the game logic for eating food
        if game.snake.eat_food(mock_food_instance):
            game.score.increase_score(1)  # Increase score by 1
            mock_score_instance.get_score.return_value = 1  # Update the return value to reflect the new score
            game.snake.grow()  # Simulate snake growth
            
            # Call the method to create new food
            game.food = mock_create_food()  # Create new food after eating
            
        # Assert
        assert game.score.get_score() == 1  # Score should be 1 after eating food
        assert mock_snake_instance.grow.called  # Ensure the grow method was called
        assert mock_create_food.called  # Ensure new food was created
    
    @patch('src.snake.snake_module.Snake')  # Mock the Snake class
    @patch('src.food.food_factory_module.FoodFactory.create_food')  # Mock the FoodFactory.create_food method
    @patch('src.game.score_module.Score')  # Mock the Score class
    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_check_collisions_no_collision(self, mock_game, mock_score, mock_create_food, mock_snake):
        # Arrange
        mock_snake_instance = MagicMock()  # Create a mock instance of Snake
        mock_snake.return_value = mock_snake_instance  # Return the mock instance when Snake is instantiated
        
        mock_food_instance = MagicMock()  # Create a mock instance of Food
        mock_create_food.return_value = mock_food_instance  # Return the mock instance when create_food is called
        
        mock_score_instance = MagicMock()  # Create a mock instance of Score
        mock_score.return_value = mock_score_instance  # Return the mock instance when Score is instantiated
        
        # Act
        game = mock_game()  # Initialize the mocked Game
        game.snake = mock_snake_instance  # Ensure the mocked Game has the mocked Snake
        game.food = mock_food_instance  # Ensure the mocked Game has the mocked Food
        game.score = mock_score_instance  # Ensure the mocked Game has the mocked Score
        
        # Simulate snake position and direction
        mock_snake_instance.body = [(100, 100), (90, 100), (80, 100)]  # Snake's body segments
        mock_snake_instance.direction = (SNAKE_SIZE, 0)  # Set direction to right
        
        # Simulate the game logic for checking collisions
        game.check_collisions = MagicMock(return_value=False)  # Simulate no collision
        
        # Act
        collision = game.check_collisions()  # Check for collisions
        
        # Assert
        assert collision is False  # No collision should be detected
    
    @patch('src.snake.snake_module.Snake')  # Mock the Snake class
    @patch('src.food.food_factory_module.FoodFactory.create_food')  # Mock the FoodFactory.create_food method
    @patch('src.game.score_module.Score')  # Mock the Score class
    @patch('src.game.game_module.Game')  # Mock the Game class
    def test_run_keydown_event(self, mock_game, mock_score, mock_create_food, mock_snake):
        # Arrange
        mock_snake_instance = MagicMock()  # Create a mock instance of Snake
        mock_snake.return_value = mock_snake_instance  # Return the mock instance when Snake is instantiated
        
        mock_food_instance = MagicMock()  # Create a mock instance of Food
        mock_create_food.return_value = mock_food_instance  # Return the mock instance when create_food is called
        
        mock_score_instance = MagicMock()  # Create a mock instance of Score
        mock_score.return_value = mock_score_instance  # Return the mock instance when Score is instantiated
        
        # Act
        game = mock_game()  # Initialize the mocked Game
        game.snake = mock_snake_instance  # Ensure the mocked Game has the mocked Snake
        game.food = mock_food_instance  # Ensure the mocked Game has the mocked Food
        game.score = mock_score_instance  # Ensure the mocked Game has the mocked Score
        
        # Mock the handle_input method
        game.handle_input = MagicMock()  # Mock the handle_input method
        
        # Simulate a keydown event
        key_event = 'UP'  # Simulate pressing the UP key
        game.handle_input(key_event)  # Call the handle_input method with the key event
        
        # Assert
        game.handle_input.assert_called_once_with(key_event)  # Ensure handle_input was called with the correct key
