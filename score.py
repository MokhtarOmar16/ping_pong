from turtle import Turtle
from ball import Ball


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l = 0
        self.r = 0
        self.update_s()
    def update_s(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r, align="center", font=("Courier", 80, "normal"))

    def left_p(self):
        self.l += 1
        self.update_s()

    def right_p(self):
        self.r += 1
        self.update_s()
