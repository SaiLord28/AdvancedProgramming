from abc import abstractmethod

#======================================== CLASS ENGINE ==============================================

class Engine:

  
  def __init__(self,type:str, potency:float, weight:float):
    """
    Constructor Method  - creates instances of Engine class - gives values to the atributes

    Args:
        type: str - type of engine
        potency: float - potency of engine (In KiloWats)
        weight: float - weight of engine (In KG)

    Class Attributes:
        __type: str - type of engine
        __potency: float - potency of engine (In KiloWats)
        __weight: float - weight of engine (In KG)

    Raises:
        ValueError: If the potency or weight is not a positive number

    Returns:
        None
    """

    self.__type = type 
    self.__potency = potency
    self.__weight = weight 
    
 #---------------------------- Methods ----------------------------   


  #Method that calculates the gas consumption of the vehicles.
    
  def cal_gas_consuption(self, chasis: str) -> float:
    """
    Calculate the gas consuption of the vehicle.

    Args:
        chasis: str - chasis of vehicle (A or B)

    Returns:
        float: The calculated gas consumption of the vehicle.

    Raises:
        ValueError: If the chasis is not 'A' or 'B'

    """
    if chasis == "A": 
        return 1.1 * self.__potency + 0.2 * self.__weight - 0.3
    elif chasis == "B": 
        return 1.1 * self.__potency + 0.2 * self.__weight - 0.5
      
  
  
#------------------------

  #The class have a __str__() method cuz the atributtes are private - they return the value of the atribute.
  
  def __str__(self) -> str:
    """
        __str__ method.

        Returns:
            str: A string of the attributes of the engine.

        """
    return f"""
            Engine type : {self.__type}
            Engine Potency: {self.__potency}
            Engine Weight: {self.__weight} \n"""
  

#===========================---  CLASS VEHICLE (FATHER CLASS)---===========================


class Vehicle:


  def __init__(self, name: str, type: str, engine: Engine, chasis: str, model: str, year: int):
    """
    Constructor Method  - creates instances of Vehicle class - gives values to the attributes

    Args:
        name: str - name of the vehicle
        type: str - type of vehicle
        engine: Engine - engine of vehicle
        chasis: str - chasis of vehicle (A or B)
        model: str - model of vehicle
        year: int - year of vehicle

    Class Attributes:
        _name: str - name of the vehicle
        _type: str - type of vehicle
        _engine: Engine - engine of vehicle
        _chasis: str - chasis of vehicle (A or B)
        _model: str - model of vehicle
        _year: int - year of vehicle
        _gas_consuption: float - calculated gas consumption of the vehicle

    Raises:
        ValueError: If the chasis is not 'A' or 'B'

    Returns:
        None
    """
    self._name = name
    self._type = type
    self._engine = engine
    self._chasis = chasis
    self._model = model
    self._year = year
    self._gas_consuption = self._engine.cal_gas_consuption(self._chasis)

#------------------------------------- Methods --------------------------------------

  @abstractmethod
  def __str__(self) -> str:
    """
    __str__ method.

    Returns:
        str: A string of the attributes of the Vehicle.

    This method is an abstract method that must be implemented by the subclasses of the Vehicle class. It should return a string representation of the vehicle's attributes.
    """
    pass
  
    
  #---------------------  Getters  ---------------------

  def get_name(self) -> str:
    """
    Method to get the name of the vehicle.

    Returns:
        str: A string of the name of the vehicle.
    """
    return self._name
  
  #----------

  def get_type(self) -> str:
      
      """Method to get the type of the vehicle
      
      Returns:

      str: A string of the type of the vehicle.
      
      """
      return self._type
  

#===========================---  CLASS CAR ---==================================================

class Car(Vehicle): #Inheritance - Car is a Vehicle  

  #Constructor Method
  def __init__(self, name: str, type: str, engine: Engine, chasis: str, model: str, year: int, transmision_type: str):
    """
    Constructor Method  - creates instances of Car class - gives values to the atributes

    Args:
        name: str - name of the car
        type: str - type of vehicle
        engine: Engine - engine of vehicle
        chasis: str - chasis of vehicle
        model: str - model of vehicle
        year: int - year of vehicle
        transmision_type: str - type of transmision of car (MANUAL OR AUTOMATIC)

    Class Attributes:
        _name: str - name of the car
        _type: str - type of vehicle
        _engine: Engine - engine of vehicle
        _chasis: str - chasis of vehicle
        _model: str - model of vehicle
        _year: int - year of vehicle
        _transmision_type: str - type of transmision of car (MANUAL OR AUTOMATIC)
        _gas_consuption: float - calculated gas consumption of the vehicle

    Raises:
        ValueError: If the chasis is not 'A' or 'B'

    Returns:
        None
    """
    super().__init__(name, type, engine, chasis, model, year)
    self.__transmision_type = transmision_type 

  #-------------------------------------- Methods  --------------------------------------

  
  def __str__(self) -> str:
    """
    __str__ method.

    Returns:
        str: A string of the attributes of the car.

    This method returns a string representation of the car's attributes.
    """
    return f"""\
        Name: {self._name}\
        Type: {self._type}\
        Engine: {self._engine}\
        Chasis: {self._chasis}\
        Model: {self._model}\
        Year: {self._year}\
        Gas Consumption: {self._gas_consuption} \
        Transmision Type: {self.__transmision_type} \n """

