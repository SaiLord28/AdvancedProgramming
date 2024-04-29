from Users import User, Designer
from Vehicles import Vehicle, Car, Motorcycle, Yacht
from Db import Database
import time

class Catalog:
    def __init__(self):
        self.__created_vehicles = []
        self.__actual_user = User(None, None, None, None)

        self.access_menu()

#------------------------------------- methods -------------------------------------
    def access_menu(self):

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

    def register_menu(self):

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

    def login_menu(self):
                
            mail = input("Please enter your email address: ")
            password = input("Please enter your password: ")

            (verification, user) = Database.verify_login(mail, password, self.__actual_user)

            if verification == True:

                self.__actual_user = user
                
                self.principal_menu()

            else:
                self.access_menu()

#--------------------------------
    def principal_menu(self):

        while True:
            try:
                 print(f"""===========================================================
                       Welcome {self.__actual_user.get_username()} !! 

                       What do you want to do today?

                        [0] Exit
                        [1] See Catalog""" )

                 if self.__actual_user.get_rol_designer() == False:
                    print("\n===========================================================")
                    sel = int(input())

                    if  not 0 <=sel<= 1:
                        print("Invalid option, please select an option")
                        time.sleep(1.5)
                    elif sel == 0: 
                        print("Good Bye :3")
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
                    sel = int(input())
                    if  not 0 <=sel<= 3:
                         print("Invalid option, please select an option")
                         time.sleep(1.5)
                    elif sel == 0:
                         print("Good Bye :3")
                         break
                    elif sel == 1:
                         print("showing catalog...")
                         time.sleep(1)
                         self.show_catalog()
                         break
                    elif sel == 2:
                         print("You selected create vehicle")
                         time.sleep(1)
                         self.create_vehicle_menu()
                         break
                    elif sel == 3:
                         print("You selected watch your created vehicles list")
                         time.sleep(1)
                         self.watch_created_vehicles()
                         break
                         
                         
            except Exception as e:
                print("Invalid option, please select an option")
                time.sleep(1.5)


#--------------------------------
    def show_catalog(self):
        print("There are no vehicles in the list.")	

 #--------------------------------      
    def create_vehicle_menu(self):
        print("vehicle menu")

#--------------------------------
    def watch_created_vehicles(self):
        print("watch created vehicles")
