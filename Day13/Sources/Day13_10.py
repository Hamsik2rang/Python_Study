class Monster:
    def __init__(self):
        self.atk = 10
        self.dfs = 5
        self.hp = 40

class Dragon(Monster):
    def __init__(self):
        # Also can use like this:
        #     super(Dragon, self).__init__()
        super().__init__()

    def print_stat(self):
        print(f"Attack status : {self.atk}")
        print(f"Defence status : {self.dfs}")
        print(f"Health Point : {self.hp}")



yongyong = Dragon()
yongyong.print_stat()