# This program calculates a retail items sale price

# DISCOUNT_PERCENTAGE is a global constant
DISCOUNT_PERCENTAGE = 0.20

# The main function
def main():
    # Get item's regular price
    reg_price = get_regular_price()

    # Calc sale price
    sale_price = reg_price - discount(reg_price)

    # Display sale price
    print("The sale price is $", format(sale_price, ',.2f'), sep='')

def get_regular_price():
    price=float(input("Enter the item's regular price: "))
    return price

def discount(price):
    return price * DISCOUNT_PERCENTAGE

main()
