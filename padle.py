from turtle import Turtle


class Padle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position, 0)

    def go_up(self):
        new = self.ycor() + 20
        self.goto(self.xcor(), new)

    def go_down(self):
        new = self.ycor() - 20
        self.goto(self.xcor(), new)
