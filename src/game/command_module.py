# Command pattern

from settings import SNAKE_SIZE

class Command:
    def execute(self):
        pass

class MoveUp(Command):
    def execute(self, snake):
        snake.change_direction((0, -SNAKE_SIZE))

class MoveDown(Command):
    def execute(self, snake):
        snake.change_direction((0, SNAKE_SIZE))

class MoveRight(Command):
    def execute(self, snake):
        snake.change_direction((SNAKE_SIZE, 0))

class MoveLeft(Command):
    def execute(self, snake):
        snake.change_direction((-SNAKE_SIZE, 0))
