import oop
class User:
    def __init__(self, _name, _surname, _username, _password):
        # attribute
        self.name = _name
        self.surname = _surname
        self.username = _username
        self.password = _password

    def showUserData(self):
        print(f"Name : {self.name}, Surname : {self.surname}, Username : {self.username}")

    def LogInUser(self):
        username = input("Username: ")
        password = input("Password: ")
        if username == self.username and password == self.password:
            print(f"Hi, {self.username}.")
        else:
            print("Inorrect data. ")

