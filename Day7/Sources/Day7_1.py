# Etch-A-Sketch program
import turtle as t

rabbit = t.Turtle()
screen = t.Screen()


def move_forwards():
    rabbit.forward(10)


def move_back():
    rabbit.back(10)


def turn_right():
    rabbit.right(15)


def turn_left():
    rabbit.left(15)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=t.resetscreen)

screen.exitonclick()