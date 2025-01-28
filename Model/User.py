

class User:#represents a user and its required details
    #intialises the user with these details
    def __init__(self, firstname:str, lastname:str, email:str, password:str, is_admin:bool=False, is_active:bool=False):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.is_active = is_active


    #checks to seeif the user email is valid if it is already in use or not
    def checkEmail(userList, email):
        if "@" not in email or "." not in email:
            print("Email doesn't have the key characters '@' and '.'")
            return False
        #returns with the correct message to what the error is for the user
        for user in userList:
            if user.userEmail == email:
                print("Email already has an account")
                return False

        return True

    def __repr__(self):#string representation of the user and email
        return f"User(email='{self.email})"

    @staticmethod
    def getadmin():#returns the first admin user from the user list
        from DAO.UserDao import UserDAO
        for user in UserDAO().getAllUsers():
            if user.is_admin:
                return user

class UserRead(User):
    def __init__(self,id:int, firstname:str, lastname:str, email:str, password:str, is_admin:bool=False, is_active:bool=False):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.is_active = is_active