# pack(), grid(), place() in Tkinter
from tkinter import *
from typing import Collection


def calculate():
    miles = float(entry_miles.get())
    km = str(miles * 1.609).split(".")[0]
    label_calculated.config(text=km)


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

entry_miles = Entry(width=7)
entry_miles.grid(row=0, column=1)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_equal = Label(text="is equal to", font=("맑은 고딕", 10, "bold"))
label_equal.grid(row=1, column=0)

label_calculated = Label(text="0")
label_calculated.grid(row=1, column=1)

label_km = Label(text="Km")
label_km.grid(row=1, column=2)

button_calc = Button(text="Calculate", command=calculate)
button_calc.grid(row=2, column=1)

window.mainloop()