import tkinter as tk
from data.colors import COLORS
from data.menus import MENU
from widget.button.Button import Button


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
        self.add_menus()

    def add_frame(self):
        self.frame.pack(
            side=tk.LEFT,
            fill=tk.Y,
            pady=(62, 0)
        )

    def add_menus(self):
        # add menus in loop
        for menu_key, menu_text in MENU.items():
            button = Button(
                self.frame,
                menu_key,
                menu_text,
                COLORS.ORANGE,
                COLORS.BLACK,
                18,
                2
            )