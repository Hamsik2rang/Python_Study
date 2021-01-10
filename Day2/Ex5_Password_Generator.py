import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pw = ""

for _ in range(0, nr_letters):
    pw += random.choice(letters)
for _ in range(0, nr_symbols):
    pw += random.choice(numbers)
for _ in range(0, nr_symbols):
    pw += random.choice(symbols)

print("Here is your password:", pw)
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# use random.shuffle
reordered_pw_list = list(pw)
random.shuffle(reordered_pw_list)

reordered_pw = "".join(reordered_pw_list)

# instead of string.join, can use for loop like this
# reordered_pw = ""
# for c in reordered_pw_list:
#     reordered_pw += c

print("Here is your randomized password:", reordered_pw)