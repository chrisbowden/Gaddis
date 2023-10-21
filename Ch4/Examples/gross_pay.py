# Thsi program displays the gross pay
# get the hours worked
hours = int(input("Enter the hours worked this week: "))

# Get the hourly rate
pay_rate = float(input("Enter the hourly pay rate: "))

# Calculate the gross pay
gross_pay = hours*pay_rate

# Display he gross pay
print("Gross pay: $", format(gross_pay, ',.2f'))
