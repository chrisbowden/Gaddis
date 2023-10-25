# Calculating of pay
def main():
    #Get amount of sales
    sales = get_sales()

    # Get amount of advanced pay
    advanced_pay = get_advanced_pay()

    # Determine the correct commission rate
    comm_rate = determine_comm_rate(sales)

    # Calculate pay
    pay = sales * comm_rate - advanced_pay

    # Display the amount of pay
    print("The pay is $", format(pay, ',.2f'), sep = '')

    # Determine if the pay is negative
    if pay < 0:
        print("The salesperson must reimburse")
        print("the company.")


# Get Sales function
def get_sales():
    monthly_sales = float(input("Enter the monthly sales: "))
    return monthly_sales

# Advance pay function
def get_advanced_pay():
    print("Enter the amount of advanced pay, or")
    print("enter 0 if no advanced pay was given.")
    advanced = float(input("Advanced pay: "))

    return advanced

# Determine commission rate function
def determine_comm_rate(sales):
    if sales < 10000.00:
        rate = 0.10

    elif sales >= 10000 and sales <= 14999.99:
        rate = 0.12

    elif sales >= 15000 and sales <= 17999.99:
        rate = 0.14

    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16

    else:
        rate = 0.18

    return rate

main()

