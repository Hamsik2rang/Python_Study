from paddle import Paddle
import random as rand


class Enemy(Paddle):
    def __init__(self, collider, ball):
        super().__init__(collider)
        self.starting_pos = ((-580, 20), (-580, 0), (-580, -20), (-580, -40))
        self.ball = ball
        self.create_paddle()

    def trace(self):
        if self.ball.xcor() > 150:
            return
        action_value = rand.randint(1, 100)
        standard_value = rand.randint(1, rand.randint(10, 15))
        if self.ball.ycor() < self.paddle[-1].ycor() and action_value > standard_value:
            self.move_down()
        elif self.ball.ycor() > self.paddle[0].ycor() and action_value > standard_value:
            self.move_up()
