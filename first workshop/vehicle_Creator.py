"""13/03/2024  - Advanced programming workshop #1

This is a programm that creates vehicles and add them to a list.

Author: Sergio Nicolás Mendivelso



"""
 # =====================---- MODEL ----====================

#====--- CLASS ENGINE ---====

class Engine:

  
  def __init__(self,type:str, potency:float, weight:float):
    """

  Constructor Method  - creates instances of Engine class - gives values to the atributes

  Args: 

type: str - type of engine
potency: float - potency of engine (In KiloWats)
weight: float - weight of engine (In KG)
  
  class atributes - All them are private. __indicates -> private

    """

    self.__type = type 
    self.__potency = potency
    self.__weight = weight 
    
 #---- GETTERS ----   

  #The class have getters cuz the atributtes are private - they return the value of the atribute.
  
  def get_type(self):
    return self.__type
 
  def get_potency(self):
    return self.__potency

  def get_weight(self):
    return self.__weight

#NOTE: It have not setters cuz the atributes will not be changed, they are defined in the constructor


#===========================---  CLASS VEHICLE (FATHER CLASS)---===========================


class Vehicle():


  def __init__(self, type:str, engine: Engine, chasis: str, model: str, year: int):

      """

    Constructor Method  - creates instances of Vehicle class - gives values to the atributes

    Args: 

    type: str - type of vehicle
    engine: Engine - engine of vehicle
    chasis: str - chasis of vehicle (A or B)
    model: str - model of vehicle
    year: int - year of vehicle
    
    class atributes - All them are protected _indicates -> protected

    """
      self._type = type
      self._engine = engine 
      self._chasis = chasis
      self._model = model 
      self._year = year 
      self._gas_consuption = None #It will be defined in the Manager Class. Cuz the logic can't be in the Model

#------------------------------------- GETTERS AND SETTERS --------------------------------------
  
  #The class have getters cuz the atributtes are private - they return the value of the atribute.
  def get_type(self):
    return self._type
  
  def get_engine(self):
    return self._engine
    
  def get_chasis(self):
    return self._chasis

  def get_model(self):
    return self._model
  
  def get_year(self):
    return self._year

  def get_gas_consuption(self):
    return self._gas_consuption

  #_gas_consuption is the only atributes that have setter cuz it will be changed after.
  
  def set_gas_consuption(self, new_gas_consuption):
        self._gas_consuption = new_gas_consuption

  #NOTE:  the other atributes will not be changed, they are defined in the constructor
  
#===========================---  CLASS CAR ---==================================================

class Car(Vehicle): #Inheritance - Car is a Vehicle  

  #Constructor Method
  def __init__(self, type, engine, chasis, model, year, transmision_type:str):

      """

    Constructor Method  - creates instances of Car class - gives values to the atributes

    Args: 

    type: str - type of vehicle
    engine: Engine - engine of vehicle
    chasis: str - chasis of vehicle
    model: str - model of vehicle
    year: int - year of vehicle
    transmision_type: str - type of transmision of car (MANUAL OR AUTOMATIC)

    class atributes - All them are private. __indicates -> private

    """

  #Defining the class atributes with the super class
    
      super().__init__(type, engine, chasis, model, year)

      self.__transmision_type = transmision_type 

  #-------------------------------------- GETTERS  --------------------------------------

  #The class have a getter cuz the atribute is private - it return the value of transmision_type
  #The inhereted atributes are defined in super class
  
  def get_transmision_type(self):
    return self.__transmision_type

  #NOTE:  the atributes will not be changed, they are defined in the constructor

#===========================---  CLASS TRUCK ---==================================================
    
class Truck(Vehicle): #Inheritance - Truck is a Vehicle


  def __init__(self, type, engine, chasis, model, year, capacity: float):

      """

    Constructor Method  - creates instances of Vehicle class - gives values to the atributes

    Args: 

    type: str - type of vehicle
    engine: Engine - engine of vehicle
    chasis: str - chasis of vehicle
    model: str - model of vehicle
    year: int - year of vehicle
    capacity: float - capacity of truck (In M3)
    

    class atributes - All them are private. __indicates -> private

    """

    #Defining the class atributes with the super class
      super().__init__(type, engine, chasis, model, year)
      self.__capacity = capacity 

