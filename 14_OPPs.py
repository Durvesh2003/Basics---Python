# 1 Basics Class and Object
    # Create a Car class with attributes/variables like brand and model . Then create and instance of the class. 
'''
class Car:                                          # class name should start with capital letter
    def __init__(self , brand , model):             # self works like (this) in js and java
        self.brand = brand                          # __init__ is constructor
        self.model = model


my_car = car("Toyota","Corolla")                 # agar hame car object mai koi value add karne hai toh hame ek special syntax banana hoga woh hai function jo ki upar hai
print(my_car.brand)
print(my_car.model)

# my_new_car = Car("Tata","safari")
# print(my_new_car.brand)
# print(my_new_car.model)
'''




# 2 Class Method and Self
    # Add a method to the car class that displays the full name of the car(brand and model)
'''
class Car:                                          # class name should start with capital letter
    def __init__(self , brand , model):             # self works like this in js and java
        self.brand = brand                          # __init__ is constructor
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"          # f"" is formated string
    
    


my_car = Car("Toyota","Corolla")                 # agar hame car object mai koi value add karne hai toh hame ek special syntax banana hoga woh hai function jo ki upar hai
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())
'''



# 3 Inheritance
    # create an ElectricCar class that inherits from car class and has an additional attributebattery_size

'''
class Car:                                         
    def __init__(self , brand , model):            
        self.brand = brand                          
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model} {self.battery_size}"         
    
class ElectricCar(Car):                                          # this is the concept of inheritance used to take reference from parent class here parant class is Car and child class is ElectricCar 
    def __init__(self, brand, model, battery_size):              
      super().__init__(brand, model)
      self.battery_size = battery_size

    


# my_car = Car("Toyota","Corolla")                 
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

my_tesla = ElectricCar("Tesla" , "Model s", "85k/h")
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.battery_size)
print(my_tesla.full_name())
'''




# 4 Encasultion
    # modify the Car class to encapsulate the brand attribute, making it private ,and provide a getter method for it.
        
        # it we have __brand i.e __attributes here __ means private so it is limited till class and object cannot access it 
'''
class Car:                                         
    def __init__(self , brand , model):            
        self.brand = brand                          
        self.model = model

    def get_brand(self):                           # this a method to get the access of that attiributes
        return self.brand + " !"                   # agar humne user se input liya aur usko kuch add karna ho to ye method ka use karte hai 

    def full_name(self):
        return f"{self.brand} {self.model} {self.battery_size}"         
    
class ElectricCar(Car):                                          # this is the concept of inheritance used to take reference from parent class here parant class is Car and child class is ElectricCar 
    def __init__(self, brand, model, battery_size):              
      super().__init__(brand, model)
      self.battery_size = battery_size


my_tesla = ElectricCar("Tesla" , "Model s", "85k/h")
print(my_tesla.brand)
print(my_tesla.get_brand())
'''





# 5 Polymorphism
    # Demostrate polymorphism by defining amethod fuel_type in both Car and ElectricCar classes, but with different behaviours
       # here fuel_type are two function with same name but different behaviour
'''
class Car:                                         
    def __init__(self , brand , model):            
        self.brand = brand                          
        self.model = model
                
    def full_name(self):
        return f"{self.brand} {self.model} {self.battery_size}"         
    
    def feul_type(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):                                          # this is the concept of inheritance used to take reference from parent class here parant class is Car and child class is ElectricCar 
    def __init__(self, brand, model, battery_size):              
      super().__init__(brand, model)
      self.battery_size = battery_size
    
    def feul_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla" , "Model s", "85k/h")
# print(my_tesla.brand)
print(my_tesla.feul_type())

Safari = Car("Tata", "Safari")
print(Safari.feul_type())
'''


# another example of polymorphism from my side
        # here mango are two function with same name but different behaviours/parameters
'''
class Fruit1:
    
    def __init__(self, color):
        self.color =color

    def mango(self):
        return "Grows in April-May"
    
class Fruit2(Fruit1):

    def mango(self):
        return "Sales in May-June"
    
season1 = Fruit1("green")
print(season1.mango())

season2 = Fruit2("red")
print(season2.mango())
'''





# 6 Class Variables
    # Add a class variable to Car that keeps the track of the number of cars created
'''
class Car:
    total_car = 0                        # this is the class variable 
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
        Car.total_car += 1    # or   self.total_car 
    
Car("Rolls Ryce", "Model 6")
Car("Tata", "Model 2")
Car("Lambo", "Model 1")
print(Car.total_car)
'''





# 7 Satic Method
    # Add a static method two the Car class that returns a general description of a car
'''
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @staticmethod                    # docaeters are very imp concept of python and mostly used in decoratotrs   # it is one of the decorator # this method only melogs to only class and not object therefor their is no neeed of self in it for telephone network jo ki woh kaat diya jata hai 
    def general_discription():
        return "Cars are means of transport"
    
print(Car.general_discription())
'''




# 8 Property Decorator
    # Use a property dcorator in the Car class tomake the model attribute read only.
'''
class Car:
    def __init__(self, brand , model):
        self.__brand = brand              # its now private
        self.__model = model
    
    @property                             # property() function returns the object of the property class and it is used to create the property of a class
    def model(self):
        return self.__model
    
my_car = Car("Tata","Safari")
print(my_car.model)
'''




# 9 Class Inheritance and isinstance() Function
    # DEmonstrate the use of isinstance() to check if my_test is an instance of Car and ElectricCar
'''
class Car:                                         
    def __init__(self , brand , model):            
        self.brand = brand                          
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model} {self.battery_size}"         
    
class ElectricCar(Car):                                          # this is the concept of inheritance used to take reference from parent class here parant class is Car and child class is ElectricCar 
    def __init__(self, brand, model, battery_size):              
      super().__init__(brand, model)
      self.battery_size = battery_size

my_tesla = ElectricCar("tata" , "model", "85km/h")
print(isinstance(my_tesla, Car))                           # used to give true or false # used to check app konsi class ke ho aur instance ho kya
print(isinstance(my_tesla, ElectricCar))                   
'''






# 10 Multiple Inheritance 
    # create two classes Battery and Engine , and let the ElectricCar class inherit from both , demonstrating multiple inheritance

class Car:                                         
    def __init__(self , brand , model):            
        self.brand = brand                          
        self.model = model

class Battery:
    def battery_info(self):
        return " This is battery"
    
class Engine:
    def engine_info(self):
        return " This is engine"

class ElectricCarTwo(Car,Battery,Engine):
    pass

my_tesla = ElectricCarTwo("Tesla", "Model 5")
print(my_tesla.engine_info())
print(my_tesla.battery_info())

    