import pygame

from src.snake.snake_module import Snake
from src.food.food_factory_module import FoodFactory
from src.game.score_module import Score
from src.game.game_manager_module import GameManager
from src.game.command_module import MoveUp, MoveDown, MoveLeft, MoveRight
from settings import States
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, SNAKE_SPEED

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = FoodFactory.create_food()
        self.score = Score()
        self.score.add_observer(self)
        self.manager = GameManager()
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.handle_iput(event.key)
            
            self.snake.move()

            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.food = FoodFactory.create_food()
                self.score.increase_score()

            if self.check_collisions():
                self.manager.change_state(States.GAME_OVER)
                running = False

            self.draw()
            self.clock.tick(SNAKE_SPEED)
            
    def handle_iput(self, key):
        if key == pygame.K_UP:
            MoveUp().execute(self.snake)
        elif key == pygame.K_DOWN:
            MoveDown().execute(self.snake)
        elif key == pygame.K_LEFT:
            MoveLeft().execute(self.snake)
        elif key == pygame.K_RIGHT:
            MoveRight().execute(self.snake)

    def check_collisions(self):
        head = self.snake.body[0]
        if head[0] < 0 or head[0] >= SCREEN_WIDTH or \
        head[1] < 0 or head[1] >= SCREEN_HEIGHT:
            return True
        if head in self.snake.body[1:]:
            return True
        return False
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.draw_score()
        pygame.display.flip()

    def draw_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score {self.score.get_score()}", True, (255,255,255))
        self.screen.blit(score_text, (10, 10))

    def update(self, score):
        print(f"Score updated:  {score}")