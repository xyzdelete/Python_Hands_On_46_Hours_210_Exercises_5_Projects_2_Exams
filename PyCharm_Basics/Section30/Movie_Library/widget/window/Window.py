import tkinter as tk
from data.colors import COLORS
from data.geometry import GEOMETRY

class Window:
    """
    It creates tkinter main window.
    """

    def __init__(self, title):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.configure(bg=COLORS.BLACK)
        self.set_size()

    # Tkinter start
    def start_method(self):
        self.window.mainloop()

    # Method for window width and height
    def set_size(self):
        w, h = GEOMETRY.MAIN_WINDOW_WIDTH, GEOMETRY.MAIN_WINDOW_HEIGHT
        self.window.geometry("%dx%d" % (w, h))
