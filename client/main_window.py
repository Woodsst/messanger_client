import tkinter
from tkinter import ttk, StringVar

from client.base import TkinterBaseFrame
from client.grpc_connect import MessangerServerConnector
from client.status_code_handler import MessangerStatusCodeHandler


class MainWindow(TkinterBaseFrame, MessangerStatusCodeHandler):
    """Central window"""

    def __init__(self, server_address: str, token: str):

        TkinterBaseFrame.__init__(self)
        self.messanger_address = server_address
        self.token = token
        self.friend_list = ['user_1', 'user_2']
        self.room_list = ['room_1', 'room_2']
        self.field = StringVar()
        self.get_frame_constructing()
        self.connect = MessangerServerConnector(
            server_address
        )

    def get_frame_constructing(self):
        """Get all frames"""

        self.friends_list()
        self.rooms_list()
        self.buttons()
        self.input_fields()

    def add_friend(self):
        get_field = self.field.get()
        result = self.connect.add_friend(
            get_field,
            self.token
        )
        status = self.result_handler(result.status)
        if status:
            self.friend_list.append(get_field)
            self.friends_list()

    def delete_friend(self):
        pass

    def create_room(self):
        pass

    def dialog_window(self):
        pass

    def delete_room(self):
        pass

    def buttons(self):
        """Buttons collection"""

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
                print(self.friend_list[select_[0]])
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
                print(self.room_list[select_[0]])
            except IndexError:
                pass

        box.bind('<<ListboxSelect>>', item_select)

        box.grid(column=1, row=1, padx=5, pady=5)

    def input_fields(self):

        field = ttk.Entry(self.frame,
                          width=12,
                          textvariable=self.field)

        field.grid(column=0, row=5, pady=5)
