import abc
from tkinter import Tk, ttk, Toplevel
from abc import ABC

import grpc


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
        self.root.resizable(width=False, height=False)

    def run(self):
        """Start show app"""
        self.root.mainloop()

    def get_frame_constructing(self):
        """Constructing frames"""
        pass


class ABCConnectGRPC(ABC):
    """abstract base to connect gRPC"""

    def __init__(self, server_address: str):
        self.server = server_address
        self.channel = grpc.insecure_channel(self.server)

    @abc.abstractmethod
    def connection_close(self):
        """Method to close connecting"""
        raise NotImplementedError


class ConnectGRPC(ABCConnectGRPC):
    """Base for connect to gRPC server"""

    def connection_close(self):
        """Method to close connect after ended all operations"""

        self.channel.close()


class TkinterToplevelFrame(FramesConstruct):
    """Class for create secondary windows"""

    def __init__(self):
        self.root = Toplevel()
        self.frame = ttk.Frame(self.root, padding=5)
        self.root.resizable(width=False, height=False)

    def get_frame_constructing(self):
        """Constructing frames"""
        pass

    def run(self):
        self.frame.grid()
        self.get_frame_constructing()
