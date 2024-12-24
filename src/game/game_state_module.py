from settings import States

class GameState:
    def __init__(self):
        self.state = States.START
    
    def change_state(self, new_state):
        self.state = new_state