from Users import User

class Database:
    __pass_register_users = {}

#--------------------------------methods--------------------------------
    @staticmethod #This method is static cuz the Db has no instances, so it can be used in another class without instantiation
    def verify_login(mail, password, user: User):

        """
        verify_login method - verifies if the user exists and if the password is correct

        Args:
        mail: str - mail of user
        password: str - password of user

        """

        logged_user = User(None, None, None, None)
        
        if mail in Database.__pass_register_users:

            if Database.__pass_register_users[mail].get_password == password:
                user.set_verification(True)
                aux = True
                logged_user = Database.__pass_register_users[mail]
            else:
                user.set_verification(False)
                aux = False
        else:
            user.set_verification(False)
            aux = False

        user.login()
        return aux, logged_user


#---------

    @staticmethod #This method is static cuz the Db has no instances, so it can be used in another class without instantiation
    def verify_register(username, mail, password, rol_designer, user: User):
        """"
        register method - registers a new user

        Args:

        username: str - username of user
        mail: str - mail of user
        password: str - password of user
        rol_designer: bool - rol of user



        """
        if not mail in Database.__pass_register_users:
            new_user = user.register(username, mail, password, rol_designer)
            user.set_verification(True)
            Database.__pass_register_users[mail] = new_user

        else: 
             user.register(username, mail, password, rol_designer)
