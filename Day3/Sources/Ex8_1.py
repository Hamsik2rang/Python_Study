import math


def get_can_count(height, width):
    cans = math.ceil(height * width / coverage)
    return cans


height = int(input("height: "))
width = int(input("width: "))

coverage = 5

print(f"You will need {get_can_count(height,width)} cans of paint.")