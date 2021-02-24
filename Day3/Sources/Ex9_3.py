from os import system
from art import logo_secret_auction

bids = {}

print(logo_secret_auction)
print("Welcome to the secret auction program.")


def find_winner():
    winner = ""
    highest_bid = 0
    for bidder in bids:
        if highest_bid < bids[bidder]:
            winner = bidder
            highest_bid = bids[bidder]

    return winner


def start_bid():
    should_end = False

    while not should_end:
        name = input("What is your name?: ")
        bid = input("What's your bid?: $")

        bids[name] = int(bid)

        is_more_bidder = input("Are there any other bidders? Type 'yes' or 'no' .\n")
        is_more_bidder.lower()
        if is_more_bidder != "yes":
            should_end = True

    winner = find_winner()
    print(f"The winner is {winner} with a bid of ${bids[winner]}.")


start_bid()
