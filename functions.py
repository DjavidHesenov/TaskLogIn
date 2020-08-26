from lib import User
from db import db
import oop
def getUserData():
    i_name = input("Name :")
    i_surname = input("Surname :")
    i_username = input("Username :")
    i_password = input("Password :")
    return [i_name, i_surname, i_username, i_password]

def addUserToDb():
    db.append(User(*getUserData()))

def userRegister():
    userCount = int(input("Type user count :"))
    for count in range(userCount):
        count += 1
        print(f"Add {count}. user data")
        addUserToDb()
        executeOrders()

def showAllUsers():
    for user in db:
        user.showUserData()

def executeOrders():
    print("Type 1 to register")
    print("Type 2 to show users")
    print("Type 3 to log in")
    order = int(input("Choose your order"))
    if order == 1:
        userRegister()
    elif order == 2:
        showAllUsers()
    elif order == 3:
        question = input("Are you user with special role? Print 'Yes' or 'No' ")
        if question == "No":
            for user in db:
                user.LogInUser()
        elif question == "Yes":
            SpecialRole = input("Insert Role: ")
            SpecialPassword = input("Insert Password: ")
            if SpecialRole == oop.admin.role and SpecialPassword == oop.admin.password:
                oop.admin.showData()


executeOrders()