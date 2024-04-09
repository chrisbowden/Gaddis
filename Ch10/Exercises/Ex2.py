# This is the program that controls the speed of the car 
# from the Car class

import car

# Capture the infomration about the car 
year = input('Enter the year and model information: ')
make = input('Enter the make of the vehicle: ')

# Create the car object
mycar = car.Car(year, make)

# Print the current speed of the car
print('The current speed is: ' + str(mycar.get_speed()))

# Call the increase speed method 5 times
for i in range (5):
    mycar.accelerate()

# Print the current speed of the car
print('The current speed is: ' + str(mycar.get_speed()))