#---- GETTERS  ----

#The class have a getter cuz the atribute is private - it return the value of capacity
#The inhereted atributes are defined in super class

  def get_transmision_type(self):
    return self.__capacity

#NOTE:  the atributes will not be changed, they are defined in the constructor

#=======================================--- CLASS YACHT---===========================
class Yacht(Vehicle):

  #Constructor Method
  def __init__(self, type, engine, chasis, model, year, people_capacity:int):


      """

    Constructor Method  - creates instances of Yacht class - gives values to the atributes

    Args: 

    type: str - type of vehicle
    engine: Engine - engine of vehicle
    chasis: str - chasis of vehicle
    model: str - model of vehicle
    year: int - year of vehicle
    people_capacity: int - people capacity of yacht (How manu peopl can go the yacht))


    class atributes - All them are private. __indicates -> private

    """
    
  #Defining the class atributes with the super class
    
      super().__init__(type, engine, chasis, model, year)

      self.__people_capacity = people_capacity 

#-------------------------------------- GETTERS  --------------------------------------

#The class have a getter cuz the atribute is private - it return the value of people_capacity
#The inhereted atributes are defined in super class

def get_people_capacity(self):
  return self.__people_capacity

#NOTE:  the atributes will not be changed, they are defined in the constructor
    
 
#==================================---  CLASS MOTORCYCLE ---============================

class Motorcycle(Vehicle):

  #Constructor Method
  def __init__(self, type,  engine, chasis, model, year, wheels_diameter:float):


      """

    Constructor Method  - creates instances of Motorcycle class - gives values to the atributes

    Args: 

    type: str - type of vehicle
    engine: Engine - engine of vehicle
    chasis: str - chasis of vehicle
    model: str - model of vehicle
    year: int - year of vehicle
    wheels_diameter: float - wheels diameter of motorcycle (In CM)


    class atributes - All them are private. __indicates -> private

    """

  #Defining the class atributes with the super class
    
      super().__init__(type, engine, chasis, model, year)

      self.__wheels_diameter = wheels_diameter 

#-------------------------------------- GETTERS  --------------------------------------

#The class have a getter cuz the atribute is private - it return the value of capacity
#The inhereted atributes are defined in super class

def get_wheels_diameter(self):
  return self.__wheels_diameter

#NOTE:  the atributes will not be changed, they are defined in the constructor

# =====================---- CONTROL ----===============================================

#====---  CLASS MAIN CONTROLLER ---====
import sys
import time
class Main_controller:

  def __init__(self):

      """

    Constructor Method  - creates instances of Main_Controller class - gives values to the atributes

    class atributes - All them are private. __indicates -> private

    """
      self.__view = View(self)
      self.__vehicles = []
      self.__view.start_menu()
    

  #-------------------------------------- ADITTIONAL METHODS --------------------------

  #Method that calculates the gas consumption of the vehicles.
    
  def cal_gas_consuption(self,vehicle:Vehicle):

      """

    Calculate the gas consuption of the vehicle

    Args: 

    vehicle: Vehicle - an object type Vehycle
    

    """
    
      if vehicle.get_chasis() == "A":  
        vehicle.set_gas_consuption(1.1 * vehicle.get_engine().get_potency() + 0.2 * vehicle.get_engine().get_weight() - 0.3)
      elif vehicle.get_chasis() == "B": 
        vehicle.set_gas_consuption(1.1 * vehicle.get_engine().get_potency() + 0.2 * vehicle.get_engine().get_weight() - 0.5)
  
      
