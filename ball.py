from turtle import Turtle
import random
BALL_SPEED = 2
possible_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # vector format


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.direction = random.choice(possible_directions)

    def move(self):
        new_x = self.xcor() + (self.direction[0] * BALL_SPEED)
        new_y = self.ycor() + (self.direction[1] * BALL_SPEED)
        self.goto((new_x, new_y))

    def change_direction(self, direction):
        self.direction = direction

    def reset(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        self.change_direction(random.choice(possible_directions))
