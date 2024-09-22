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
        self.read_csv()
        self.create_page()
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

    def read_csv(self):
        movie_path = "data/imdb_top_250.csv"
        with open(movie_path, "r") as file:
            movie_dict = csv.DictReader(file, delimiter=";")
            for movie in movie_dict:
                self.movies.append(movie)

    def create_page(self):
        self.add_header_row()
        self.create_table()

    def add_header_row(self):
        for j, column in enumerate(MovieList.columns):
            if column != "imdbID":
                lbl = tk.Label(
                    self.frame,
                    text=str(column),
                    width=54,
                    height=2,
                    bg=COLORS.BLACK,
                    fg=COLORS.WHITE,
                    font=("Iosevka Custom", 10, "bold")
                )

                # Configuration width
                if column == "Id":
                    lbl.configure(
                        text="#",
                        width=4
                    )
                elif column == "Year":
                    lbl.configure(width=8)
                elif column == "imdbRating":
                    lbl.configure(text="Rating", width=8)
                elif column == "imdbVotes":
                    lbl.configure(text="# of Ratings", width=12)

                # Place in a grid
                if column == "imdbVotes":
                    lbl.grid(
                        row=1,
                        column=j,
                        sticky="we",
                        padx=(0, 10)
                    )
                else:
                    lbl.grid(
                        row=1,
                        column=j,
                        sticky="we",
                        padx=(0, 1)
                    )

    def create_table(self):
        for i, movie in enumerate(self.movies):
            for j, key in enumerate(MovieList.columns):
                name = "table_row_" + str(i) + str(j) + "_" + movie["imdbID"]
                if j == 0:
                    # render image
                    self.render_image(
                        movie,
                        i,
                        j,
                        name
                    )
                else:
                    # Print label
                    self.write_label(
                        movie,
                        i,
                        j,
                        key,
                        name
                    )

    def render_image(
        self,
        movie,
        i,
        j,
        name
    ):
        try:
            # Load the image
            load = Image.open("images/posters_small/" + movie["imdbID"] + ".jpg")
        except:
            load = Image.open("images/posters_small/no_image.jpg")
        finally:
            render = ImageTk.PhotoImage(load)
            lbl_img = tk.Label(
                self.frame,
                name=name,
                image=render,
                bg=COLORS.ORANGE
            )
            lbl_img.image = render
            lbl_img.grid(
                row=i+2,
                column=j,
                padx=(7, 0),
                sticky="we"
            )

    def write_label(
        self,
        movie,
        i,
        j,
        key,
        name
    ):
        lbl = tk.Label(
            self.frame,
            name=name,
            text=str(movie[key]),
            height=4,
            bg=COLORS.WHITE,
            fg=COLORS.BLACK,
            font=("Iosevka Custom", 10, "bold"),
            cursor="hand2"
        )

        # Configuration width
        if key == "Id":
            lbl.configure(width=4)
        elif key == "Title":
            lbl.configure(width=54)
        elif key == "Year":
            lbl.configure(width=8)
        elif key == "imdbRating":
            lbl.configure(width=8)
        elif key == "imdbVotes":
            lbl.configure(width=12)

        # Place in a grid
        if key == "imdbVotes":
            lbl.grid(
                row=i+2,
                column=j,
                sticky="we",
                padx=(0, 10)
            )
        else:
            lbl.grid(
                row=i+2,
                column=j,
                sticky="we",
                padx=(0, 1)
            )