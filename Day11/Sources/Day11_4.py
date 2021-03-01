import tkinter as tk

window = tk.Tk()
window.title("my Tkinter GUI")
window.minsize(width=500, height=300)


my_label = tk.Label(text="It's Label", font=("맑은 고딕", 18, "bold"))
my_label.pack()

window.mainloop()
