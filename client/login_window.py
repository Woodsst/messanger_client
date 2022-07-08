from tkinter import StringVar, ttk
from client.base import TkinterBaseFrame
from client.grpc_connect import AuthorizationServerConnector
from client.main_window import MainWindow
from client.status_code_handler import LoginStatusCodeHandler


class Login(TkinterBaseFrame, LoginStatusCodeHandler):
    """Login window"""

    def __init__(self, address_authorization_server: str,
                 address_messanger_server: str, name: str):

        TkinterBaseFrame.__init__(self, name)
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
        main = MainWindow(self.messanger_address, token, self.username.get())
        main.run()
