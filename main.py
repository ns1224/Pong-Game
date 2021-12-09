from ball import Ball
from court import Court
from paddle import Paddle
from scoreboard import Scoreboard
from turtle import Screen
import time


screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

court = Court()
l_paddle = Paddle("blue", (-350, 0))
r_paddle = Paddle("red", (350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:

    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce('y')

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce('x')

    # Detect right paddle miss
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.give_point('l')

    # Detect left miss
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.give_point('r')

screen.exitonclick()
