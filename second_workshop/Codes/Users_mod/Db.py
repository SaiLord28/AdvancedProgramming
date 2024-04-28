from Users_mod.Users import User

class Database:
    def __init__(self):
        """
        Constructor Method  - creates instances of User class - gives values to the atributes

        """

        self.__pass_register_users = {}

#--------------------------------methods--------------------------------
    @staticmethod #This method is static cuz the Db has no instances, so it can be used in another class without instantiation
    def verify_login(self, mail, password, user: User):



        """
        verify_login method - verifies if the user exists and if the password is correct

        Args:
        mail: str - mail of user
        password: str - password of user

        """
        if mail in self.register_users:
            if self.register_users[mail].get_password == password:
                user.set_verification(True)
            else:
                user.set_verification(False)
        else:
            user.set_verification(False)

        user.login()

#---------

    @staticmethod #This method is static cuz the Db has no instances, so it can be used in another class without instantiation
    def verify_register(self, username, mail, password, rol_designer, user: User):
        """"
        register method - registers a new user

        Args:

        username: str - username of user
        mail: str - mail of user
        password: str - password of user
        rol_designer: bool - rol of user



        """
        if not mail in self.pass__register_users:
            new_user = user.register(username, mail, password, rol_designer)
            user.set_verification(True)
            self.pass__register_users[mail] = new_user

        else: 
             user.register(username, mail, password, rol_designer)
