# This program converts the speeds 60 through 130
# to MPH

start_speed = 60
end_speed = 131
increment = 10
conversion_factor = 0.6214

# Print the table headings
print("KPH\t\tMPH")
print("-----------")

# Print the speeds
for kph in range(start_speed, end_speed,increment):
    mph = kph * conversion_factor
    print(format(kph, '3'), '\t', format(mph, '.1f'))
