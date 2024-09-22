import tkinter as tk
from tkinter import Frame, Button

window = tk.Tk()

window.title("Tkinter Basics - Frame")
window.geometry("1280x720")

frame = Frame(window)

btnLeft = Button(
    master=frame,
    text="Frame Button Left",
    bg="black",
    fg="white"
)
btnLeft.pack(side=tk.LEFT)

btnRight = Button(
    master=frame,
    text="Frame Button Right",
    bg="black",
    fg="white"
)
btnRight.pack(side=tk.RIGHT)

frame.pack()

window.mainloop()