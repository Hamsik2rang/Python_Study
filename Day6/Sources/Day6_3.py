import turtle as t
import random


class RabbitController:
    def __init__(self, rabbit, move_count):
        self.rabbit = rabbit
        self.move_count = move_count

    def process(self):
        for _ in range(self.move_count):
            rgb = (random.random(), random.random(), random.random())
            self.rabbit.pencolor(rgb)
            self.rabbit.setheading(90 * random.randint(0, 3))
            self.rabbit.forward(30)


rabbit = t.Turtle()
rabbit.pensize(10)
rabbit.speed("fast")


rabbit_controller = RabbitController(rabbit, 500)
rabbit_controller.process()
