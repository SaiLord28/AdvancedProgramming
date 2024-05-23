from Users import User, Designer
from Vehicles import Vehicle, Car, Truck, Motorcycle, Yacht, Engine
from Db import Database
import time

class Catalog:

    """
    This class represents a catalog for vehicles. It allows users to register, login, and interact with the catalog.
    """

    def __init__(self):

        """
        Initializes the catalog with an empty list of created vehicles and an uninitialized user.
        """  

        self.__created_vehicles = []
        self.__actual_user = User(None, None, None, None)

        self.access_menu()

#------------------------------------- methods -------------------------------------
    def access_menu(self) -> None:
        """
        This method is the main menu of the catalog. It allows users to select options such as registering, logging in, or exiting the program.
        """

        while True:
            try:
                sel =  int(input ("""

===========================================================                                                
        Welcome to the vehicles catalog!
           
            What do you want to do?
                [0] Exit
                [1] Register
                [2] Login
           
===========================================================  \n """))

                if not 0<= sel < 3 :
                    print("Invalid option, please select an option")
                    time.sleep(1.5)
                else:
                    break
                
            except:
                print("Invalid option, please select an option")
                time.sleep(1.5)

        if sel == 0:
            print("Good Bye :3")

        elif sel == 1:

            print("===========================================================")
            self.register_menu()
            time.sleep(1.5)

        elif sel == 2:
            print("===========================================================")
            self.login_menu()
                  
  
#--------------------------------

    def register_menu(self) -> None:

        """
        This method is responsible for registering a new user in the catalog.
        It prompts the user to enter their username, email address, and password.
        Additionally, it asks the user if they want to be a designer.
        The method then verifies the registration details with the Database class.
        Finally, it returns to the main menu of the catalog.

        Args:
            self (Catalog): An instance of the Catalog class.

        Returns:
            None: This method does not return any value. It simply returns to the main menu of the catalog.
        """

        username = input("Please enter your username: ")
        mail = input("Please enter your email address: ")
        password = input("Please enter your password: ")

        while True:    
            design_ask = input("Do you want to be a designer? (y/n): ")

            if design_ask.lower() == "y":
                rol_designer = True
                break

            elif design_ask.lower() == "n":
                rol_designer = False
                break

            else:
                print("Invalid option, select y or n")
                time.sleep(1)

        Database.verify_register(username, mail, password, rol_designer,self.__actual_user)
        self.access_menu()


#--------------------------------

    def login_menu(self) -> None:
            
            """
            This method is responsible for logging in a user in the catalog.
            It prompts the user to enter their email address and password.
            The method then verifies the login details with the Database class.
            Finally, it returns to the main menu of the catalog.

            Args:
                self (Catalog): An instance of the Catalog class.

            Returns:
                None: This method does not return any value. It simply returns to the main menu of the catalog.
            """
                
            mail = input("Please enter your email address: ")
            password = input("Please enter your password: ")

            (verification, user) = Database.verify_login(mail, password, self.__actual_user)

            if verification == True:

                self.__actual_user = user
                
                self.principal_menu()

            else:
                self.access_menu()

