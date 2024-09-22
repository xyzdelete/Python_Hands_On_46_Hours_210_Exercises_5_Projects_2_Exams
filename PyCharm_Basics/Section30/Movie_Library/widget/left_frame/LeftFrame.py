import tkinter as tk
from data.colors import COLORS

class LeftFrame:
    """
    Class for left Frame to hold the menu items.
    """

    def __init__(self, window, name):
        self.frame = tk.Frame(
            master=window,
            name=name,
            bg=COLORS.GRAY
        )

        self.master = window
        self.add_frame()
        self.add_button()

    def add_frame(self):
        self.frame.pack(
            side=tk.LEFT,
            fill=tk.Y,
            pady=(62, 0)
        )

    def add_button(self):
        btn = tk.Button(
            master=self.frame,
            text="Left Menu Button"
        )
        btn.pack()