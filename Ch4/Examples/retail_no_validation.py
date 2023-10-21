# Retail Price Calculator

mark_up = 2.5
another = 'y'

# Process on or more items
while another == 'y' or another == 'Y':
    # Get the wholesale cost
    wholesale = float(input("Enter the item's wholesale cost: "))

    retail = wholesale * mark_up

    print("Retail price: $", format(retail, ',.2f'))

    another = input("Do you have another item (enter y for yes): ")
    
