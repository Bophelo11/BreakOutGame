import turtle
from turtle import Turtle
import random

tr = turtle.Turtle()
wn = turtle.Screen()

wn.addshape("Asset 1@4x.png")

COLOR_OPTIONS = [
              "light blue", "royal blue",
              "light steel blue", "steel blue",
              "light cyan", "light sky blue",
              "violet", "salmon", "tomato",
              "sandy brown", "purple", "deep pink",
              "medium sea green", "khaki"
]

weights = [
           1, 2, 1, 1, 3, 2, 1, 4, 1, 3,
           1, 1, 1, 4, 1, 3, 2, 2, 1, 2,
           1, 2, 1, 2, 1
]

class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.color(random.choice(IMAGES))
        self.goto(x=x_cor, y=y_cor)

        self.quantity = random.choice(weights)

class Bricks:
    def __init__(self):
        self.y_start = 0
        self.y_end = 240
        self.bricks = []
        self.make_de_lines_exe()

    def make_lines_exe(self, y_cor):
        for n in range(-570, 570, 63):
            brick = Brick(n, y_cor)
            self.bricks.append(brick)

    def make_de_lines_exe(self):
        for n in range(self. y_start, self.y_end,32):
            self.make_lines_exe(n)