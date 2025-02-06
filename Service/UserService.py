
from Model.User import User
from Validation.UserValidation import PasswordLengthError,PasswordCharacterError
from db import select_user_by_email, insert_user, select_user

class UserService:

    def __init__(self, userValidation): # Initializes the service
        self.userValidation = userValidation

    def get_user_by_email(self,email):
        return select_user_by_email(email)

    def get_user(self, email, password):
        user=select_user(email, password)
        return user

    def create_user(self, firstname, lastname, email, password):#creates a new user
        try:
            if self.userValidation.checkEmail(email) and self.userValidation.checkPassword(password):
                user=User(firstname, lastname, email, password)#user class and passing firstname etc given by the signup process

                insert_user(user.firstname, user.lastname, user.email, user.password, is_admin=False, is_active=True)
                return (user, 'User Created')#message that pops up
            else:
                return (False, 'Invalid Email or Password')
        except PasswordLengthError as ple:#error for is length is too short
            return (False, str(ple))
        except PasswordCharacterError as pce:#error for if password does not have required speacial characters
            return (False, str(pce))
