import tkinter as tk
from tkinter import Label, Entry

window = tk.Tk()

window.title("Tkinter Basics - Label Entry")
window.geometry("1280x720")


lblName = Label(
    master=window,
    text="name"
)
lblLastName = Label(
    window,
    text="Last Name"
)

entName = Entry(window)
entLastName = Entry(window)

lblName.grid(row=0, column=0)
entName.grid(row=0, column=1)

lblLastName.grid(row=1, column=0)
entLastName.grid(row=1, column=1)

window.mainloop()