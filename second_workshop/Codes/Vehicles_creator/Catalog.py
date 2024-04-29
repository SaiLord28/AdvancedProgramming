from Users import User, Designer
from Vehicles import Vehicle, Car, Motorcycle, Yacht
from Db import Database
import time

class Catalog:
    def __init__(self):
        self.__created_vehicles = []
        self.__actual_user = User(None, None, None, None)

        self.access_menu()


    def access_menu(self):

        while True:
            sel=  int(input ("""

===========================================================                                                
        Welcome to the vehicles catalog!
           
            What do you want to do?
                [1] Register
                [2] Login
                [0] Exit
           
===========================================================  \n """))
            if sel < 0:
                print("Invalid option, select an option")
                time.sleep(1500)
            else:
                break
        if sel == 0:
            print("Good Bye :3")
            time.sleep(1500)

        elif sel == 1:

            print("===========================================================")
            self.register_menu()
            print("===========================================================")

        elif sel == 2:
            print("===========================================================")
            self.login_menu()
            print("===========================================================")
            
                
    def register_menu(self):
        rol_designer:bool 

        while True:
            username = input("Please enter your username")
            mail = input("Please enter your email address")
            password = input("Please enter your password")
            design_ask = input("Do you want to be a designer? (y/n)")


            if design_ask == "y":
                rol_designer = True
                break


            elif design_ask == "n":
                rol_designer == False
                break
            else:
                print("Invalid option, select y or n")
                Database.verify_register(username, mail, password, rol_designer)

    def login_menu(self):
                
            mail = input("Please enter your email address")
            password = input("Please enter your password")

            if Database.verify_login(mail, password, self.__actual_user)[0] == True:

                self.__actual_user = Database.verify_login(mail, password, self.__actual_user)[1]

            else:
                self.access_menu()
    
