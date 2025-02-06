

class User:#represents a user and its required details
    #intialises the user with these details
    def __init__(self, firstname:str, lastname:str, email:str, password:str, is_admin:bool=False, is_active:bool=False):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.is_active = is_active

    def __repr__(self):#string representation of the user and email
        return f"User(email='{self.email})"

class UserRead(User):
    def __init__(self,id:int, firstname:str, lastname:str, email:str, password:str, is_admin:bool=False, is_active:bool=False):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.is_active = is_active