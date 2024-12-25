import pytest
from src.game.game_state_module import GameState
from settings import States

# Test class for GameState
class TestGameState:

    def test_initial_state(self):
        # Act
        game_state = GameState()
        
        # Assert
        assert game_state.state == States.START  # Initial state should be START

    def test_change_state(self):
        # Arrange
        game_state = GameState()
        
        # Act
        game_state.change_state(States.PLAYING)
        
        # Assert
        assert game_state.state == States.PLAYING  # State should change to PLAYING

    def test_change_state_to_game_over(self):
        # Arrange
        game_state = GameState()
        
        # Act
        game_state.change_state(States.GAME_OVER)
        
        # Assert
        assert game_state.state == States.GAME_OVER  # State should change to GAME_OVER

    def test_change_state_multiple_times(self):
        # Arrange
        game_state = GameState()
        
        # Act
        game_state.change_state(States.PLAYING)
        game_state.change_state(States.GAME_OVER)
        
        # Assert
        assert game_state.state == States.GAME_OVER  # State should be GAME_OVER after multiple changes