#-------------------------------------------------------------------------------------
  
  #Methods that creates the  different Vehicles and engine:
  
  def create_engine(self,type:str, potency:float, weight:float):

      """

    Create a engine 

    Args: 

    type: str - type of engine
    potency: float - potency of engine (In KiloWats)
    weight: float - weight of engine (In KG)

    return

    the created engine
    """
    
      engine = Engine(type, potency, weight)
      return engine
  #-------------------------------------------------------------------------------------
  def create_car(self, type:str, engine:Engine,chasis:str,model:str,year:int,transmision_type: str):

      """

    Creates a Car and add it to a list of vehicles

    Args: 

    type: str - type of vehicle
    engine: Engine - engine of vehicle
    chasis: str - chasis of vehicle
    model: str - model of vehicle
    year: int - year of vehicle
    transmision_type: str - type of transmision of car (MANUAL OR AUTOMATIC


    """
      car = Car(type,engine,chasis,model,year,transmision_type)
      self.cal_gas_consuption(car)
    
  
      self.__vehicles.append(car)

  #-------------------------------------------------------------------------------------
  
  def create_truck(self,type:str,engine:Engine,chasis:str,model:str,year:int,capacity:float):
      """

    Creates a truck and add it to a list of vehicles

    Args: 

    type: str - type of vehicle
    engine: Engine - engine of vehicle
    chasis: str - chasis of vehicle
    model: str - model of vehicle
    year: int - year of vehicle
    capacity: float - capacity of truck (In M3)


    """
      truck = Truck(type,engine,chasis,model,year,capacity)
      self.cal_gas_consuption(truck)
      self.__vehicles.append(truck)
 
#-------------------------------------------------------------------------------------
  def create_yacht (self,type:str,engine:Engine,chasis:str,model:str,year:int, people_capacity:int):
    """

    Creates a yacht and add it to a list of vehicles

    Args: 

    type: str - type of vehicle
    engine: Engine - engine of vehicle
    chasis: str - chasis of vehicle
    model: str - model of vehicle
    year: int - year of vehicle
    people_capacity: int - people capacity of yacht (How many people can go the yach)


    """
    
    yacht = Yacht(type,engine,chasis,model,year,people_capacity)
    self.cal_gas_consuption(yacht)
    self.__vehicles.append(yacht)

#-------------------------------------------------------------------------------------

  def create_motorcycle(self,type:str,engine:Engine,chasis:str,model:str,year:int,wheels_diameter:float):
    """

    Creates a mntorcycle and add it to a list of vehicles

    Args: 

    type: str - type of vehicle
    engine: Engine - engine of vehicle
    chasis: str - chasis of vehicle
    model: str - model of vehicle
    year: int - year of vehicle
    wheels_diameter: float - wheels diameter of motorcycle (In CM)


    """
    motorcycle = Motorcycle(type, engine,chasis,model,year,wheels_diameter)
    self.cal_gas_consuption(motorcycle)
    self.__vehicles.append(motorcycle)
    
#-------------------------------------------------------------------------------------
  def start_menu_logic(self, index : int):

    """

    Start the logic of the menu

    Args: 
    
    index: int - index of the option selected

    """
    if index == 1:
      self.__view.create_vehicle_menu("car")
    elif index == 2:
      self.__view.create_vehicle_menu("truck")
    elif index == 3:
      self.__view.create_vehicle_menu("yacht")
    elif index == 4:
      self.__view.create_vehicle_menu("motorcycle")
    elif index == 5:
      self.__view.vehicles_list_menu()
    elif index == 6:
      print("goodbye! See u later ;)")
      sys.exit()
    else: 
      print("Please, select a valid number")
      
      

#------------------------------------- GETTERS -------------------------------------

  #The class have a getter cuz the atribute is private - it return the value of capacity
  
  def get_vehicles(self):
    return self.__vehicles

  #NOTE:  the atributes will not be changed, they are defined in the constructor
    
    # =====================---- GUI ----=============================================
