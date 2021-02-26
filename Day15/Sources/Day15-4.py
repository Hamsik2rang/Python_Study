from tkinter import *


def clicked():
    my_label.config(text=entry.get())
    entry.delete(0, END)


window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)


# Label
my_label = Label(text="I Am a Label", font=("Roboto Mono", 24, "bold"))
my_label.pack(side="left")

my_label.config(text="New Text")


# Button
button = Button(text="Click Me", command=clicked)
button.pack(side="right")

# Entry
entry = Entry(width=20)
entry.pack()


window.mainloop()