from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-230, 260)
        self.write(f"Level: {self.score}", align="center", font=FONT)
    def add_level(self):
        self.score += 1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)