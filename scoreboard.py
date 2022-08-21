from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto((0, 270))
        self.display()

    def display(self):
        self.write(f"{self.r_score}  |  {self.l_score}", False, ALIGNMENT, FONT)

    def r_scores(self):
        self.r_score += 1

    def l_scores(self):
        self.l_score += 1

    def game_over(self):
        pass
