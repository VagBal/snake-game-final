import pytest
from src.game.score_module import Score

# Test class for Score
class TestScore:

    def test_initial_score(self):
        # Act
        score = Score()
        
        # Assert
        assert score.get_score() == 0  # Initial score should be 0

    def test_increase_score(self):
        # Arrange
        score = Score()
        
        # Act
        score.increase_score()
        
        # Assert
        assert score.get_score() == 1  # Score should increase to 1

    def test_increase_score_multiple_times(self):
        # Arrange
        score = Score()
        
        # Act
        score.increase_score()
        score.increase_score()
        
        # Assert
        assert score.get_score() == 2  # Score should increase to 2

    def test_observer_notification(self):
        # Arrange
        score = Score()
        observer_called = False
        
        class MockObserver:
            def update(self, new_score):
                nonlocal observer_called
                observer_called = True
                assert new_score >= 0 # Check initial score notification

        observer = MockObserver()
        score.add_observer(observer)
        
        # Act
        score.notify_observers()
        
        # Assert
        assert observer_called  # Observer should be notified

        # Act
        score.increase_score()
        observer_called = False  # Reset the flag
        
        # Act
        score.notify_observers()
        
        # Assert
        assert observer_called  # Observer should be notified again

    def test_remove_observer(self):
        # Arrange
        score = Score()
        observer_called = False
        
        class MockObserver:
            def update(self, new_score):
                nonlocal observer_called
                observer_called = True

        observer = MockObserver()
        score.add_observer(observer)
        score.remove_observer(observer)
        
        # Act
        score.increase_score()
        score.notify_observers()
        
        # Assert
        assert not observer_called  # Observer should not be notified after removal