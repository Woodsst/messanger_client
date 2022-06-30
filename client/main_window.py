import tkinter
from tkinter import ttk

from client.base import TkinterBaseFrame


class MainWindow(TkinterBaseFrame):
    """Central window"""

    def __init__(self, server_address: str):

        TkinterBaseFrame.__init__(self)
        self.messanger_address = server_address
        self.friend_list = ['user_1', 'user_2']
        self.room_list = ['room_1', 'room_2']
        self.get_frame_constructing()

    def get_frame_constructing(self):
        """Get all frames"""

        self.friends_list()
        self.rooms_list()
        self.buttons()

    def add_friend(self):
        pass

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

        box.grid(column=1, row=0, padx=5, pady=5)

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
