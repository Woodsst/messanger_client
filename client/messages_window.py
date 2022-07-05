import tkinter
from tkinter import ttk

from client.base import TkinterToplevelFrame


class MessagesWindow(TkinterToplevelFrame):
    """Window to messages"""

    def __init__(self, name: str):
        TkinterToplevelFrame.__init__(self)
        self.root.title(name)

    def get_frame_constructing(self):
        """Constructing frames"""

        self.buttons()
        self.text_field()
        self.messanger_field()

    def text_field(self):
        """Text input field for sending"""

        messages = tkinter.Text(self.frame,
                                width=50,
                                height=3)
        messages.grid(column=0, row=1)

    def messanger_field(self):
        """Messages field"""

        messages = tkinter.Text(self.frame,
                                width=50,
                                height=25)
        messages.grid(column=0, row=0, pady=5)

    def buttons(self):
        """buttons"""

        ok = ttk.Button(self.frame, width=10, text='Send',
                        command=self.send)
        ok.grid(column=0, row=2, pady=5)

    def send(self):
        """Command to send a message"""
        pass
