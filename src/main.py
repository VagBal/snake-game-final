import sys
import os

# Add the src directory to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from game.game_module import Game

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()