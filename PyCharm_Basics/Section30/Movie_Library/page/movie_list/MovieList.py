import tkinter as tk
from tkinter import ttk
import csv
from tkinter.font import names

from PIL import Image, ImageTk
from PIL.ImageOps import expand

from data.colors import COLORS

class MovieList:
    """
    This class is the frame for movie list.
    """

    # column list
    columns = ["imdbID", "Id", "Title", "Year", "imdbRating", "imdbVotes"]

    def __init__(
        self,
        master,
        bg_color,
        relief=tk.SUNKEN,
        side=tk.LEFT
    ):
        self.frame = tk.Frame(
            master=master,
            name="movieList",
            relief=relief,
            bg=bg_color
        )

        self.side = side
        self.movies = []
        self.add_frame()

    def add_frame(self):
        self.add_page_title("Movie List")
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
            height=3,
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

