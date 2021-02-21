numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

square_numbers = [i * i for i in numbers]

print(square_numbers)

odd_numbers = [i for i in numbers if i & 1 != 0]

print(odd_numbers)

with open("./Day10/Resources/file1.txt", mode="r") as f1:
    list_one = list(map(int, f1.readlines()))

with open("./Day10/Resources/file2.txt", mode="r") as f2:
    list_two = list(map(int, f2.readlines()))


list_intersection = [i for i in list_one if i in list_two]

print(list_intersection)