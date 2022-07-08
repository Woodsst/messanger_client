from client.login_window import Login


def main():
    login = Login('localhost:5000', 'localhost:5001', 'Login')
    login.run()


if __name__ == "__main__":
    main()
