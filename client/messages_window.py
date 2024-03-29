import json
import time
import tkinter
from threading import Thread
from tkinter import ttk
from typing import Union

from client.base import TkinterToplevelFrame
from client.grpc_connect import MessangerServerConnector


class MessagesWindow(TkinterToplevelFrame):
    """Window to messages"""

    def __init__(self, name: str, server_address: str,
                 credentials: str):
        TkinterToplevelFrame.__init__(self)
        self.root.title(name)
        self.connect = MessangerServerConnector(
            server_address
        )
        self.messages: Union[tkinter.Text, None] = None
        self.messanger_window: Union[tkinter.Text, None] = None
        self.token = credentials
        self.addressee = name
        self.last_message_time = 0

    def get_frame_constructing(self):
        """Constructing frames"""

        self.buttons()
        self.text_field()
        self.messanger_field()

    def run(self):
        TkinterToplevelFrame.run(self)
        thread = Thread(target=self.update_thread, daemon=True)
        thread.start()

    def text_field(self):
        """Text input field for sending"""

        self.messages = tkinter.Text(self.frame,
                                     width=50,
                                     height=3)
        self.messages.grid(column=0, row=1)

    def messanger_field(self):
        """Messages field"""

        self.messanger_window = tkinter.Text(self.frame,
                                             width=50,
                                             height=25)
        self.messanger_window.grid(column=0, row=0, pady=5)

    def buttons(self):
        """Buttons"""

        ok = ttk.Button(self.frame, width=10, text='Send',
                        command=self.send)
        ok.grid(column=0, row=2, pady=5)

    def send(self):
        """Command to send a message"""

        self.connect.send_message(
            message=self.messages.get(index1=1.0, index2='end'),
            address=self.addressee,
            token=self.token)

        self.messanger_window.insert('1.0',
                                     f'{time.ctime(time.time())}\n'
                                     f'{self.messages.get(index1=1.0, index2="end")}\n')

        self.last_message_time = int(time.time())

    def new_message(self, messages: list):
        """Display new message"""

        for message in messages:
            self.messanger_window.insert('1.0',
                                         f'{time.ctime(time.time())}\n'
                                         f'{message.get("message")}\n')

        self.last_message_time = int(time.time())

    def update_thread(self):

        while True:
            update = self.connect.update_messages(self.token,
                                                  self.addressee,
                                                  self.last_message_time)
            self.new_message(json.loads(update.json_info))
            time.sleep(5)
