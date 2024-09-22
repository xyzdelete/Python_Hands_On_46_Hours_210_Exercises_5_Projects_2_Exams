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
        self.add_content()
        self.add_page_title("Movie Detail")
        self.frame.pack(
            side=self.side,
            fill=tk.BOTH,
            expand=True
        )

    def add_page_title(
        self,
        title
    ):
        if self.imdbID != None:
            lbl = tk.Label(
                self.frame,
                text=self.movie["Title"],
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
        else:
            lbl = tk.Label(
                self.frame,
                text=title,
                height=2,
                bg=COLORS.BLACK,
                fg=COLORS.WHITE,
                font=("Iosevka Custom", 12, "bold")
            )
            lbl.pack(
                fill=tk.BOTH,
                padx=(1, 0)
            )



    def add_content(self):
        if self.imdbID != None:
            self.render_image()
            self.get_movie()
            self.render_keys()
            self.render_values()
        else:
            pass

    def render_image(self):
        try:
            # Load the image
            load = Image.open("images/posters_large/" + str(self.imdbID) + ".jpg")
        except:
            load = Image.open("images/posters_large/no_image.jpg")
        finally:
            render = ImageTk.PhotoImage(load)
            lbl_img = tk.Label(
                self.frame,
                image=render,
                bg=COLORS.ORANGE
            )
            lbl_img.image = render
            lbl_img.grid(
                row=1,
                column=0,
                columnspan=2,
                pady=(0, 10)
            )

    def get_movie(self):
        for m in self.movies:
            if m["imdbID"] == self.imdbID:
                self.movie = m
                break

    def render_keys(self):
        for i, key in enumerate(self.movie.keys()):
            txt = str(key)
            lbl = tk.Label(
                self.frame,
                text=txt,
                height=2,
                width=12,
                anchor="w"
            )

            self.fill_bg(lbl, i)

            lbl.grid(
                row=i+2,
                column=0,
                padx=(10, 1)
            )

    def fill_bg(
        self,
        widget,
        i
    ):
        if i % 2 == 1:
            widget.configure(bg=COLORS.LIST_ODD_LINE)
        else:
            widget.configure(bg=COLORS.LIST_EVEN_LINE)

    def render_values(self):
        for i, value in enumerate(self.movie.values()):
            txt = str(value)
            lbl = tk.Label(
                self.frame,
                text=txt,
                height=2,
                width=96,
                anchor="w"
            )

            self.fill_bg(lbl, i)

            lbl.grid(
                row=i+2,
                column=1,
                padx=(0, 8)
            )