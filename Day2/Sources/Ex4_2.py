import random

whole_name = input()

name_list = whole_name.split(", ")

print(f"{random.choice(name_list)} is going to buy the meal today!")