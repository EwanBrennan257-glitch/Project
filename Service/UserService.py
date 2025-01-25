from DAO.UserDao import UserDAO
from Model.User import User
from Validation.UserValidation import PasswordLengthError,PasswordCharacterError



class UserService:

    def __init__(self, userValidation): # Initializes the service with UserDAO and validation
        # Create an instance of UserDAO to users data
        self.userDAO = UserDAO([])  # Passing an empty list to UserDAO constructor
        self.userValidation = userValidation

    def get_user_by_email(self,email):#gets a user by email from the DAO
        from app import select_user_by_email
        return select_user_by_email(email)


    # Creating the login function
    def signin(self, email, password):

        #gets the list of all users from UserDAO
        userListToCheckAgainst = self.userDAO.getAllUsers()

        # search through the list of users to find a matching model
        for user in userListToCheckAgainst:
            if user.email == email and user.password == password:
                return user

    def get_user(self, email, password):
        from app import select_user
        user=select_user(email, password)
        return user

    def create_user(self, firstname, lastname, email, password):#creates a new user
        from app import insert_user
        try:
            if self.userValidation.checkEmail(self.userDAO.getAllUsers(), email) and self.userValidation.checkPassword(password):
                user=User(firstname, lastname, email, password)#user class and passing firstname etc given by the signup process
                #self.userDAO.addusertolist(user)
                insert_user(user.firstname, user.lastname, user.email, user.password, is_admin=False, is_active=True)
                return (user, 'User Created')#message that pops up
            else:
                return (False, 'Invalid Email or Password')
        except PasswordLengthError as ple:#error for is length is too short
            return (False, str(ple))
        except PasswordCharacterError as pce:#error for if password does not have required speacial characters
            return (False, str(pce))
