from turtle import Turtle, Screen

rabbit = Turtle()


rabbit.shape("turtle")
rabbit.color(0.3, 0.4, 0.5)


rabbit.penup()
rabbit.back(500)

for i in range(96):
    if i & 1:
        rabbit.pendown()
    else:
        rabbit.penup()
    rabbit.forward(10)

rabbit.shape("classic")
rabbit.stamp()


rabbit.shape("turtle")
rabbit.hideturtle()

screen = Screen()
screen.exitonclick()