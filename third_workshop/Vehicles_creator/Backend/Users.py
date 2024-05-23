import time
from Vehicles import Vehicle
#====================================== USER  CLASS =====================================

class User:
    """
    User class - represents a user in the system

    Attributes:
        username (str): The username of the user
        mail (str): The mail address of the user
        password (str): The password of the user
        rol_designer (bool): A boolean value indicating if the user is a designer role

    Methods:
        __init__(self, username: str, mail: str, password: str, rol_designer: bool) -> None: Initializes a new User instance
        register(self, username: str, mail: str, password: str, rol_designer: bool, db: Database) -> None: Registers the user in the database
        get_password(self) -> str: Retrieves the user's password
        set_verification(self, verified: bool) -> None: Sets the user's verification status
    """

    def __init__(self, username: str, mail: str, password: str, rol_designer: bool) -> None:
        """
        Initializes a new User instance

        Args:
            username (str): The username of the user
            mail (str): The mail address of the user
            password (str): The password of the user
            rol_designer (bool): A boolean value indicating if the user is a designer role
        """
        self._username = username
        self._mail = mail
        self._password = password
        self._rol_designer = rol_designer
        self._verified = False
#---------------------------------- methods --------------------------------

    def register(self, username, mail, password, rol_designer, verification):
         
         """
    register method - registers a new user

    Args:
        username (str): username of user
        mail (str): mail of user
        password (str): password of user
        rol_designer (bool): rol of user
        verification (bool): verification of user

    Returns:
        User: A new user

    If the verification is True, the method checks if the user is a designer role. If so, it creates a new Designer instance. If not, it creates a new User instance. It then prints a registration confirmation message and returns the new user. If the verification is False, it prints a message indicating that the mail is already registered and returns None.
    """
         if verification == True:
              
              if rol_designer == True:
                user = Designer(username, mail, password, rol_designer)
                

              elif rol_designer == False:  
                user = User(username, mail, password, rol_designer)
            
              print("===========================================================")
              print ("The user has been registered, now you can login")
              time.sleep(2.2)
              return user
         else:
              print("===========================================================")
              print("The mail is already registered, please try again")
              time.sleep(2.2)
         self._verification = False

#--------------

    def login(self) -> None:
          
          """
          login method - logs in a user

          Args: 

          mail: str - mail of user
          password: str - password of user
          
          """

          if self._verification == True:
            print("===========================================================")
            print("Succesfull log in")
            time.sleep(1.5)
            return True
          else:
               print("===========================================================")
               print("E-mail or password incorrect") 
               time.sleep(1.5)
               return False 

#---------------------------- Getters and setters -----------------------------------------

    def get_username(self) -> str:
      """
      get_username method - gets the username of the user

      Returns:
      str: The username of the user

      This method retrieves the username of the user. It does not take any parameters and simply returns the stored username attribute of the user.
      """
      return self._username

#--------------

    def get_password(self) -> str:
      """
    get_password method - gets the password of the user

    Returns:
    str: The password of the user
    """
      return self._password

#--------------

    def get_rol_designer(self) -> bool:
      """
    get_rol_designer method - gets the designer role of the user

    Returns:
    bool: True if the user is a designer role, False otherwise
    """
      return self._rol_designer
#--------------------
    def set_verification(self, new_verification: bool) -> None:
         
         """
    set_verification method - sets the verification of the user

    Args:
        new_verification (bool): The new verification status for the user

    Returns:
        None: This method does not return any value

    This method sets the verification status of the user. It takes a boolean parameter, new_verification, which represents the new verification status for the user. The method then updates the user's verification status with the new value.
    """

         self._verification = new_verification

        
#====================================== DESIGNER CLASS =====================================

class Designer(User): #Son class



    def __init__(self, username: str, mail:str , password:str , rol_designer:bool):
      """
    constructor method - creates instance of Designer class - gives values to the attributes

    Args:
        username (str): username of user
        mail (str): mail of user
        password (str): password of user
        rol_designer (bool): rol of user
        verification (bool): verification of user
        vehicles_list (list): vehicles of designer

    Class attributes:
        All of them are private. __indicates -> private

    This method initializes a new Designer instance by setting the provided attributes. It takes the following parameters:
        - username (str): The username of the user
        - mail (str): The mail address of the user
        - password (str): The password of the user
        - rol_designer (bool): A boolean value indicating if the user is a designer role
        - verification (bool): A boolean value indicating if the user is verified
        - vehicles_list (list): A list of vehicles associated with the designer

    The method then calls the constructor of the superclass (User) using the `super()` function, passing the provided attributes as arguments. Finally, it initializes the `__vehicles_list` attribute as an empty list.
    """
      super().__init__(username, mail, password, rol_designer)
      self.__vehicles_list = [] 

#---------------------------------- getters --------------------------------

    def get_vehicles_list(self) -> list:
      """
    get_vehicles_list method - gets the vehicles list of the designer

    Returns:
    list: The vehicles list of the designer
    """
      return self.__vehicles_list

# -----------------------------------methods --------------------------------
    def upload_v(self, vehicle: 'Vehicle') -> None:
      """
    upload_v method - uploads a new vehicle to the vehicles list of the designer
   
    Args:
        vehicle: 'Vehicle' - vehicle to be added to the vehicles list
        
    Returns:
        None: This method does not return any value
        
    This method adds a new vehicle to the vehicles list of the designer. It takes a single parameter, vehicle, which is an instance of the Vehicle class. The method then appends the provided vehicle to the designer's vehicles list using the `append()` method.
    """
      self.__vehicles_list.append(vehicle)
    

