class Vector:
    def __init__(self, pos=(0, 0)):
        self.__x, self.__y = pos

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def set(self, pos):
        if pos == "up":
            self.__x, self.__y = (0, 1)
        elif pos == "down":
            self.__x, self.__y = (0, -1)
        elif pos == "right":
            self.__x, self.__y = (1, 0)
        elif pos == "left":
            self.__x, self.__y = (0, 1)
        else:
            self.__x, self.__y = pos

    def get(self):
        return (self.__x, self.__y)
