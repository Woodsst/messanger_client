import abc
from tkinter import Tk, ttk
from abc import ABC


class FramesConstruct(ABC):
    """ABC class for constructing windows and frames in tkinter"""

    @abc.abstractmethod
    def run(self):
        """Method to start run main loop tkinter"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_frame_constructing(self):
        """Method to collecting all construction frames"""
        raise NotImplementedError


class TkinterBaseFrame(FramesConstruct):
    """Base for all frames"""

    def __init__(self):
        self.root = Tk()
        self.frame = ttk.Frame(self.root, padding=5)
        self.frame.grid()

    def run(self):
        """Start show app"""
        self.root.mainloop()

    def get_frame_constructing(self):
        """Constructing frames"""
        pass
