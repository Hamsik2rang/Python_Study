# Treasure Find Game(보물찾기/지뢰찾기)
import random

treasure_point = [random.randint(0, 2)]
# append 써보려고 이렇게 짜 봤음
treasure_point.append(random.randint(0, 2))

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

point_input = position.split()
point_input = [int(point_input[0]), int(point_input[1])]


point_input[0] -= 1
point_input[1] -= 1

if point_input[0] == treasure_point[0] and point_input[1] == treasure_point[1]:
    map[treasure_point[1]][treasure_point[0]] = "●"
else:
    map[point_input[1]][point_input[0]] = "X"

print(f"{row1}\n{row2}\n{row3}")