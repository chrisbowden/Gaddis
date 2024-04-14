# The Mammal class represents a generic mammal

class Mammal:
    # The init accepts species only

    def __init__(self, species):
        self.__species = species

    # The show_species method displays a message 
    # indicating the species
    
    def show_species(self):
        print('I am a', self.__species)

    # The make_sound method is the mammal's 
    # way of making a generic sound

    def make_sound(self):
        print('Grrrrr') 

    
# The Dog class is a subclass of the Mammal class

class Dog(Mammal):

    # The init calls the superclass  passing dog
    # as the species
    def __init__(self):
        Mammal.__init__(self, 'Dog')

    # the make sound overrides the superclass's
    # make sound method
    
    def make_sound(self):
        print('Woof! Woof!')

# The Dog class is a subclass of the Mammal class

class Cat(Mammal):

    # The init calls the superclass  passing dog
    # as the species
    def __init__(self):
        Mammal.__init__(self, 'Cat')

    # the make sound overrides the superclass's
    # make sound method
    
    def make_sound(self):
        print('Meow')
    
