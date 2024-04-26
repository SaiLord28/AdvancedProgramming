#====================================== USER  CLASS =====================================

class User():
    def __init__(self, username: str, mail:str , password:str , rol_designer:bool, verification:bool):

        """
        Constructor Method  - creates instances of User class - gives values to the atributes
        
        Args:
        
        username: str - username of user
        mail: str - mail of user
        password: str - password of user
        rol_designer: bool - rol of user
        verification: bool - verification of user
        
        class atributes - All them are protected. _indicates -> protected

        """
        self._username = username
        self._mail = mail
        self._password = password
        self._rol_designer = rol_designer
        self._verification = False
#---------------------------------- methods --------------------------------

    def register(self, username, mail, password, rol_designer, verification):
         
         """"
         register method - registers a new user

         Args:

         username: str - username of user
         mail: str - mail of user
         password: str - password of user
         rol_designer: bool - rol of user
         verification: bool - verification of user

         Returns:
         User: A new user
         """
         if verification == True:
              user = User(username, mail, password, rol_designer, verification)
              self._verification = False
              return user
         else:
              print("The user is already registered")
              self._verification = False

#--------------

    def login(self, mail, password):
          
          """
          login method - logs in a user

          Args: 

          mail: str - mail of user
          password: str - password of user
          
          """

          if self._verification == True:
            print("Succesfull log in")
          else:
               print("E-mail or password incorrect")  

#---------------------------- Getters and setters -----------------------------------------

    def get_username(self):

        """
        get_username method - gets the username of the user
        
        Returns:
        str: The username of the user
        """
        return self._username

#--------------------


    def set_verification(self, new_verification: bool):
         
         """
         set_verification method - sets the verification of the user

         Args:      
         self._verification = new_verification

         """

         self._verification = new_verification

        
#====================================== DESIGNER CLASS =====================================

class Designer(User): #Son class



    def __init__(self, username: str, mail:str , password:str , rol_designer:bool, verification:bool, vehicles_list:list):

            """
            constructor method - creates instance of Designer class - gives values to the atributes

            Args:
    
            username: str - username of user
            mail: str - mail of user
            password: str - password of user
            rol_designer: bool - rol of user
            verification: bool - verification of user
            vehicles_list: list - vehicles of designer

            class atributes - All them are private. __indicates -> private
            """
    
    #Defining the class atributes with the super class

            super().__init__(username, mail, password, rol_designer, verification)
            self.__vehicles_list = vehicles_list
   