# Blackjack Project
from art import logo
from os import system
import random


def draw_card():
    """Returns an random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def get_should_play():
    """If type 'y' return True, otherwise return false"""
    wanna_play = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': "
    ).lower()
    if wanna_play == "y":
        return True
    else:
        return False


def calculate_score(list):
    return sum(list)


def compare(player_sum, dealer_sum):
    """Both two arguments must be int type."""
    if player_sum > dealer_sum:
        return 1
    elif player_sum == dealer_sum:
        return 0
    else:
        return -1


was_draw = False

while was_draw or get_should_play():
    system("cls")
    print(logo)
    player = []
    dealer = []
    dealer.append(draw_card())
    player.append(draw_card())

    next_draw = True
    while next_draw:
        player.append(draw_card())
        print(f"\tyour cards: {player}, current score: {calculate_score(player)}")
        print(f"\tComputer's first card: {dealer[-1]}")

        if compare(calculate_score(player), 21) == 1:
            if 11 in player:
                player[player.index(11)] = 1
            else:
                break

        should_next_draw = input(
            "Type 'y' to get another card, type 'n' to pass: "
        ).lower()

        if should_next_draw == "y":
            next_draw = True
        else:
            next_draw = False

    if compare(calculate_score(player), 21) == 1:
        print("You went over. You lose.😭")
    else:
        while compare(calculate_score(dealer), 16) < 1:
            dealer.append(draw_card())

        result = compare(calculate_score(player), calculate_score(dealer))
        print(
            f"\tYour final hand: {player[-1]}, final score: {calculate_score(player)}"
        )
        print(
            f"\tComputer's final hand: {dealer[-1]}, final score: {calculate_score(dealer)}"
        )
        if result == 1 or calculate_score(dealer) > 21:
            if compare(calculate_score(dealer), 21) == 1:
                print("Opponent went over. You win!😎")
            else:
                print("You Win!😎")
        elif result == 0:
            print("Draw. Get next game.🤔")
            was_draw = True
        else:
            print("You lose.😭")
