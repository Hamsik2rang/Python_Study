class Animal:
    num_of_legs = 4

    def __init__(self):
        self.num_of_eyes = 2

    def breath(self):
        print("들숨, 날숨.")


class Fish(Animal):
    def __init__(self):
        pass

    def swim(self):
        print("첨벙첨벙")


nemo = Fish()
nemo.swim()
nemo.breath()