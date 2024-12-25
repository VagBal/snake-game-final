import pytest
from src.game.game_manager_module import GameManager
from settings import States

# Test class for GameManager
class TestGameManager:

    def test_singleton_instance(self):
        # Act
        instance1 = GameManager()
        instance2 = GameManager()
        
        # Assert
        assert instance1 is instance2  # Both instances should be the same

    def test_initial_state(self):
        # Act
        manager = GameManager()
        
        # Assert
        assert manager.state == States.START  # Initial state should be START

    def test_change_state(self):
        # Arrange
        manager = GameManager()
        
        # Act
        manager.change_state(States.PLAYING)
        
        # Assert
        assert manager.state == States.PLAYING  # State should change to PLAYING

    def test_change_state_to_game_over(self):
        # Arrange
        manager = GameManager()
        
        # Act
        manager.change_state(States.GAME_OVER)
        
        # Assert
        assert manager.state == States.GAME_OVER  # State should change to GAME_OVER