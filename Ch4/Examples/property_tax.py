# This program displays property taxes

tax_factor = 0.0065

# Get the first lot number
print("Enter the property lot number")
print("or enter 0 to end.")
lot = int(input('Lot Number: '))

# Continue processing as long as the user does not
# enter lot number 0
while lot != 0:
    # Get the property value
    value = float(input("Enter the property value: "))

    # Calculate the tax
    tax = value * tax_factor

    # Display the tax
    print("Property tax: $", format(tax, ',.2f'), sep='')

    # Get the next lot number
    print("Enter the next lot number")
    print("or enter 0 to end.")
    lot = int(input('Lot Number: '))
