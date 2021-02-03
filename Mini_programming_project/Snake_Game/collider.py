from game_manager import GameManager

Epsilon = 2.73e-11


class Collider:
    def __init__(self, snake, food_spawner):
        self.snake = snake
        self.food_spawner = food_spawner
        self.game_manager = None

    def ref_game_manager(self, game_manager):
        self.game_manager = game_manager

    def collide_with_food(self):
        if (
            self.snake.body[0].xcor() - self.food_spawner.food.xcor()
        ) ** 2 < Epsilon and (
            self.snake.body[0].ycor() - self.food_spawner.food.ycor()
        ) ** 2 < Epsilon:
            return True
        else:
            return False

    def collide_with_wall(self):
        if (
            self.snake.body[0].xcor() > 290
            or self.snake.body[0].xcor() < -290
            or self.snake.body[0].ycor() < -290
            or self.snake.body[0].ycor() > 290
        ):
            return True
        else:
            return False

    def collide_with_tail(self):
        for i in range(4, len(self.snake.body)):
            if (
                self.snake.body[0].xcor() - self.snake.body[i].xcor()
            ) ** 2 < Epsilon and (
                self.snake.body[0].ycor() - self.snake.body[i].ycor()
            ) ** 2 < Epsilon:
                return True
        return False

    def check_collision(self):
        if self.collide_with_food():
            self.food_spawner.delete()
            self.snake.add_tail()
            self.game_manager.increase_score()
        elif self.collide_with_wall() or self.collide_with_tail():
            self.game_manager.game_over()