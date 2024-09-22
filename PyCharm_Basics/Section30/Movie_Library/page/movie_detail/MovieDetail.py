import tkinter as tk
from doctest import master

from PIL.ImageOps import expand

from data.colors import COLORS
from PIL import Image, ImageTk

class MovieDetail:
    """
    Page to hold movie detail.
    """
    def __init__(
        self,
        window,
        bg_color,
        imdbID=None,
        movies=[],
        relief=tk.SUNKEN,
        side=tk.LEFT
    ):
        self.frame = tk.Frame(
            master=window,
            name="movieDetail",
            relief=relief,
            bg=bg_color
        )
        self.side = side
        self.imdbID = imdbID
        self.movies = movies
        self.add_frame()

    def add_frame(self):
        self.add_page_title("Movie Detail")
        self.add_content()
        self.frame.pack(
            side=self.side,
            fill=tk.BOTH,
            expand=True
        )

    def add_page_title(
        self,
        title
    ):
        lbl = tk.Label(
            self.frame,
            text=title,
            height=2,
            bg=COLORS.BLACK,
            fg=COLORS.WHITE,
            font=("Iosevka Custom", 12, "bold")
        )

        lbl.grid(
            row=0,
            column=0,
            columnspan=8,
            padx=1,
            pady=(0, 8),
            sticky="we"
        )

    def add_content(self):
        pass