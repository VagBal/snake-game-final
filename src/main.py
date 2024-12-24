import sys
import os

# Add the src directory to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from game.game_module import Game

if __name__ == "__main__":
    game = Game()
    game.run()