# Step 1
import random
from hangman_art import stages, logo
from hangman_words import word_list
from os import system

print(logo)

answer = random.choice(word_list)

display = ["_" for _ in range(len(answer))]

game_end = False
lives = 6
last_guess = ""
while not game_end:
    blank_count = 0

    guess = input("Guess a letter: ").lower()

    system("cls")

    if guess in display:
        print(f"You've already guessed {guess}")
        print(" ".join(display))
    else:
        for i in range(len(answer)):
            if guess == answer[i]:
                display[i] = guess

        print(" ".join(display))

        if guess not in answer:
            print(f"You guessed {guess}, that's not in the word")
            lives -= 1
            if lives == 0:
                game_end = True
                print(f"You lose. The answer is {answer}.")

        if "_" not in display:
            game_end = True
            print("You Win!")

    print(stages[lives])