def main():
    # Pass a string to the show_mammal_info
    show_mammal_info('I am a string')

# The show_mammal_info accepts and object

def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()

main()
