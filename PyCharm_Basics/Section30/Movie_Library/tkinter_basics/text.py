import tkinter as tk
from tkinter import Text

window = tk.Tk()
window.title("Tkinter Basics - Text")
window.geometry("1280x720")

txt = Text(
    window,
    height=2,
    width=40
)

txt.pack()

window.mainloop()