import random
from Ex4_ASCII_Arts import rock, scissors, paper

game_images = [rock, paper, scissors]

ai_choice = random.randint(0, 2)
player_choice = int(
    input("What do you choose? Type 0(Rock), 1(Paper), or 2(Scissors): \n")
)

print()
print("Computer Chose:\n")
print(game_images[ai_choice] + "\n")
print("You Chose:\n")
print(game_images[player_choice] + "\n")

if ai_choice - player_choice == 1:
    print("You lose.\n")
elif ai_choice - player_choice == 0:
    print("Draw.\n")
elif player_choice < 0 or player_choice > 2:
    print("You typed an invalid number. you lose!\n")
else:
    print("You Win!\n")