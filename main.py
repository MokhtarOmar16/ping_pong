import time
from turtle import Screen, Turtle
from padle import Padle
from ball import Ball
from score import Score


scr = Screen()
scr.bgcolor("black")
scr.setup(800, 600)
scr.title("ping-pong")
scr.tracer(0)

paddle_r = Padle(350)
paddle_l = Padle(-350)
ball = Ball()
score = Score()

scr.listen()
scr.onkey(paddle_r.go_up, "Up")
scr.onkey(paddle_r.go_down, "Down")

scr.onkey(paddle_l.go_up, "w")
scr.onkey(paddle_l.go_down, "s")

while True:
    time.sleep(ball.move_speed)
    scr.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(paddle_r) < 40 and ball.xcor() > 315 or ball.distance(paddle_l) < 40 and ball.xcor() < -315:
        ball.hit()
    if ball.xcor() > 380:
        ball.re()
        score.left_p()
    if ball.xcor() < -380:
        ball.re()
        score.right_p()

scr.exitonclick()
