import tkinter as tk
from turtledemo.nim import COLOR

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
            bg=COLORS.BLACK
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

    # method for click event of menu buttons
    def handle_click(
            self,
            event
    ):
        self.manage_button_colors(event)

    def add_menus(self):
        # add menus in loop
        for menu_key, menu_text in MENU.items():
            if menu_key == "about":
                button = Button(
                    self.frame,
                    menu_key,
                    menu_text,
                    COLORS.ORANGE,
                    COLORS.BLACK,
                    18,
                    2,
                    handle_click=self.handle_click,
                    side=tk.BOTTOM
                )
            else:
                button = Button(
                    self.frame,
                    menu_key,
                    menu_text,
                    COLORS.ORANGE,
                    COLORS.BLACK,
                    18,
                    2,
                    handle_click=self.handle_click,
                    side=tk.TOP
                )

    def manage_button_colors(
            self,
            event
    ):
        # clicked button -> event.widget
        # all the menu buttons -> event.widget.master.children
        for child in event.widget.master.winfo_children():
            if child == event.widget:
                child.configure(
                    bg=COLORS.ORANGE,
                    fg=COLORS.WHITE
                )
            else:
                child.configure(
                    bg=COLORS.BLACK,
                    fg=COLORS.ORANGE
                )