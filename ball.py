from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("cyan")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1
    def move(self):
        new_y = self.ycor() + self.move_y
        new_x = self.xcor() + self.move_x
        self.goto(new_x, new_y)

    def bounce(self):
        self.move_y *= -1

    def hit(self):
        self.move_x *= -1
        self.move_speed *= 0.9
    def re(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.hit()
