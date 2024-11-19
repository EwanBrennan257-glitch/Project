import re
class PasswordLengthError(Exception):
    pass

class PasswordCharacterError(Exception):
    pass
class UserValidation:
    def __init__(self):
        pass

    def checkEmail(self, userList, email):
        if "@" not in email or "." not in email:
            print("Email doesn't have the key characters '@' and '.'")
            return False

        for user in userList:
            if user.email == email:
                print("Email already has an account")
                return False

        return True

    def checkPassword(self, password):
        pattern = re.compile(r'[^a-zA-Z0-9]')
        if len(password) < 10:
            raise PasswordLengthError("Password must be at least 10 characters long")
        if not pattern.search(password):
            raise PasswordCharacterError("Password must contain at least one special character")
        return True