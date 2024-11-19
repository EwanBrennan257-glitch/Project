import re


class User:
    def __init__(self, firstname:str, lastname:str, email:str, password:str, is_admin:bool=False):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.is_admin = is_admin



    def checkEmail(userList, email):
        if "@" not in email or "." not in email:
            print("Email doesn't have the key characters '@' and '.'")
            return False

        for user in userList:
            if user.userEmail == email:
                print("Email already has an account")
                return False

        return True

    def __repr__(self):
        return f"User(email='{self.email})"