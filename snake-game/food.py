from turtle import Turtle
import random


# Constants
FOOD_COLOR = "green"
FOOD_SHAPE = "circle"
FOOD_SIZE = 0.7


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_wid=FOOD_SIZE, stretch_len=FOOD_SIZE)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        """Move the food to a random location"""
        while True:
            random_x = random.randint(-14, 14) * 20
            random_y = random.randint(-14, 14) * 20
            # Avoid the area around the scoreboard text
            if not (-50 < random_x < 50 and 240 < random_y < 290):
                break
        self.goto(random_x, random_y)