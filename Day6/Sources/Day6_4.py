import turtle as t
import random as rand


rabbit = t.Turtle()
rabbit.speed("fastest")


screen = t.Screen()
screen.colormode(255)

rad = 3

for _ in range(120):
    rabbit.color(rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255))
    rabbit.left(rad)
    rabbit.circle(100)

screen.exitonclick()