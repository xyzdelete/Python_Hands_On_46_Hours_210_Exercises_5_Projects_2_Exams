import tkinter as tk

class Window:
    """
    It creates tkinter main window.
    """

    def __init__(self, title):
        self.window = tk.Tk()
        self.window.title(title)

    # tkinter start
    def start_method(self):
        self.window.mainloop()