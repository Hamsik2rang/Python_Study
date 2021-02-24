import random as rand
from food import Food
import time


class FoodSpawner:
    def __init__(self):
        self.food = None
        self.spawn()

    def spawn(self):
        xpos = rand.randint(-280, 280)
        xpos = (xpos // 20) * 20
        ypos = rand.randint(-280, 280)
        ypos = (xpos // 20) * 20

        self.food = Food((xpos, ypos))

    def delete(self):
        """지우고 다시 삭제하지 말고 refresh 메서드를 쓰면 더 적은 자원으로 구현 가능(Object Pooling)"""
        self.food.hideturtle()
        del self.food
        self.spawn()