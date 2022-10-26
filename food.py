from turtle import Turtle
from random import *

class Food(Turtle):
    def __init__(self, w, h):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.new_location(w, h)

    def new_location(self, w, h):
        self.x = randint(-w // 2 + 20, w // 2 - 20)
        self.y = randint(-h // 2 + 20, h // 2 - 20)
        self.goto(self.x,self.y)