import pytest
from src.snake.snake_module import Snake
from src.game.command_module import MoveUp, MoveDown, MoveLeft, MoveRight, Command
from settings import SNAKE_SIZE

# Test class for Command Module
class TestCommandModule:

    def test_move_up(self):
        # Arrange
        snake = Snake()
        command = MoveUp()
        
        # Act
        command.execute(snake)
        
        # Assert
        assert snake.direction == (0, -SNAKE_SIZE)  # Direction should be up
        snake.move()  # Move the snake
        assert snake.body[0] == (100, 80)  # New head position after moving up
    
    def test_move_left(self):
        # Arrange
        snake = Snake()
        command = MoveLeft()
        
        # Act
        command.execute(snake)
        
        # Assert
        # THE INITIAL STATE IS MOVING RIGHT ITS PREVENTED TO OVE LEFT
        assert snake.direction != (-SNAKE_SIZE, 0)  # Direction should be left
        snake.move()  # Move the snake
        assert snake.body[0] == (120, 100)  # New head position after moving left

    def test_move_down(self):
        # Arrange
        snake = Snake()
        command = MoveDown()
        
        # Act
        command.execute(snake)
        
        # Assert
        assert snake.direction == (0, SNAKE_SIZE)  # Direction should be down
        snake.move()  # Move the snake
        assert snake.body[0] == (100, 120)  # New head position after moving down

    def test_move_right(self):
        # Arrange
        snake = Snake()
        command = MoveRight()
        
        # Act
        command.execute(snake)
        
        # Assert
        assert snake.direction == (SNAKE_SIZE, 0)  # Direction should be right
        snake.move()  # Move the snake
        assert snake.body[0] == (120, 100)  # New head position after moving right
    
    def test_command_execute(self):
        # Arrange
        snake = Snake()
        command = MoveUp()
        
        # Act
        command.execute(snake)
        
        # Assert
        assert snake.direction == (0, -SNAKE_SIZE)  # Direction should be up
    
    def test_command_execute(self):
        # Arrange
        command = Command()
        
        # Act & Assert
        try:
            command.execute()  # Should not raise an error
            assert True
        except Exception:
            assert False
