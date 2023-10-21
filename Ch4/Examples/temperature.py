# This program assists a technician in the process
# of checking a substances temperature

# Create a variable to represent the maximum
max_temp = 102.5

# Get the substances temperature
temperature = float(input("Enter the substance's Celcius temperature: "))

# As long as necessary, instruct the user to
# adjust the thermostat
while temperature > max_temp:
    print("The temperature is too high.")
    print("Turn the thermostat down and wait")
    print("5 minutes. Then take the temperature")
    print("and enter it.")
    temperature = float(input("Enter the new Celcius temperature: "))

# Remind the user to check the temperature again
print("The temperature is acceptable.")
print("Check again in 15 minutes.")