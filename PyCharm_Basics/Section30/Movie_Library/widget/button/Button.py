import tkinter as tk
from data.colors import COLORS

# Wrapper Class -> wrapped tkinter.Button()
class Button:
    """
    It will create Tkinter Button.
    """
    def __init__(
            self,
            master,
            name,
            text,
            fg,
            bg,
            width,
            height,
            padx=0,
            pady=0,
            side=tk.TOP
    ):
        self.button = tk.Button(
            master=master,
            name=name,
            text=text,
            fg=fg,
            bg=bg,
            width=width,
            height=height,
            activebackground=COLORS.ORANGE
        )
        self.padx = padx
        self.pady = pady
        self.side = side
        self.add_button()

    def add_button(self):
        self.button.configure(
            font=("Arial", 12)
        )
        self.button.pack(
            padx = self.padx,
            pady = self.pady,
            side = self.side
        )

