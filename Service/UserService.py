from DAO.UserDao import UserDAO
from Model.User import User
# Creating a service layer for the model class this will handle business logic related to model
# this is an example of MVC (Model View Controller) Good programming practice for website development
class UserService:

    def __init__(self, userValidation):
        # Create an instance of UserDAO to handle model data
        self.userDAO = UserDAO([])  # Passing an empty list to UserDAO constructor
        self.userValidation = userValidation

    # Creating the login function
    def signin(self, email, password):

        # Retrieve the list of all users from UserDAO
        userListToCheckAgainst = self.userDAO.getAllUsers()

        # Iterate through the list of users to find a matching model
        for user in userListToCheckAgainst:
            if user.email == email and user.password == password:
                return user

    def create_user(self, firstname, lastname, email, password):

        if self.userValidation.checkEmail(self.userDAO.getAllUsers(), email) and self.userValidation.checkPassword(password):
            user=User(firstname, lastname, email, password)
            self.userDAO.addusertolist(user)
            return user
        else:
            print("Sign up failed. Please try again.")
