from turtle import Turtle, Screen

rabbit = Turtle()

print(rabbit)

rabbit.shape("turtle")
my_screen = Screen()
my_screen.colormode()

rabbit.color(0, 0.5, 0)

print(my_screen.canvheight)
my_screen.exitonclick()