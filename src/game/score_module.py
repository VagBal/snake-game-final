class Score:
    def __init__(self):
        self._score = 0
        self._observers = []
    
    def add_observer(self, observer):
        self._observers.append(observer)
    
    def remove_observer(self, observer):
        self._observers.remove(observer)
    
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._score)
    
    def increase_score(self):
        self._score += 1
        self.notify_observers()
    
    def get_score(self):
        return self._score