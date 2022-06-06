from turtle import Turtle
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("orange")
        self.refresh()
        self.speed("fastest")

    def refresh(self):
        rand_x = randint(-220,220)
        rand_y = randint(-220,220)
        self.goto(rand_x,rand_y)