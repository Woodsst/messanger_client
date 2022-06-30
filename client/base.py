import abc
from tkinter import Tk, ttk
from abc import ABC

import grpc

from client.authorization_pb2_grpc import GreeterStub


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


class ABCConnectGRPC(ABC):
    """abstract base to connect gRPC"""

    def __init__(self, server_address: str):
        self.authorization_server = server_address
        self.channel = grpc.insecure_channel(self.authorization_server)
        self.stub = GreeterStub(self.channel)

    @abc.abstractmethod
    def connection_close(self):
        """Method to close connecting"""
        raise NotImplementedError


class ConnectGRPC(ABCConnectGRPC):
    """Base for connet to gRPC server"""

    def connection_close(self):
        """Method to close connect after ended all operations"""

        self.channel.close()
