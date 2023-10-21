# Asks user for mass and calculate weight
# If > 500 or < 100 newtons display error

mass = float(input("Enter the mass of the object: "))
weight = mass * 9.8

if weight > 500:
    print("The object is too heavy")
if weight < 100:
    print("The object is too light")

