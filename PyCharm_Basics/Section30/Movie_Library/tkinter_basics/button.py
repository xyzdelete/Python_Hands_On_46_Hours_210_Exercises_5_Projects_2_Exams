import tkinter as tk

window = tk.Tk()

window.title("Tkinter Basics - Button")
window.geometry("1280x720")

btn = tk.Button(
    master=window,
    text="Close",
    width=25,
    height=10,
    bg="grey",
    command=window.destroy
)

btn.pack()

window.mainloop()