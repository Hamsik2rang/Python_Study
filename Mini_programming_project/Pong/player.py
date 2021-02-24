from paddle import Paddle


class Player(Paddle):
    def __init__(self, collider):
        super().__init__(collider)
        self.starting_pos = ((580, 20), (580, 0), (580, -20), (580, -40))
        self.create_paddle()