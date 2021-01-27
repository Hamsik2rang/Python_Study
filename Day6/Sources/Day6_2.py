# 정삼각형 ~ 정이십사각형
from turtle import Turtle, Screen

import random

rabbit = Turtle()
rabbit.shape("turtle")
rabbit.pensize(3)
rabbit.penup()
rabbit.setposition(-25, 200)
rabbit.pendown()
for a in range(3, 25):
    red = random.random()
    green = random.random()
    blue = random.random()
    rabbit.pencolor(red, green, blue)
    r = 360 / a
    for _ in range(a):
        rabbit.forward(50)
        rabbit.right(r)

screen = Screen()
screen.exitonclick()