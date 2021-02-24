from scoreboard import Scoreboard
import time


class Referee:
    def __init__(self, player=None, enemy=None, ball=None):
        self.__player_score = Scoreboard(pos=(300, 320))
        self.__enemy_score = Scoreboard(pos=(-300, 320))
        self.__notice = Scoreboard(is_center=True)

        self.player = player
        self.enemy = enemy
        self.ball = ball
        self.game_is_on = True

    def give_player_score(self):
        self.__player_score.increase_score()
        if self.__player_score.score >= 15:
            self.game_over()
        else:
            time.sleep(3)

    def give_enemy_score(self):
        self.__enemy_score.increase_score()
        if self.__enemy_score.score >= 15:
            self.game_over()
        else:
            time.sleep(3)

    def game_over(self):
        self.game_is_on = False
        self.__notice.notice_game_over()
        time.sleep(3)
