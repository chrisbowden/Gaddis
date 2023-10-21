# variables to represent the base hours and
# the overtime multiplier
base_hours = 40
ot_multiplier = 1.5  # Overtime multiplier

# Get hours worked and pay rates
hours = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the hourly pay rate: "))

# Calculate and display gross pay
if hours > base_hours:
    # First calculate the number of overtime hours
    overtime_hours = hours - base_hours

    # Calculate overtime pay
    overtime_pay = overtime_hours * pay_rate * ot_multiplier

    # Calculate gross pay
    gross_pay = base_hours * pay_rate + overtime_pay
else:
    gross_pay = hours*pay_rate

# Display the gross pay
print("The gross pay is $", format(gross_pay, ',.2f'), sep="")

