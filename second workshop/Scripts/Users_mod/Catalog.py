from Vehicles_creator.Vehicles import Vehicle, Car, Motorcycle, Yacht, Truck
from Users_mod.Db import Database
from Users_mod.Users import User

class Catalog:
    def __init__(self):
        self.__created_vehicles = []
        self.__actual_user = None

        self.access_menu()


    def access_menu(self):

     while True:
        sel:int = input ("""
           
        What do you want to do?
            [1] Register
            [2] Login
            [0] Exit
           
                    """)
        if sel < 0:
            print("Invalid option, select an option")
        else:
            break
        if sel == 0:
            print("Good Bye :3")

        elif sel == 1:
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
    
        elif sel == 2:

            mail = input("Please enter your email address")
            password = input("Please enter your password")
            Database.verify_login(mail, password, self.__actual_user)
