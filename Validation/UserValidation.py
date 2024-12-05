import re
class PasswordLengthError(Exception):#custom exception for invalid password length
    pass

class PasswordCharacterError(Exception):#custom exception for invalid password characters missing speacial character
    pass
class UserValidation:#validates user input email and password
    def __init__(self):#intialises the user validation object
        pass

    def checkEmail(self, userList, email):
        if "@" not in email or "." not in email:#checks to see if the required speacial characters are in the email
            print("Email doesn't have the key characters '@' and '.'")#displays this message if the required characters are not present
            return False

        for user in userList:
            if user.email == email:#checks to see if the email is already in use by another user
                print("Email already has an account")
                return False

        return True

    def checkPassword(self, password):#checks to see if the password meets the length and character requirements
        pattern = re.compile(r'[^a-zA-Z0-9]')
        if len(password) < 10:#makes sure password is a certain length to be accepted
            raise PasswordLengthError("Password must be at least 10 characters long")
        if not pattern.search(password):#makes sure password has the required special characters
            raise PasswordCharacterError("Password must contain at least one special character")
        return True