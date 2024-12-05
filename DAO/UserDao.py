from Model.User import User
#to hold all users in global list
GLOBAL_USER_LIST=list()


# class to hold all users in memory, using this instead of database
class UserDAO:

    def __init__(self, user_list=None):
        # Initialize user_list as an empty list if None is provided
        self.user_list = GLOBAL_USER_LIST
        if user_list:
            self.user_list.extend(user_list)

    # This method grabs all users, and creates some if the list is empty
    def getAllUsers(self):
        if not self.user_list:  # Check if the list is empty
            # Create default users if list is empty
            user_manager = User("Admin", "Admin", "Admin@gmail.com", "pw1", True)
            user_employee = User("User", "User", "User@gmail.com", "pw2", False)

            self.user_list.append(user_manager)
            self.user_list.append(user_employee)

        return self.user_list

    # Add a new model to the list
    def addusertolist(self, user):
        self.user_list.append(user)

    def getManager(self):
        for user in self.user_list:
            if user.is_admin: return user

