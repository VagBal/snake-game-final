Use Case 1: Starting the Game
Title: Start Snake Game Description: As a player, I want to start the game so that I can begin playing the Snake game. Acceptance Criteria:

The game should display a start button on the main screen.

When the player clicks the start button, the game initializes and the snake appears on the screen.

Use Case 2: Controlling the Snake
Title: Control Snake Movement Description: As a player, I want to control the movement of the snake so that I can navigate it to eat food and avoid obstacles. Acceptance Criteria:

The player can use arrow keys (up, down, left, right) or (w, a ,s, d) to change the direction of the snake.

The snake should continuously move in the direction it is heading.

Use Case 3: Eating Food
Title: Snake Eats Food Description: As a player, I want the snake to eat food so that it grows longer and increases my score. Acceptance Criteria:

Food items randomly appear on the screen. If the snake's head don't collide with the food in a timeslice (10 sec) then it will dissapear, and a new one will reappear randomly.

When the snake's head collides with a food item, the snake grows longer and the food item disappears.

The player's score increases by a set amount each time the snake eats a food item.

Use Case 4: Game Over Condition
Title: Game Over Description: As a player, I want the game to end if the snake collides with the wall or itself so that I know when I have lost. Acceptance Criteria:

The game ends if the snake's head collides with the walls of the screen or any part of its own body.

A "Game Over" message is displayed along with the player's final score.

Use Case 5: Displaying the Score
Title: Display Score Description: As a player, I want to see my current score while playing the game so that I can track my progress. Acceptance Criteria:

The current score is displayed on the screen in a visible location.

The score updates in real-time as the snake eats food items.

Use Case 6: Increasing Difficulty
Title: Increase Game Difficulty Description: As a player, I want the game to become more challenging as I progress so that it remains engaging. Acceptance Criteria:

The speed of the snake increases as the player achieves higher scores.

With the increased speed also the timeslice where the food appearing should be shorter.

Optional: Additional obstacles appear on the screen as the game progresses.

These use cases cover the basic functionality and progression of the classic Snake game. Feel free to modify or expand upon these to suit your specific needs!


Technical requirements:
- The gui should be pygame
- The test framework is PyTest
- Utilize venv