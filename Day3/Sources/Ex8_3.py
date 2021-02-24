from art import logo_caesar_cipher

alphabet = [
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
]


def encrypt(text, shift):
    cipher = ""
    for i in range(len(text)):
        cipher += alphabet[(alphabet.index(text[i]) + shift) % len(alphabet)]
    return cipher


def decrypt(text, shift):
    decrypted_text = ""
    for i in range(len(text)):
        decrypted_text += alphabet[
            (len(alphabet) + alphabet.index(text[i]) - shift) % len(alphabet)
        ]
    return decrypted_text


def caesar(text, shift, direction):
    if direction == "encode":
        return_text = encrypt(text, shift)
    elif direction == "decode":
        return_text = decrypt(text, shift)
    else:
        return None
    print(f"The {direction}d text is {return_text}")


print(logo_caesar_cipher)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        print("Goodbye")
        should_end = True
