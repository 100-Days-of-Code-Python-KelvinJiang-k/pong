from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.colormode(255)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")

screen.tracer(1)

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    ball.move()

    # Detect collision with top/bottom wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_direction((ball.direction[0], -ball.direction[1]))

    # Detect collision with both paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.change_direction((-ball.direction[0], ball.direction[1]))

    # Detect collision with right wall
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_scores()

    # Detect collision with left wall
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_scores()

    if scoreboard.game_over():
        pass

screen.exitonclick()
