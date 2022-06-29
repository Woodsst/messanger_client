from client.login_window import Login


def main():
    login = Login('localhost:5000')
    login.run()


if __name__ == "__main__":
    main()
