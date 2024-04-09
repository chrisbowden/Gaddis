# The automobile class holds general data
# about an automobile in inventory

class Automobile:
    # The __init__ method accepts arguments for the
    # make, model, mileage and price. It initialises 
    # the data attributes with these values

    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    # The following methods are mutators for the
    # class data attributes
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    # The follwoing are accessors for 
    # the classes data attributes
            
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_mileage(self):
        return self.__mileage
    def get_price(self):
        return self.__price
        

# The Car class represents a car. It is a subclass
# of the Automobile class
class Car(Automobile):
    # The __init__ method accepts arguments for the
    # car's make, model, mileage, price and doors.

    def __init__(self, make, model, mileage, price, doors):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note we also have 
        # to pass self as an argument
        
        # This was the vscode suggested: super().__init__(make, model, mileage, price)    
        Automobile.__init__(self, make, model, mileage, price)

        # Initialise the doors attribute
        self.__doors = doors

    # The set doors method is the mutator for the doors
    def set_doors(self, doors):
        self.__doors = doors

    # THe doors accessor
    def get_doors(self):
        return self.__doors
    
# The Truck class represents a pickup truck. It is a 
# subclass of the automobile class
    
class Truck(Automobile):
    # The init method needs attributes for all of the 
    # Autombile attributes, plus the truck specific 
    # drive type
    def __init__ (self, make, model, mileage, price, drive_type):
        # Call the super type and it's init method
        Automobile.__init__(self, make, model, mileage, price)

        # init the Drive type attributes
        self.__drive_type = drive_type

    # Create the set drive type method
    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    def get_drive_type(self):
        return self.__drive_type

# The SUV class represents a sports utility vehicle
# and is a subclass of the Autommobile class

class SUV(Automobile):
    def __init__(self, make, model, mileage, price, pass_cap):
        # Call the superclass first
        Automobile.__init__(self, make, model, mileage, price)

        # init the Passenger Capacity attribute
        self.__pass_cap = pass_cap

    # Mutator
    def set_pass_cap(self, __pass_cap):
        self.__pass_cap = __pass_cap

    # Accessor
    def get_pass_cap(self):
        return self.__pass_cap
    
    


