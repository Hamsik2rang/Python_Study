from turtle import Turtle


class Food(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.goto(pos)