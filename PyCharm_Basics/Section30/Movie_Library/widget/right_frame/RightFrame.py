import tkinter as tk
from data.colors import COLORS

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
        if page_name == "home":
            # Add home page
            pass
        elif page_name == "movieList":
            # Add movie list page
            pass
        elif page_name == "movieDetail":
            # Add movie detail page
            pass

