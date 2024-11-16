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
    def login(self):

        # Retrieve the list of all users from UserDAO
        userListToCheckAgainst = self.userDAO.getAllUsers()

        # Prompt the model for email and password input
        email = input("Enter your Email: ")
        password = input("Enter your password: ")

        # Flag to check if the model is found
        user_found = False

        # Iterate through the list of users to find a matching model
        for user in userListToCheckAgainst:
            if user.userEmail == email and user.userPassword == password:
                user_found = True
                if user.isManager:
                    print("Hello Manager, Welcome Back")
                else:
                    print("Hello Employee, Welcome Back")
                break  # Exit the loop once a model is found

        # If no matching model is found, display an error message
        if not user_found:
            print("Invalid username or password. Try again.")
            self.login()

    def create_user(self, firstname, lastname, email, password):

        if self.userValidation.checkEmail(self.userDAO.getAllUsers(), email) and self.userValidation.checkPassword(password):
            user=User(firstname, lastname, email, password)
            self.userDAO.addusertolist(user)
            return user
        else:
            print("Sign up failed. Please try again.")
