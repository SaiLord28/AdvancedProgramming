from Users import User

class Database:

    """
    Database class - manages user registration and login

    Attributes:
        __pass_register_users (dict): A dictionary that stores user instances based on their mail addresses

    Methods:
        verify_login(mail: str, password: str, user: User) -> tuple: Verifies if the user exists and if the password is correct
        verify_register(username: str, mail: str, password: str, rol_designer: bool, user: User) -> None: Registers a new user
    """
    __pass_register_users = {}

#--------------------------------methods--------------------------------
    @staticmethod  # This method is static cuz the Db has no instances, so it can be used in another class without instantiation
    def verify_login(mail, password, user: User) -> tuple: 
        """
        verify_login method - verifies if the user exists and if the password is correct

        Args:
        mail: str - mail of user
        password: str - password of user
        user: User - instance of the User class

        Returns:
        tuple - a tuple containing a boolean value (aux) and the logged_user instance
        """

        if mail in Database.__pass_register_users:
            verify_user: User = Database.__pass_register_users[mail]

            if verify_user.get_password() == password:
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

    @staticmethod  # This method is static cuz the Db has no instances, so it can be used in another class without instantiation
    def verify_register(username: str, mail: str, password: str, rol_designer: bool, user: User) -> None:
        """
        verify_register method - registers a new user

        Args:
            username: str - username of user
            mail: str - mail of user
            password: str - password of user
            rol_designer: bool - rol of user
            user: User - instance of the User class

        Returns:
            None

        Raises:
            ValueError: If the user already exists in the database

        This method first checks if the provided mail already exists in the database. If it does not, it creates a new user instance with the provided username, mail, password, and role, and then adds the new user to the database. If the user already exists, it does not register the new user and raises a ValueError.
        """
        if not mail in Database.__pass_register_users:
            new_user = user.register(username, mail, password, rol_designer, True)
            user.set_verification(True)
            Database.__pass_register_users[mail] = new_user
            print(len(Database.__pass_register_users))
        else:
            raise ValueError("User already exists in the database")
