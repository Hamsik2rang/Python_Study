from turtle import Turtle

FONT = "Kenney Blocks"


class Scoreboard(Turtle):
    def __init__(self, pos=(0, 0), is_center=False):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(pos)
        self.score = 0
        if not is_center:
            self.update()

    def update(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=(FONT, 48, "bold"))

    def notice_game_over(self):
        self.clear()
        self.write("GAME OVER!", align="center", font=(FONT, 108, "bold"))

    def increase_score(self):
        self.score += 1
        self.update()