from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__() # inherits from the Turtle class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # New Food location
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)
