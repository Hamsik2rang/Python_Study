from turtle import Turtle
from vector import Vector

DISTANCE = 20


class Paddle:
    def __init__(self, collider):
        self.paddle = []
        self.vector = Vector()
        self.starting_pos = ((0, 20), (0, 0), (0, -20), (0, -40))
        self.collider = collider

    def create_paddle(self):
        """새로운 발판을 생성합니다. 오버라이딩 시 생성자에서 self.starting_pos에 발판이 생성될 값을 지정해야 합니다."""
        for pos in self.starting_pos:
            component = Turtle(shape="square")
            component.penup()
            component.color("white")
            component.goto(pos)
            component.setheading(90)
            component.clear()
            self.paddle.append(component)

    def move_up(self):
        self.vector.set("up")
        if self.collider.check(self):
            return
        for i in range(len(self.paddle) - 1, 0, -1):
            self.paddle[i].goto(self.paddle[i - 1].pos())
        self.paddle[0].forward(DISTANCE)

    def move_down(self):
        self.vector.set("down")
        if self.collider.check(self):
            return
        for i in range(0, len(self.paddle) - 1):
            self.paddle[i].goto(self.paddle[i + 1].pos())
        self.paddle[-1].back(DISTANCE)
