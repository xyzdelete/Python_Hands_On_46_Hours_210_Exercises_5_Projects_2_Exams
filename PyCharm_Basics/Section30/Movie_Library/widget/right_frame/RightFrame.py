import tkinter as tk
from data.colors import COLORS
from page.home.Home import Home
from page.movie_list.MovieList import MovieList
from page.movie_detail.MovieDetail import MovieDetail

class RightFrame:
    """
    It will hold the pages on the right frame.
    """

    # Class attribute
    bg_color = COLORS.ORANGE

    def __init__(
        self,
        window,
        name,
        relief=tk.SUNKEN,
        side=tk.LEFT,
    ):
        self.frame = tk.Frame(
            master=window,
            name=name,
            relief=relief,
            bg=RightFrame.bg_color
        )

        self.side = side
        self.add_frame()

    def add_frame(self):
        # Frame content
        self.frame_content()
        self.frame.pack(
            side=self.side,
            fill=tk.BOTH,
            expand=True,
        )

    def frame_content(
            self,
            page_name="home"
    ):
        try:
            incoming_frame = self.frame
        except:
            incoming_frame = self
        finally:
            if page_name == "home":
                # Add home page
                Home(
                    incoming_frame,
                    RightFrame.bg_color
                )
            elif page_name == "movieList":
                # Add movie list page
                MovieList(
                    incoming_frame,
                    RightFrame.bg_color
                )
            elif page_name == "movieDetail":
                # Add movie detail page
                MovieDetail(
                    incoming_frame,
                    RightFrame.bg_color
                )

    # Static method -> Class Method
    def destroy_children(frame):
        # Destroy the children
        for child in frame.winfo_children():
            child.destroy()
