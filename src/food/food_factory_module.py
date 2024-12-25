from src.food.food_module import Food

# Factory pattern
class FoodFactory:
    @staticmethod
    def create_food(color, shape):
        return Food(color, shape) # create different types of food if needed