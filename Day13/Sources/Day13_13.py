# Class that inherit list
class AdvancedList(list):
    def replace(self, origin, new):
        if origin in self:
            self[self.index(origin)] = new


x = AdvancedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x.replace(0, 101)

print(x)