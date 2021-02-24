from turtle import Turtle
import random as rand

from vector import Vector


COLLIDE_WITH_PADDLE = 0
COLLIDE_WITH_WALL = 1

DISTANCE = 20

random_start_vector = ((1, 1), (1, -1), (-1, -1), (-1, 1))


class Ball(Turtle):
    def __init__(self, collider, referee=None):
        super().__init__(shape="circle")
        self.collider = collider
        self.vector = Vector(rand.choice(random_start_vector))
        self.referee = referee

        self.penup()
        self.color("white")
        self.collider = collider

    def set_referee(self, referee):
        self.referee = referee

    def move(self):
        collide_check_result = self.collider.check(self)
        # 충돌체와 닿은 경우
        if collide_check_result == 0 or collide_check_result == 1:
            self.bounce(collide_check_result)
        # 밖으로 나간 경우
        elif collide_check_result == 2:
            xpos = self.xcor()
            self.new_game()
            if xpos > 0:
                # 오른쪽 밖으로 나갔으면 enemy 득점
                self.referee.give_enemy_score()
            else:
                # 왼쪽 밖으로 나갔으면 player 득점
                self.referee.give_player_score()
        new_pos = (
            self.xcor() + (DISTANCE * self.vector.x),
            self.ycor() + (DISTANCE * self.vector.y),
        )
        self.goto(new_pos)

    def bounce(self, check_result):
        """충돌체와 충돌 시 방향을 변경합니다. check_result에 충돌 검사 결과를 전달합니다."""
        random_y_vector = (-1, 1)
        if check_result == COLLIDE_WITH_PADDLE:
            self.vector.set((-1 * self.vector.x, rand.choice(random_y_vector)))
        elif check_result == COLLIDE_WITH_WALL:
            self.vector.set((self.vector.x, -1 * self.vector.y))

    def new_game(self):
        """누군가 득점하거나 게임이 끝났을 때, 공을 중앙으로 되돌리고 방향을 반대로 설정합니다."""
        random_y_vector = (-1, 1)
        self.vector.set((-1 * self.vector.x, rand.choice(random_y_vector)))
        self.goto(0, 0)
