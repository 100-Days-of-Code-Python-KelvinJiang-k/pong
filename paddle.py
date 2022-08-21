from turtle import Turtle
PADDLE_LENGTH = 5
PADDLE_SPEED = 20
PADDLE_WIDTH = 1


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=PADDLE_LENGTH, stretch_len=PADDLE_WIDTH)
        self.goto(position)

    def up(self):
        self.sety(self.ycor() + PADDLE_SPEED)

    def down(self):
        self.sety(self.ycor() - PADDLE_SPEED)