#--------------------------------
    def principal_menu(self)->None:
        """"
            Shows the principal menu for the user.

        Args:
        self (Catalog): An instance of the Catalog class.

        eturns:
        None: This method does not return any value. It simply returns to the main menu of the catalog.

        Raises:
        None: This method does not raise any exceptions.

        """

        while True:
            
                 print(f"""===========================================================
                       Welcome {self.__actual_user.get_username()} !! 

                       What do you want to do today?

                        [0] Exit
                        [1] See Catalog""" )

                 if self.__actual_user.get_rol_designer() == False:
                    print("\n===========================================================")
                        
                        
                    try:    
                        sel = int(input())
                    except Exception:
                        print("Invalid option, please select an option")
                        time.sleep(1.5)

                    if  not 0 <=sel<= 1:

                        print("Invalid option, please select an option")
                        time.sleep(1.5)

                    elif sel == 0: 

                        print ("loggin out...")
                        time.sleep(1)
                        self.__actual_user.set_verification(False)
                        self.access_menu()
                        break

                    elif sel == 1:

                        print("showing catalog...")
                        time.sleep(1)
                        self.show_catalog()
                        break

                 elif self.__actual_user.get_rol_designer() == True:

                    self.__actual_user: Designer
                    print("""                        [2] Create vehicle
                        [3] Watch Your Created Vehicles list
===========================================================""")
                    try:
                        sel = int(input())
                    except Exception:
                        print("Invalid option, please select an option")
                        time.sleep(1.5)

                    if  not 0 <=sel<= 3:
                         
                         print("Invalid option, please select an option")
                         time.sleep(1.5)

                    elif sel == 0:
                         
                        print ("loggin out...")
                        time.sleep(1)
                        self.__actual_user.set_verification(False)
                        self.access_menu()
                        break
                    
                    elif sel == 1:
                         
                         print("showing catalog...")
                         time.sleep(1)
                         self.show_catalog()
                         break
                    
                    elif sel == 2:
                         
                        
                        self.create_vehicle_menu()
                        break

                    elif sel == 3:
                         
                         print("You selected watch your created vehicles list")
                         time.sleep(1)
                         self.watch_created_vehicles()
                         break

                    print("Invalid option, please select an option")
                    time.sleep(1.5)

#--------------------------------
    def show_catalog(self) -> None:
        """
    Displays the catalog of vehicles created by the user.

    Args:
        self (Catalog): An instance of the Catalog class.

    Returns:
        None: This method does not return any value. It simply returns to the main menu of the catalog.

    Raises:
        None: This method does not raise any exceptions.

    """    

        if self.__created_vehicles == []:

            print("There are no vehicles in the Catalog")
            time.sleep(1.5)
            self.principal_menu()

        else:

            print(f"There are {len(self.__created_vehicles)} vehicles in the list.")
            for i in range(len(self.__created_vehicles)):

                print("===========================================================")
               
                vehicle: Vehicle = self.__created_vehicles[i]

                print(vehicle.__str__())

                print("===========================================================")
                time.sleep(3)
            
            self.principal_menu()

 #--------------------------------      
    def create_vehicle_menu(self) -> None:
    
        """
    Shows the menu to create a vehicle

    Args:
        vehicle: str - type of vehicle (car, truck, yacht, motorcycle)

    Returns:
        None: This method does not return any value. It simply returns to the main menu of the catalog.

    Raises:
        None: This method does not raise any exceptions.

    """
        print("You selected create vehicle")
        time.sleep(1)
        
        while True:
            try:    
                sel = int(input(f"""========================================================

                                   [1] Create Car
                                   [2] Create Truck
                                   [3] Create Motorcycle
                                   [4] Create Yacht

========================================================
"""))
                if not 1<=sel<=4:

                    print("Invalid option, please select an option")
                    time.sleep(1.5)

                elif sel == 1:
                    vehicle_type ="car"
                    break

                elif sel == 2:
                    vehicle_type ="truck"
                    break

                elif sel == 3:
                    vehicle_type ="motorcycle"
                    break

                elif sel == 4:
                    vehicle_type ="yacht"
                    break

            except Exception:
                print("Invalid option, please select an option")
                time.sleep(1.5)

        print("  =============================================================")
        engine = self.create_engine_menu(vehicle_type)
        name = input(f"Please writte the name of the {vehicle_type}: ")
        chasis = input(f"Please select the chasis of your {vehicle_type} (A or B): ").upper()
        
        while chasis.upper() != "A" and chasis.upper() != "B":
          
          chasis = input(" Please write A or B: ")
    
        model = input(f"Please write the model of your {vehicle_type}: ")
        
        while True:
        
          try:
            year = int (input(f"Please write the year of the model of your {vehicle_type}: "))

            while year < 1886 or year > 2024: 
              
              year = int (input("Please write a year between 1886 and 2024: "))
            break
            
          except Exception:
            print("Please write a number")
        
        if vehicle_type == "car":
           
           transmision = None
           transmision = input("Please select the type of transmision of your car (MANUAL or AUTOMATIC): ")
    
           while transmision.upper() != "MANUAL" and transmision.upper() != "AUTOMATIC":

            transmision = input("Please select the type of transmision of your car (MANUAL or AUTOMATIC): ")
    
           new_vehicle = Car(name,vehicle_type,engine,chasis,model,year,transmision)
        
        elif vehicle_type == "truck":
          
          while True:

            try:
              
              capacity = float(input("Please write the capacity of your truck in cubic meters: "))

              while capacity < 0:

                capacity = float(input("Please write a positive number: "))
                
              new_vehicle = Truck(name,vehicle_type,engine,chasis,model,year,capacity)
              break  

            except Exception:
              
              print("Please write a number")
    
        elif vehicle_type == "yacht":
          
          while True:

            try:
              
              people_capacity = int(input("Please write the number of people that can go in the yacht: "))

              while people_capacity < 0:

                people_capacity = int(input("Please write a positive number: "))
    
              new_vehicle = Yacht(name,vehicle_type,engine,chasis,model,year,people_capacity)
              break

            except Exception:
              print("Please write a number")
    
        elif vehicle_type == "motorcycle":
          
          while True:

            try:
              
              wheels_diameter = float(input("Please write the wheels diameter of your motorcycle in centimeters: "))
              
              while wheels_diameter < 0:
                 
                 wheels_diameter = int(input("Please write a positive number: "))

              new_vehicle = Motorcycle(name,vehicle_type,engine,chasis,model,year,wheels_diameter)
              break

            except Exception:
              
              print("Please write a number")

        print(f"your {vehicle_type} was created ")
        time.sleep(1.5)
        
        sel = input("Do you want to upload your vehicle to the catalog? (y/n): ")
        
        while True:

            if sel.lower() == "y":
                self.__created_vehicles.append(new_vehicle)
                print("Your vehicle was uploaded to the catalog")
                time.sleep(1.5)
                break

            elif sel.lower() == "n":
                print("Your vehicle was not uploaded to the catalog")
                time.sleep(1.5)
                break

            else:
                print(" please writte y or n")
                time.sleep(1.5)
            
        
        time.sleep(1.5)
        self.__actual_user.get_vehicles_list().append(new_vehicle)
        self.principal_menu()
        