class View:
  def __init__(self,controller:Main_controller):

    """

    Contructor Method  - creates instances of View class - define the controller

    Args: 

    controller: Main_controller - an object type Main_controller - allow to use controller Methods



    """
    self.__controller = controller
  #-------------------------------------------------------------------------------------
  def start_menu(self):

    """

    Start the main menu


    """
    
    self.__controller.start_menu_logic( 
      int(input(""""=============================================================
      
      Welcome to Create Vehicles program. Please select one option:
      1. Create a car
      2. Create a truck
      3. Create a yacht
      4. Create a motorcycle
      5. Vehicle list
      6. Exit
      
      =============================================================
      
      """
      )))
  #-------------------------------------------------------------------------------------

  def create_engine_menu(self, vehicle:str):

    """

    Shows the menu to create the engine of the vehicle

    Args: 

    vehicle: str - type of vehicle (car, truck, yacht, motorcycle)

    return:

    the created engine

    """
    print(f"Frist, let's create the engine of your {vehicle}: ")
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
     
    engine = self.__controller.create_engine(type, potency, weight)
    return engine
    #-------------------------------------------------------------------------------------
  def create_vehicle_menu(self,vehicle:str):

    """

    Shows the menu to create a vehicle

    Args: 

    vehicle: str - type of vehicle (car, truck, yacht, motorcycle)

    """
    print("  =============================================================")
    engine = self.create_engine_menu(vehicle)
    chasis = input(f"Please select the chasis of your {vehicle} (A or B): ")
    
    while chasis.upper() != "A" and chasis.upper() != "B":
      chasis = input(" Please write A or B: ")

    model = input(f"Please write the model of your {vehicle}: ")
    
    while True:

      try:
        year = int (input(f"Please write the year of the model of your {vehicle}: "))
        while year < 1886 or year > 2024: 
          year = int (input("Please write a year between 1886 and 2024: "))
        break
        
      except Exception:
        print("Please write a number")
    
    if vehicle == "car":
       transmision = None
       transmision = input("Please select the type of transmision of your car (MANUAL or AUTOMATIC): ")

       while transmision.upper() != "MANUAL" and transmision.upper() != "AUTOMATIC":
        transmision = input("Please select the type of transmision of your car (MANUAL or AUTOMATIC): ")

       self.__controller.create_car(vehicle,engine,chasis,model,year,transmision)
    
    elif vehicle == "truck":
      while True:
        try:
          capacity = float(input("Please write the capacity of your truck in cubic meters: "))
          while capacity < 0:
            capacity = float(input("Please write a positive number: "))
            
          self.__controller.create_truck(vehicle,engine,chasis,model,year,capacity)
          break  
        except Exception:
          print("Please write a number")

    elif vehicle == "yacht":
      while True:
        try:
          people_capacity = int(input("Please write the number of people that can go in the yacht: "))
          while people_capacity < 0:
            people_capacity = int(input("Please write a positive number: "))

          self.__controller.create_yacht(vehicle,engine,chasis,model,year,people_capacity)
          break
        except Exception:
          print("Please write a number")

    elif vehicle == "motorcycle":
      while True:
        try:
          wheels_diameter = float(input("Please write the wheels diameter of your motorcycle in centimeters: "))
          while wheels_diameter < 0:
             wheels_diameter = int(input("Please write a positive number: "))
          self.__controller.create_truck(vehicle,engine,chasis,model,year,wheels_diameter)
          break
        except Exception:
          print("Please write a number")

    print(f"your {vehicle} was created ")
    time.sleep(3)
    
    self.start_menu()

  #-------------------------------------------------------------------------------------

  def vehicles_list_menu(self):

    """

    Shows the list of vehicles and their attributes

    """
    print("  =============================================================")
    if self.__controller.get_vehicles() == []:
      print("There are no vehicles in the list.")

      time.sleep(3)
      self.start_menu()

    else: 
      for  vehicle in self.__controller.get_vehicles():
     
        print(f"""  ____________________
        Vehicle type: {vehicle.get_type()}
        Chasis: {vehicle.get_chasis()}
        Model: {vehicle.get_model()}
        Year: {vehicle.get_year()}
        Engine type: {vehicle.get_engine().get_type()}
        Engine potency: {vehicle.get_engine().get_potency()}
        Engine weight: {vehicle.get_engine().get_weight()}
        Gas consumption: {vehicle.get_gas_consuption()}
_________________--""")
        time.sleep(2)
      self.start_menu()

  # =====================---- LAUNCHER ----============================================

"""

Launch programm

"""

control = Main_controller()

