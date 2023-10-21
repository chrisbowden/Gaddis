# This program asks the user to enter rainfall per month
# over a series of years (number of years specified by user
# We will capture total months, total rainfall and average
# for entire period
years = int(input("How many years of rainfall would you like to capture? "))
months = years * 12 # Calc total months to display later
total_rainfall = 0 # Initial value of rainfall (Accumulator)

for year in range (years):
    for month in range(12):
        rainfall = float(input("What is the rainfall in mm for this month: "))
        total_rainfall += rainfall

# Loops finished now, so display the data
print()
print("The number of months was", months)
print("Total rainfall for the period was", total_rainfall)
print("Average monthly rainfall across the period was", total_rainfall/months)
