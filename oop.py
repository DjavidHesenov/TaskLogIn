# base class

class UserX:
    def __init__(self, _name, _surname):
        self.name = _name
        self.surname = _surname

    def showData(self):
        print(f"{self.name} / {self.surname}")


# derived class
class AdminUser(UserX):
    def __init__(self, _ad, _soyad, role, _password):
        UserX.__init__(self, _ad, _soyad)
        self.role = role
        self.password = _password
    def showData(self):
        print(f"{self.name} / {self.surname} / {self.role}")

    def showData(self, _permissions=None):
        if _permissions is not None:
            print(f"{self.name} is an admin and he has permissions to {_permissions}")
        else:
            print(f"{self.name} / {self.surname} / {self.role}")


admin = AdminUser("Samir", "Hesenov", "Editor", "12345678")

