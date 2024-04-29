import time

#====================================== USER  CLASS =====================================

class User:
    def __init__(self, username: str, mail:str , password:str , rol_designer:bool):

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

    def login(self):
          
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

    def get_username(self):

        """
        get_username method - gets the username of the user
        
        Returns:
        str: The username of the user
        """
        return self._username


    def get_password(self):
         
         """
         get_password method - gets the password of the user
         
         Returns:
         str: The password of the user
         """
         return self._password
    
    def get_rol_designer(self):
         return self._rol_designer
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



    def __init__(self, username: str, mail:str , password:str , rol_designer:bool):

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

            super().__init__(username, mail, password, rol_designer)
            self.__vehicles_list = [] 

#---------------------------------- getters --------------------------------

    def get_vehicles_list(self):

        """
        get_vehicles_list method - gets the vehicles list of the designer
        
        Returns:
        list: The vehicles list of the designer
        """
        return self.__vehicles_list

# -----------------------------------methods --------------------------------
    def upload_v(self, vehicle):
         
            """
            upload_v method - uploads a new vehicle to the vehicles list of the designer

            Args:

            vehicle: Vehicle - vehicle to be added to the vehicles list

            """
            self.__vehicles_list.append(vehicle)
    