#--------------------------------
    def watch_created_vehicles(self) -> None:

        """
    Displays the list of vehicles created by the user.

    Args:
        self (Catalog): An instance of the Catalog class.

    Returns:
        None: This method does not return any value. It simply returns to the main menu of the catalog.

    Raises:
        None: This method does not raise any exceptions.

    """
        
        if self.__actual_user.get_vehicles_list() == []:
           
            print("There are no vehicles created yet.")
            time.sleep(1.5)
            self.principal_menu()

        else:
           
            print(f"There are {len(self.__actual_user.get_vehicles_list())} vehicles created.")
            for i in range(len(self.__actual_user.get_vehicles_list())):
               
                print("===========================================================")
               
                vehicle: Vehicle = self.__actual_user.get_vehicles_list()[i]

                print(vehicle.__str__())

                print("===========================================================")
                time.sleep(3)
            
            self.principal_menu()

#--------------------------------
    def create_engine_menu(self, vehicle_type:str) -> Engine:

            """
    This method is responsible for creating an engine for a vehicle.
    It prompts the user to input the type, potency, and weight of the engine.
    The method then returns an instance of the Engine class with the provided details.

    Args:
        vehicle_type (str): The type of vehicle for which the engine is being created.

    Returns:
        Engine: An instance of the Engine class with the details provided by the user.

    Raises:
        ValueError: If the user inputs a negative number for potency or weight.
    """
            print(f"Frist, let's create the engine of your {vehicle_type}: ")

            type = input("Please write the type of engine: ")

            while True:
                try:
                  
                  potency = float(input("Please write the potency of your engine in Kilowats: "))

                  while potency < 0:

                    print("Please, write a possitive number")
                  break

                except Exception:
                  print("Please, write a number")

            while True:
                try:
                  
                  weight = float(input("Please write the weight of your engine in Kilograms: "))
                  
                  while weight < 0:

                    print("Please, write a possitive number")
                  break

                except Exception:
                  print("Please, write a number")

            engine = Engine(type, potency, weight)
            return engine
