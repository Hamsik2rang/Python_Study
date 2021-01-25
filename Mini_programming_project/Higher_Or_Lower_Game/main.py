import random
from os import system

from art import logo, vs
from data import data

SCORE = 0


def get_comparison_data(compare_left):
    if compare_left == "":
        compare_left = random.choice(data)
    compare_right = random.choice(data)

    while compare_left == compare_right:
        compare_right = random.choice(data)

    return [compare_left, compare_right]


def introduce(data):
    """data must be dictionary"""
    print(f"{data['name']}, a {data['description']}, from {data['country']}.")


def sort(comparison_data, choice):
    if choice == "B":
        comparison_data[0], comparison_data[1] = comparison_data[1], comparison_data[0]
    return comparison_data


def compare(comparison_data):
    if comparison_data[0]["follower_count"] > comparison_data[1]["follower_count"]:
        return True
    else:
        return False


def game():
    result = True
    comparison_data = ["", ""]
    while result == True:
        global SCORE

        comparison_data = get_comparison_data(comparison_data[0])

        print(logo)
        print(f"Compare A: ", end="")
        introduce(comparison_data[0])

        print(vs)

        print(f"Against B: ", end="")
        introduce(comparison_data[1])

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        comparison_data = sort(comparison_data, guess)
        result = compare(comparison_data)
        system("cls")
        print(logo)
        if result == True:
            SCORE += 1
            print(f"You're right! Current score: {SCORE}")
        else:
            print(f"Sorry, that's wrong. Final score: {SCORE}")


game()