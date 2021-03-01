# Password Generator using JSON Format
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from typing import Collection
from random import *
import pyperclip
import json

######### Password Generator Function #########
def generate_password():
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

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


######### Search Password #########
def search_data():
    search_website = entry_website.get()

    with open("./Day16/Resources/save.json", mode="r") as f:
        data = json.load(f)

        is_exist = False
        for website in data:
            if search_website == website:
                is_exist = True

                username = data[website]["username"]
                password = data[website]["password"]
                break
        if is_exist:
            entry_username.insert(0, username)
            entry_password.insert(0, password)


######### Save Password #########
def save_data():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()
    new_data = {
        website: {"username": username, "password": password},
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Sorry", message="Please make sure you haven't left any fields empty."
        )
        label_website.focus()
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \nUsername: {username} \npassword: {password} \nIs it OK to save?",
    )
    if is_ok:
        try:
            with open("./Day16/Resources/save.json", mode="r") as f:
                data = json.load(f)
                data.update(new_data)
        except:
            with open("./Day16/Resources/save.json", mode="w") as f:
                data = new_data
        finally:
            with open("./Day16/Resources/save.json", mode="w") as f:
                json.dump(data, f, indent=4)
                entry_website.delete(0, END)
                entry_password.delete(0, END)


######### UI Setup #########
window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="./Day16/Resources/logo.png")
canvas.create_image(115, 100, image=image)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0, sticky="W")

label_username = Label(text="Email/Username:")
label_username.grid(row=2, column=0, sticky="W")

label_password = Label(text="Password:")
label_password.grid(row=3, column=0, sticky="W")


entry_website = Entry(width=27)
entry_website.grid(row=1, column=1, sticky="W")
entry_website.focus()

entry_username = Entry(width=45)
entry_username.grid(row=2, column=1, columnspan=2, sticky="W")

entry_password = Entry(width=27)
entry_password.grid(row=3, column=1, sticky="W")

button_search = Button(text="Search", width=15, command=search_data)
button_search.grid(row=1, column=2, sticky="EW")

button_generate = Button(text="Generate Password", width=15, command=generate_password)
button_generate.grid(row=3, column=2, sticky="EW")

button_add = Button(text="Add", command=save_data)
button_add.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()