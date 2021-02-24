import colorgram as cg
import turtle as t
import random as rand

colors = cg.extract("./Day6/Images/image.jpg", 30)

rabbit = t.Turtle()
rabbit.shape("turtle")
rabbit.speed("fastest")
rabbit.penup()

screen = t.Screen()
screen.colormode(255)


for ypos in range(
    50 - screen.window_height() // 2, screen.window_height() // 2 - 50, 50
):
    for xpos in range(
        -screen.window_width() // 2, screen.window_width() // 2 - 100, 50
    ):
        rabbit.color(rand.choice(colors).rgb)
        rabbit.setposition(xpos, ypos)
        rabbit.forward(50)
        rabbit.dot(30)


screen.exitonclick()