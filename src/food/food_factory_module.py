from src.food.food_module import Food

class FoodFactory:
    @staticmethod
    def create_food():
        return Food() # create different types of food if needed