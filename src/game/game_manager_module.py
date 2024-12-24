from settings import States

class GameManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
            cls._instance.init_game()
        return cls._instance
    
    def init_game(self):
        self.state = States.START
    
    def change_state(self, new_state):
        self.state = new_state