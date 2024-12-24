class Command:
    def execute(self):
        pass

class MoveUp(Command):
    def execute(self, snake):
        snake.change_direction((0, -20))

class MoveDown(Command):
    def execute(self, snake):
        snake.change_direction((0, 20))

class MoveRight(Command):
    def execute(self, snake):
        snake.change_direction((20, 0))

class MoveLeft(Command):
    def execute(self, snake):
        snake.change_direction((-20, 0))
