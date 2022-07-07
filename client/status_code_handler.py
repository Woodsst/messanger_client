from tkinter import messagebox

from client.authorization_api.authorization_pb2 import RegisterCodeResult, LoginCodeResult
from client.messanger_api.messanger_pb2 import CodeResult


class LoginStatusCodeHandler:
    """A class for handling response code statuses"""

    @staticmethod
    def registration_result_handler(result: RegisterCodeResult):
        """Handle response server to registration request"""

        if result == RegisterCodeResult.Value('RCR_ok'):
            messagebox.showinfo(message='Thank you for registering',
                                title='Registration')

        elif result == RegisterCodeResult.Value('RCR_undefined'):
            messagebox.showerror(message='Wrong username or password'
                                 , title='Registration')

        elif result == RegisterCodeResult.Value('RCR_already_exist'):
            messagebox.showerror(message='User already exists',
                                 title='Registration')

        else:
            messagebox.showerror(message='Unknown error',
                                 title='Registration')

    @staticmethod
    def authorization_result_handler(result: RegisterCodeResult) -> bool:
        """Handle response server to login request"""

        if result == LoginCodeResult.Value('LCR_ok'):
            messagebox.showinfo(message='Hello!',
                                title='Registration')
            return True

        elif result == LoginCodeResult.Value('LCR_undefined'):
            messagebox.showerror(message='Wrong username or password'
                                 , title='Registration')

        elif result == LoginCodeResult.Value('LCR_unknown_user'):
            messagebox.showerror(message="User not found",
                                 title='Registration')

        else:
            messagebox.showerror(message='Unknown error',
                                 title='Registration')
        return False


class MessangerStatusCodeHandler:
    """A class for handling response code statuses"""

    @staticmethod
    def friend_request_handler(result: CodeResult) -> bool:
        """Handle response server to add friend request"""

        if result == CodeResult.Value('ok'):
            messagebox.showinfo(message='Friend added in your friend list',
                                title='Friend add')
            return True

        elif result == CodeResult.Value('bad'):
            messagebox.showerror(message='Friend in friend list or does not exist',
                                 title='Friend add')

        else:
            messagebox.showerror(message='Unknown error',
                                 title='Friend add')

    @staticmethod
    def friend_remove_request_handler(result: CodeResult) -> bool:
        """Handle response server to remove friend request"""

        if result == CodeResult.Value('ok'):
            messagebox.showinfo(message='Friend remove in your friend list',
                                title='Friend remove')
            return True

        elif result == CodeResult.Value('bad'):
            messagebox.showerror(message='Friend not in friend list or does not exist',
                                 title='Friend remove')

        else:
            messagebox.showerror(message='Unknown error',
                                 title='Friend remove')

    @staticmethod
    def create_room_request_handler(result: CodeResult) -> bool:
        """Handle response server to create room request"""

        if result == CodeResult.Value('ok'):
            messagebox.showinfo(message='Create room',
                                title='Room')
            return True

        elif result == CodeResult.Value('bad'):
            messagebox.showerror(message='Create room error',
                                 title='Room')

        else:
            messagebox.showerror(message='Unknown error',
                                 title='Room')

    @staticmethod
    def leave_room_request_handler(result: CodeResult) -> bool:
        """Handle response server to leave room request"""

        if result == CodeResult.Value('ok'):
            messagebox.showinfo(message='leave room',
                                title='Room')
            return True

        elif result == CodeResult.Value('bad'):
            messagebox.showerror(message='Room error',
                                 title='Room')

        else:
            messagebox.showerror(message='Unknown error',
                                 title='Room')

    @staticmethod
    def delete_room_request_handler(result: CodeResult) -> bool:
        """Handle response server to delete room request"""

        if result == CodeResult.Value('ok'):
            messagebox.showinfo(message='Room delete',
                                title='Room')
            return True

        elif result == CodeResult.Value('bad'):
            messagebox.showerror(message='Room error',
                                 title='Room')

        else:
            messagebox.showerror(message='Unknown error',
                                 title='Room')

    @staticmethod
    def join_room_request_handler(result: CodeResult) -> bool:
        """Handle response server to join room request"""

        if result == CodeResult.Value('ok'):
            messagebox.showinfo(message='Room join',
                                title='Room')
            return True

        elif result == CodeResult.Value('bad'):
            messagebox.showerror(message='Room error',
                                 title='Room')

        else:
            messagebox.showerror(message='Unknown error',
                                 title='Room')
