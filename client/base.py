from tkinter import Tk, ttk


class TkinterBaseFrame:
    """Base for all frames"""

    def __init__(self):
        self.root = Tk()
        self.frame = ttk.Frame(self.root, padding=5)
        self.frame.grid()

    def run(self):
        """Start show app"""
        self.root.mainloop()
