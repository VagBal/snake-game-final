import pytest
import pygame
from src.main import Game
from unittest.mock import patch, MagicMock
from src.main import main

@pytest.fixture(scope="module", autouse=True)
def init_pygame():
    pygame.init()
    yield
    pygame.quit()

def test_main():
    # Arrange
    with patch('src.main.main') as mock_main:
        mock_game_instance = MagicMock()  # Create a mock instance of Game
        mock_main.return_value = None  # Prevent the actual main function from running
        
        # Act
        mock_main()  # Call the mocked main function
        
        # Assert
        mock_main.assert_called_once()  # Ensure the main function was called once

def test_main_game_execution():
    # Arrange
    with patch('src.main.Game') as MockGame:
        game_instance = MockGame.return_value  # This is the mock instance of Game
        game_instance.run = patch('src.main.Game.run').start()  # Mock the run method

        # Act
        main()  # This will trigger the Game initialization and run

        # Assert
        MockGame.assert_called_once()  # Ensure the Game class was instantiated
        game_instance.run.assert_called_once()  # Ensure the run method was called

def test_main_function():
    # Arrange
    with patch('src.main.Game') as MockGame:
        game_instance = MockGame.return_value  # This is the mock instance of Game
        game_instance.run = MagicMock()  # Mock the run method

        # Act
        main()  # Call the main function

        # Assert
        MockGame.assert_called_once()  # Ensure the Game class was instantiated
        game_instance.run.assert_called_once()  # Ensure the run method was called