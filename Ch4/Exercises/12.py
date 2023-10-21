organisms = int(input("Starting number of organisms: "))
daily_increase = int(input("Average daily increase: "))
days = int(input("Number of days to multiply: "))
daily_increase = (daily_increase / 100) +1 # Convert the input value to the maths value

print("Day Approximate\t\tPopulation")
print("------------------------------")

for day in range(days):
    print(day+1, "\t\t\t\t\t", format(organisms, ',.3f'))
    organisms *= daily_increase
