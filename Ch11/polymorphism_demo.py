# This program demonstrates polymorphism

import animals

def main():
    # Create three objects, Mammal, Dog and Cat
    mammal = animals.Mammal('Regular Animal')
    dog = animals.Dog()
    cat = animals.Cat()

    # Display infomrmation about each
    print('Here are some animals and')
    print('the sounds they make.')
    print('---------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)

# The show_mammal_info function accepts an object
# as an argument, and calls its show_species
# and make_sound methods
def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()

# Call the main function
main()
