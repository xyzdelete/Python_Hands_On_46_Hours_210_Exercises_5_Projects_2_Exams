import tkinter as tk

window = tk.Tk()

window.title("Tkinter Basics - Check Button")
window.geometry("1280x720")

chkBtn_1 = tk.Checkbutton(
    master=window,
    text="Correct"
)
chkBtn_2 = tk.Checkbutton(
    master=window,
    text="Incorrect"
)

chkBtn_1.grid(
    row=0,
    column=0
)

chkBtn_2.grid(
    row=1,
    column=0
)

window.mainloop()