from tkinter import StringVar, ttk, messagebox
from client.base import TkinterBaseFrame
from client.grpc_connect import AuthorizationServerConnector
from client.authorization_pb2 import RegisterCodeResult, LoginCodeResult
from client.main_window import MainWindow


class Login(TkinterBaseFrame):
    """Login window"""

    def __init__(self, address_authorization_server: str,
                 address_messanger_server: str):
        TkinterBaseFrame.__init__(self)
        self.messanger_address = address_messanger_server
        self.server_address = address_authorization_server
        self.root.wm_title("Login")
        self.username = StringVar()
        self.password = StringVar()
        self.get_frame_constructing()
        self.connect = AuthorizationServerConnector(
            self.server_address)

    def get_frame_constructing(self):
        """Method that collects all the parts of the frame"""

        self.input_fields()
        self.labels()
        self.buttons()

    def labels(self):
        """All labels stings"""

        username = ttk.Label(self.frame, text='Username')
        password = ttk.Label(self.frame, text='Password')

        username.grid(column=0, row=0, padx=5)
        password.grid(column=0, row=2, padx=5)

    def input_fields(self):
        """All input fields"""

        username = ttk.Entry(self.frame, width=20, textvariable=self.username)
        password = ttk.Entry(self.frame, width=20, textvariable=self.password, show='*')

        username.grid(column=1, row=0, padx=5, pady=6)
        password.grid(column=1, row=2, padx=5)

    def buttons(self):
        """All buttons"""

        ok_button = ttk.Button(self.frame, width=10, text='Ok', command=self.login)
        ok_button.grid(column=0, row=3, pady=3)

        registration_button = ttk.Button(self.frame, width=10,
                                         text='Registration', command=self.registration)
        registration_button.grid(column=1, row=3, pady=5, padx=5, sticky='e')

    def registration(self):
        """Registration request"""

        result = self.connect.registration_request(self.username.get(), self.password.get())
        self.registration_result_handler(result.code)

    def login(self):
        """login request"""

        result = self.connect.authorization_request(self.username.get(), self.password.get())
        if self.authorization_result_handler(result.code):
            self.connect.connection_close()
            self.open_main_app(result.token)

    def open_main_app(self, token: str):
        """Destroy login window and run main window"""

        self.root.destroy()
        main = MainWindow(self.messanger_address, token)
        main.run()

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
