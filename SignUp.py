from Tutorial_4.userservice.UserService import UserService
from Tutorial_4.validation.UserValidation import UserValidation

userValidation = UserValidation

userService = UserService(userValidation)

userService.signUp()