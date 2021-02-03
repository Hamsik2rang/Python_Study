EPSILON = 2.73e-11


class Collider:
    def __init__(self, player=None, enemy=None, ball=None):
        self.__outside_right = 590
        self.__outside_left = -590
        self.__outside_up = 390
        self.__outside_down = -390

        self.__player = player
        self.__enemy = enemy
        self.__ball = ball

    def set_player(self, player):
        self.__player = player

    def set_enemy(self, enemy):
        self.__enemy = enemy

    def set_ball(self, ball):
        self.__ball = ball

    def is_collide_with_wall(self, collider):
        """상하단 벽과 충돌 체크 메서드. collider에는 self, vector에는 이동 방향을 리스트로 전달, 충돌하거나 충돌할 수 있는 경우 True, 그렇지 않은 경우 False 반환"""
        # collider가 패들인 경우
        if collider is (self.__player or self.__enemy):
            # 방향벡터가 위이면서 y상단에 이동하려 하거나, 방향벡터가 아래이면서 y하단에 이동하려 하는 경우
            if (
                collider.paddle[0].ycor() + 20 > self.__outside_up
                and collider.vector.y > 0
            ) or (
                collider.paddle[-1].ycor() - 20 < self.__outside_down
                and collider.vector.y < 0
            ):
                # if collider is self.__player:
                #     print("player : collide with wall")
                # elif collider is self.__enemy:
                #     print("enemy : collide with wall")
                return True
            else:
                return False
        # collider가 공인 경우
        elif collider is self.__ball:
            # 방향벡터가 위이면서 y상단에 이동하려 하거나, 방향벡터가 아래이면서 y하단에 이동하려 하는 경우
            if (collider.ycor() + 20 > self.__outside_up and collider.vector.y > 0) or (
                collider.ycor() - 20 < self.__outside_down and collider.vector.y < 0
            ):
                # print("ball : collide with wall")
                return True
            else:
                return False

    def is_collide_with_paddle(self):
        """공과 패들의 충돌 체크 메서드"""
        if (
            self.__ball.xcor() + 20 - self.__player.paddle[0].xcor()
        ) ** 2 < EPSILON or (
            self.__ball.xcor() - 20 - self.__enemy.paddle[0].xcor()
        ) ** 2 < EPSILON:
            ball_ypos = self.__ball.ycor()
            player_first_ypos = self.__player.paddle[0].ycor()
            player_last_ypos = self.__player.paddle[-1].ycor()
            enemy_first_ypos = self.__enemy.paddle[0].ycor()
            enemy_last_ypos = self.__enemy.paddle[-1].ycor()

            if (
                ball_ypos < player_first_ypos + EPSILON
                and ball_ypos > player_last_ypos - EPSILON
            ) or (
                ball_ypos < enemy_first_ypos + EPSILON
                and ball_ypos > enemy_last_ypos - EPSILON
            ):
                # print("ball : collide with paddle")
                return True
            else:
                return False
        else:
            return False

    def is_out(self):
        """공이 필드 밖으로 나갔는지 체크 메서드"""
        # enemy 득점
        if (
            self.__ball.xcor() > self.__outside_right
            or self.__ball.xcor() < self.__outside_left
        ):
            # print("ball : fall out")
            return True
        else:
            return False

    def check(self, collider):
        """encapsulated collision check method.if collider is ball and it was collide with paddle, return 0. else if it was out, return 1."""
        if (collider is self.__player) or (collider is self.__enemy):
            return self.is_collide_with_wall(collider)
        elif collider is self.__ball:
            if self.is_collide_with_paddle():
                return 0
            elif self.is_collide_with_wall(collider):
                return 1
            elif self.is_out():
                return 2
        else:
            return None