from turtle import Turtle, Screen
import time

from player import Player
from enemy import Enemy
from referee import Referee
from collider import Collider
from ball import Ball

FRAME = 0.1


def draw_line():
    line = Turtle(shape="square")
    line.speed("fastest")
    line.penup()
    line.pencolor("white")
    line.pensize(15)
    line.goto(0, 390)
    line.setheading(270)

    for i in range(0, 11):
        if i & 1:
            line.penup()
        else:
            line.pendown()
        line.forward(80)


screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("Hamsik2rang's Pong")
screen.tracer(0)
screen.listen()

draw_line()

collider = Collider()
player = Player(collider)
ball = Ball(collider=collider)
enemy = Enemy(collider=collider, ball=ball)
referee = Referee(player=player, enemy=enemy, ball=ball)
screen.update()

collider.set_player(player)
collider.set_enemy(enemy)
collider.set_ball(ball)

ball.set_referee(referee=referee)
screen.onkeypress(key="Up", fun=player.move_up)
screen.onkeypress(key="Down", fun=player.move_down)


# write game logic below
while referee.game_is_on:
    screen.update()
    time.sleep(FRAME)
    ball.move()
    enemy.trace()


screen.exitonclick()