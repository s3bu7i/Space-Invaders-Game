
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-240,-310)
        self.hideturtle()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Courier", 22, "bold"))

    def increase_score(self):
        self.score+=1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER :(", align="center", font=("Courier", 22, "bold"))

