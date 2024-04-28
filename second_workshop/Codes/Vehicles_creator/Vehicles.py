"""13/03/2024  - Advanced programming workshop #1

This is a programm that creates vehicles and add them to a list.

Author: Sergio Nicolás Mendivelso



"""


#======================================== CLASS ENGINE ==============================================

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
    
 #---------------------------- Methods ----------------------------   


  #Method that calculates the gas consumption of the vehicles.
    
  def cal_gas_consuption(self, chasis:str):

      """

    Calculate the gas consuption of the vehicle
    

    """

      if chasis == "A":  
        return  1.1 * self.__potency() + 0.2 * self.__weight() - 0.3
      
      
      elif chasis == "B": 
       return  1.1 * self.__potency() + 0.2 * self.__weight() - 0.5
      
  
  
#------------------------

  #The class have a __str__() method cuz the atributtes are private - they return the value of the atribute.
  
  def __str__(self):
    """"   

    __str__ method.    

    Returns:
  
    str: A string of the attributes of the engine.

    """
    return f"Type: {self.__type} \n 
            Potency: {self.__potency} \n 
            Weight: {self.__weight} \n"
  

#===========================---  CLASS VEHICLE (FATHER CLASS)---===========================


class Vehicle():


  def __init__(self, name:str , type:str, engine_type:str, potency:float, weight:float, chasis: str, model: str, year: int):

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
      self._name = name
      self._type = type
      self._engine = Engine(engine_type, potency, weight)
      self._chasis = chasis
      self._model = model 
      self._year = year 
      self._gas_consuption = self._engine.cal_gas_consuption(self._chasis)

#------------------------------------- Methods --------------------------------------

  def __str__(self):

    """"   

    __str__ method.    

     Returns:
  
      str: A string of the attributes of the Vehicle.

      """
    return f"Name: {self._name} \n 
          Type: {self._type} \n 
          Engine: {self._engine} \n 
          Chasis: {self._chasis} \n 
          Model: {self._model} \n 
          Year: {self._year} \n 
          Gas Consuption: {self._gas_consuption} \n"
  
    
  #---------------------  Getters  ---------------------

  def get_name(self):
      
      """Method to get the name of the vehicle
      
      Returns:
      
      str: A string of the name of the vehicle."""

      return self._name
  
  #----------

  def get_type(self):
      
      """Method to get the type of the vehicle
      
      Returns:

      str: A string of the type of the vehicle.
      
      """
      return self._type

  

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

  #-------------------------------------- Methods  --------------------------------------

  
  def __str__(self):
   
      """"   

      __str__ method.    

     Returns:
  
      str: A string of the attributes of the car.

      """  
      return f"Name: {self._name} \n 
          Type: {self._type} \n 
          Engine: {self._engine} \n 
          Chasis: {self._chasis} \n 
          Model: {self._model} \n 
          Year: {self._year} \n 
          Gas Consuption: {self._gas_consuption} \n 
          Transmision Type: {self._transmision_type} \n "

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
      

  def __str__(self):

    """"   

    __str__ method.    

     Returns:
  
      str: A string of the attributes of the truck.

      """
    return f"Name: {self._name} \n 
          Type: {self._type} \n 
          Engine: {self._engine} \n 
          Chasis: {self._chasis} \n 
          Model: {self._model} \n 
          Year: {self._year} \n 
          Gas Consuption: {self._gas_consuption} \n 
          Capacity: {self._capacity} \n "
  

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

  def __str__(self):

        """"   

    __str__ method.    

     Returns:
  
      str: A string of the attributes of the yacht.

      """
        return f"Name: {self._name} \n 
          Type: {self._type} \n 
          Engine: {self._engine} \n 
          Chasis: {self._chasis} \n 
          Model: {self._model} \n 
          Year: {self._year} \n 
          Gas Consuption: {self._gas_consuption} \n 
          People Capacity: {self._people_capacity} \n"

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


#------------------------------------- Methods --------------------------------------

  def __str__(self):

    """"   

    __str__ method.    

     Returns:
  
      str: A string of the attributes of the motorcycle.

      """
    return f"Name: {self._name} \n 
          Type: {self._type} \n 
          Engine: {self._engine} \n 
          Chasis: {self._chasis} \n 
          Model: {self._model} \n 
          Year: {self._year} \n 
          Gas Consuption: {self._gas_consuption} \n 
          Wheels Diameter: {self._wheels_diameter} \n "

