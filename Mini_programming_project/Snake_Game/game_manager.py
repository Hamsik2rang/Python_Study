from turtle import Turtle


class GameManager(Turtle):
    def __init__(self, snake, food_spawner, collider):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.game_is_on = True
        self.score = 3
        self.update_scoreboard()

    def game_over(self):
        self.game_is_on = False
        self.clear()
        self.goto(0, 0)
        self.update_scoreboard()

    def update_scoreboard(self):
        if not self.game_is_on:
            self.write(
                f"   GAME OVER!\nFinal Score is {self.score}",
                align="center",
                font=("Ariel", 24, "bold"),
            )
            return
        self.write(
            f"Snake's Length : {self.score}", align="center", font=("Ariel", 24, "bold")
        )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
