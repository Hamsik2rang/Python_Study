import random as rand
import turtle as t

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
is_gameover = False

screen = t.Screen()
screen.setup(width=500, height=400)
bet = screen.textinput("Choice", "가장 빠른 토북이를 골라주세요 : ")


def initialize():
    for ypos in range(-50, 51, 20):
        turtle = t.Turtle(shape="turtle")
        turtle.penup()
        turtle.color(colors[(ypos - (-50)) // 20])
        turtle.goto(-200, ypos)
        turtles.append(turtle)
        turtle.pendown()


def check(rabbit):
    global is_gameover
    if rabbit.xcor() > 230:
        is_gameover = True
        return rabbit.pencolor()
    else:
        return None


def run(rabbit):
    rabbit.forward(rand.randint(5, 20))


def compare(choice, winner):
    if input == winner:
        print("You Win")
    else:
        print(f"You lose. The winner rabbit is {winner}.")


initialize()

winner = None
while not is_gameover:
    for t in turtles:
        run(t)
        winner = check(t)
        if is_gameover:
            break

compare(bet, winner)

screen.exitonclick()