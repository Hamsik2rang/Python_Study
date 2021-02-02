import turtle as t
import time

HEAD = 0
ANGLE = 90
SIZE = 20
LATENCY = 0.1


class Snake:
    def __init__(self):
        self.body = []
        self.len = 3
        self.cur_direction = "Right"
        self.was_ate = False
        self.can_handle = True
        self.create_snake()

    def create_snake(self):
        first_pos = [(0, 0), (-20, 0), (-40, 0)]
        for i in range(self.len):
            segment = t.Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(first_pos[i])
            self.body.append(segment)

    def add_tail(self):
        segment = t.Turtle(shape="square")
        segment.color("black")
        segment.penup()
        self.was_ate = True
        self.body.append(segment)

    def turn_up(self):
        if self.can_handle:
            if self.cur_direction == "Right":
                self.body[HEAD].left(ANGLE)
                self.cur_direction = "Up"
            elif self.cur_direction == "Left":
                self.body[HEAD].right(ANGLE)
                self.cur_direction = "Up"
            else:
                pass
            self.can_handle = False

    def turn_down(self):
        if self.can_handle:
            if self.cur_direction == "Right":
                self.body[HEAD].right(ANGLE)
                self.cur_direction = "Down"
            elif self.cur_direction == "Left":
                self.body[HEAD].left(ANGLE)
                self.cur_direction = "Down"
            else:
                pass
            self.can_handle = False

    def turn_right(self):
        if self.can_handle:
            if self.cur_direction == "Up":
                self.body[HEAD].right(ANGLE)
                self.cur_direction = "Right"
            elif self.cur_direction == "Down":
                self.body[HEAD].left(ANGLE)
                self.cur_direction = "Right"
            else:
                pass
            self.can_handle = False

    def turn_left(self):
        if self.can_handle:
            if self.cur_direction == "Up":
                self.body[HEAD].left(ANGLE)
                self.cur_direction = "Left"
            elif self.cur_direction == "Down":
                self.body[HEAD].right(ANGLE)
                self.cur_direction = "Left"
            else:
                pass
            self.can_handle = False

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            if self.was_ate and i == len(self.body) - 1:
                self.was_ate = False
                self.body[i].color("white")
            self.body[i].goto(self.body[i - 1].pos())
            if not self.can_handle:
                self.can_handle = True
        self.body[HEAD].forward(20)
