import json
import time
import tkinter
from tkinter import ttk, StringVar

from threading import Thread
from client.base import TkinterBaseFrame
from client.grpc_connect import MessangerServerConnector
from client.status_code_handler import MessangerStatusCodeHandler
from client.messages_window import MessagesWindow


class MainWindow(TkinterBaseFrame, MessangerStatusCodeHandler):
    """Central window"""

    def __init__(self, server_address: str, token: str, name: str):

        TkinterBaseFrame.__init__(self, name)
        self.messanger_address = server_address
        self.token = token
        self.friend_list = []
        self.room_list = []
        self.field = StringVar()
        self.get_frame_constructing()
        self.select = None
        self.connect = MessangerServerConnector(
            server_address
        )

    def get_frame_constructing(self):
        """Show all frames"""

        self.friends_list()
        self.rooms_list()
        self.buttons()
        self.input_fields()

    def add_friend(self):
        """Actions when clicking the "Add friend" button"""

        get_field = self.field.get()
        result = self.connect.add_friend(
            friend_name=get_field,
            token=self.token
        )
        if self.friend_request_handler(result.status):
            self.friend_list.append(get_field)
            self.friends_list()

    def delete_friend(self):
        """Actions when clicking the "Remove friend" button"""

        result = self.connect.remove_friend(
            friend_name=self.select,
            token=self.token
        )
        if self.friend_remove_request_handler(result.status):
            self.friends_list()

    def create_room(self):
        """Actions when clicking the "Create room" button"""

        get_field = self.field.get()
        response = self.connect.create_room(
            room=get_field,
            token=self.token
        )
        if self.create_room_request_handler(response.status):
            self.rooms_list()

    def dialog_window(self):
        """Window for send messages to a room or other client"""

        if self.select is not None:
            window = MessagesWindow(self.select)
            window.run()

    def delete_room(self):
        """Actions when clicking the "Delete room" button"""

        if self.select is not None:
            select = self.select
            response = self.connect.delete_room(
                room=select,
                token=self.token
            )
            if self.delete_room_request_handler(response.status):
                self.rooms_list()

    def leave_room(self):
        """Actions when clicking the "leave room" button"""

        if self.select is not None:
            response = self.connect.leave_room(room=self.select,
                                               token=self.token)
            status = self.leave_room_request_handler(response.status)
            if status:
                self.rooms_list()

    def join_room(self):
        result = self.connect.join_room(room=self.field.get(),
                                        token=self.token)
        self.join_room_request_handler(result)

    def buttons(self):
        """Buttons collection"""

        join_room = ttk.Button(
            self.frame,
            width=11,
            text='join room',
            command=self.join_room
        )

        leave_room = ttk.Button(
            self.frame,
            width=11,
            text='leave room',
            command=self.leave_room
        )

        add_friend = ttk.Button(
            self.frame,
            width=11,
            text='Add friend',
            command=self.add_friend
        )

        delete_friend = ttk.Button(
            self.frame,
            width=11,
            text='Delete friend',
            command=self.delete_friend
        )

        create_room = ttk.Button(
            self.frame,
            width=11,
            text='Create room',
            command=self.create_room
        )

        delete_room = ttk.Button(
            self.frame,
            width=11,
            text='Delete room',
            command=self.delete_room
        )

        open_dialog = ttk.Button(
            self.frame,
            width=11,
            text='Open dialog',
            command=self.dialog_window
        )

        # Position all buttons
        open_dialog.grid(column=0, row=0)
        add_friend.grid(column=0, row=1)
        create_room.grid(column=0, row=2)
        delete_room.grid(column=0, row=3)
        delete_friend.grid(column=0, row=4)
        leave_room.grid(column=0, row=5)
        join_room.grid(column=0, row=6)

    def friends_list(self):
        """Friend List"""

        friend_list_var = tkinter.StringVar(
            value=self.friend_list)
        box = tkinter.Listbox(
            self.root,
            listvariable=friend_list_var,
            height=8,
            selectmode='single',
            width=13
        )

        def item_select(event):
            """Selecting an element for actions with it"""
            select_ = box.curselection()
            try:
                self.select = self.friend_list[select_[0]]
            except IndexError:
                pass

        box.bind('<<ListboxSelect>>', item_select)

        box.grid(column=1, row=0, padx=5)

    def rooms_list(self):
        """Room List"""

        room_list_var = tkinter.StringVar(
            value=self.room_list)
        box = tkinter.Listbox(
            self.root,
            listvariable=room_list_var,
            height=8,
            width=13
        )

        def item_select(event):
            """Selecting an element for actions with it"""
            select_ = box.curselection()
            try:
                self.select = self.room_list[select_[0]]
            except IndexError:
                pass

        box.bind('<<ListboxSelect>>', item_select)

        box.grid(column=1, row=1, padx=5, pady=5)

    def input_fields(self):

        field = ttk.Entry(self.frame,
                          width=12,
                          textvariable=self.field)

        field.grid(column=0, row=7, pady=5)

    def update(self):
        """Thread for update"""

        while True:
            data = self.connect.update_data(self.token)
            data_dict = json.loads(data.json_info)
            if self.friend_list != data_dict['info']["friend_list"]:
                self.friend_list = data_dict['info']["friend_list"]
                self.friends_list()
            elif self.room_list != data_dict['info']['room_list']:
                self.room_list = data_dict['info']['room_list']
                self.rooms_list()
            time.sleep(5)

    def run(self):
        """Run all thread and tkinter mainloop"""

        thread = Thread(target=self.update, daemon=True)
        thread.start()
        self.root.mainloop()
