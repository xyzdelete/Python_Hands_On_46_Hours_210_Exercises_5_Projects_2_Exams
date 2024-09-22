from widget.window.Window import Window
from widget.left_frame.LeftFrame import LeftFrame
from widget.button.Button import Button

if __name__ == "__main__":
    pass
    # Root Window
    root = Window("Movie Library - Tkinter")

    # LEFT FRAME
    left_frame = LeftFrame(root.window, "leftFrame")


    # RIGHT FRAME

    # Start Root Window -> mainloop()
    root.start_method()