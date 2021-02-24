import turtle as t
import time

from food_spawner import FoodSpawner
from snake import Snake
from collider import Collider
from game_manager import GameManager

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.update()

food_spawner = FoodSpawner()
screen.update

collider = Collider(snake=snake, food_spawner=food_spawner)

game_manager = GameManager(snake=snake, food_spawner=food_spawner, collider=collider)
collider.ref_game_manager(game_manager)

screen.listen()
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)

# write game logic below
while game_manager.game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    collider.check_collision()

screen.exitonclick()