#===========================---  CLASS TRUCK ---==================================================
    
class Truck(Vehicle): #Inheritance - Truck is a Vehicle


  def __init__(self, name, type, engine, chasis, model, year, capacity: float):
    """
    Constructor Method  - creates instances of Truck class - gives values to the attributes

    Args:
        name: str - name of the truck
        type: str - type of vehicle
        engine: Engine - engine of vehicle
        chasis: str - chasis of vehicle
        model: str - model of vehicle
        year: int - year of vehicle
        capacity: float - capacity of truck (In M3)

    Class Attributes:
        __name: str - name of the truck
        __type: str - type of vehicle
        __engine: Engine - engine of vehicle
        __chasis: str - chasis of vehicle
        __model: str - model of vehicle
        __year: int - year of vehicle
        __capacity: float - capacity of truck (In M3)
        __gas_consuption: float - calculated gas consumption of the vehicle

    Raises:
        ValueError: If the chasis is not 'A' or 'B'

    Returns:
        None
    """
    #Defining the class attributes with the super class
    super().__init__(name, type, engine, chasis, model, year)
    self.__capacity = capacity 
      
#------------------------------------- Methods --------------------------------------

  def __str__(self) -> str:
    """
    __str__ method.

    Returns:
        str: A string of the attributes of the truck.

    This method returns a string representation of the truck's attributes.
    """
    return f"""\
        Name: {self._name} \
        Type: {self._type} \
        Engine: {self._engine} \
        Chasis: {self._chasis} \
        Model: {self._model} \
        Year: {self._year} \
        Gas Consumption: {self._gas_consuption} \
        Capacity: {self.__capacity} \n """
  

#=======================================--- CLASS YACHT---===========================
class Yacht(Vehicle):

  #Constructor Method
  def __init__(self, name, type, engine, chasis, model, year, people_capacity:int):
    """
    Constructor Method  - creates instances of Yacht class - gives values to the atributes

    Args:
        type: str - type of vehicle
        engine: Engine - engine of vehicle
        chasis: str - chasis of vehicle
        model: str - model of vehicle
        year: int - year of vehicle
        people_capacity: int - people capacity of yacht (How many people can go the yacht)

    Class Attributes:
        __name: str - name of the yacht
        __type: str - type of vehicle
        __engine: Engine - engine of vehicle
        __chasis: str - chasis of vehicle
        __model: str - model of vehicle
        __year: int - year of vehicle
        __people_capacity: int - people capacity of yacht (How many people can go the yacht)
        __gas_consuption: float - calculated gas consumption of the vehicle

    Raises:
        ValueError: If the chasis is not 'A' or 'B'

    Returns:
        None
    """
    # Defining the class attributes with the super class
    super().__init__(name, type, engine, chasis, model, year)
    self.__people_capacity = people_capacity 

#------------------------------------- Methods --------------------------------------
  def __str__(self) -> str:
    """
    __str__ method.

    Returns:
        str: A string of the attributes of the yacht.

    This method returns a string representation of the yacht's attributes.
    """
    return f"""\
        Name: {self._name} \
        Type: {self._type} \
        Engine: {self._engine} \
        Chasis: {self._chasis} \
        Model: {self._model} \
        Year: {self._year} \
        Gas Consumption: {self._gas_consuption} \
        People Capacity: {self.__people_capacity} \n"""""

#==================================---  CLASS MOTORCYCLE ---============================

class Motorcycle(Vehicle):

  #Constructor Method
  def __init__(self, name, type, engine, chasis, model, year, wheels_diameter: float) -> None:
    """
    Constructor Method  - creates instances of Motorcycle class - gives values to the atributes

    Args:
        type: str - type of vehicle
        engine: Engine - engine of vehicle
        chasis: str - chasis of vehicle
        model: str - model of vehicle
        year: int - year of vehicle
        wheels_diameter: float - wheels diameter of motorcycle (In CM)

    Class Attributes:
        __name: str - name of the motorcycle
        __type: str - type of vehicle
        __engine: Engine - engine of vehicle
        __chasis: str - chasis of vehicle
        __model: str - model of vehicle
        __year: int - year of vehicle
        __wheels_diameter: float - wheels diameter of motorcycle (In CM)
        __gas_consuption: float - calculated gas consumption of the vehicle

    Raises:
        ValueError: If the chasis is not 'A' or 'B'

    Returns:
        None
    """
    # Defining the class attributes with the super class
    super().__init__(type, name, engine, chasis, model, year)
    self.__wheels_diameter = wheels_diameter 


#------------------------------------- Methods --------------------------------------

  def __str__(self) -> str:
    """
    __str__ method.

    Returns:
        str: A string of the attributes of the motorcycle.

    This method returns a string representation of the motorcycle's attributes.
    """
    return f"""\
        Name: {self._name}\
        Type: {self._type}\
        Engine: {self._engine}\
        Chasis: {self._chasis} \
        Model: {self._model} \
        Year: {self._year}\
        Gas Consumption: {self._gas_consuption}\
        Wheels Diameter: {self.__wheels_diameter} \n """

