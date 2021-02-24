import random

logo = """___________                        _________                      __  .__    .__                 
\__    ___/__.__.______   ____    /   _____/ ____   _____   _____/  |_|  |__ |__| ____    ____   
  |    | <   |  |\____ \_/ __ \   \_____  \ /  _ \ /     \_/ __ \   __\  |  \|  |/    \  / ___\  
  |    |  \___  ||  |_> >  ___/   /        (  <_> )  Y Y  \  ___/|  | |   Y  \  |   |  \/ /_/  > 
  |____|  / ____||   __/ \___  > /_______  /\____/|__|_|  /\___  >__| |___|  /__|___|  /\___  /  
          \/ | __ | \/ \/ \/ \/ \/ \//_____/ """


ANSWER = random.randint(1, 100)
EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def intro():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def set_turn_count(difficulty):
    if difficulty == "easy":
        guess_count = EASY_LEVEL_TURN
    elif difficulty == "hard":
        guess_count = HARD_LEVEL_TURN
    return guess_count


def guess_number(input):
    print(ANSWER)
    if input == ANSWER:
        return 0
    elif input > ANSWER:
        return 1
    else:
        return -1


intro()

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
guess_count = set_turn_count(difficulty)

while guess_count > 0:
    print(f"You have {guess_count} attempts remaining to guess the number.")
    guess_count -= 1

    guess = int(input("Make a guess: "))
    result = guess_number(guess)
    if result == 0:
        print(f"You got it!. The answer is {guess}.")
        break
    elif result == 1:
        print("Too High.")
    else:
        print("Too Low.")