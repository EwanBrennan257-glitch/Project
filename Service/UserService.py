from DAO.UserDao import UserDAO
from Model.User import User
from Validation.UserValidation import PasswordLengthError,PasswordCharacterError
# Creating a service layer for the model class this will handle business logic related to model
# this is an example of MVC (Model View Controller) Good programming practice for website development
class UserService:

    def __init__(self, userValidation):
        # Create an instance of UserDAO to handle model data
        self.userDAO = UserDAO([])  # Passing an empty list to UserDAO constructor
        self.userValidation = userValidation

    def get_user_by_email(self,email):
        userListToCheckAgainst = self.userDAO.getAllUsers()

        # Iterate through the list of users to find a matching model
        for user in userListToCheckAgainst:
            if user.email == email:
                return user
    # Creating the login function
    def signin(self, email, password):

        # Retrieve the list of all users from UserDAO
        userListToCheckAgainst = self.userDAO.getAllUsers()

        # Iterate through the list of users to find a matching model
        for user in userListToCheckAgainst:
            if user.email == email and user.password == password:
                return user

    def create_user(self, firstname, lastname, email, password):
        try:
            if self.userValidation.checkEmail(self.userDAO.getAllUsers(), email) and self.userValidation.checkPassword(password):
                user=User(firstname, lastname, email, password)
                self.userDAO.addusertolist(user)
                return (user, 'User Created')
            else:
                return (False, 'Invalid Email or Password')
        except PasswordLengthError as ple:
            return (False, str(ple))
        except PasswordCharacterError as pce:
            return (False, str(pce))
