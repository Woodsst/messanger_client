from tkinter import Tk, StringVar, ttk


class Login:
    """Login window"""

    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Login")
        self.frame = ttk.Frame(self.root, padding=5)
        self.frame.grid()
        self.username = StringVar()
        self.password = StringVar()
        self.get_frame_constructing()

    def run(self):
        """Start show app"""
        self.root.mainloop()

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
        """Registration form"""
        pass

    def login(self):
        """Command to send credentials to the server"""
        pass

