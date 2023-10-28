# Calculation of gross pay

def main():
    # Get hours worked
    hours = int(input("How many hours did you work? "))
    pay_rate = float(input("Enter your hourly pay rate: "))

    # Calc Gross pay
    gross_pay = hours * pay_rate

    # Display
    print("Gross pay: $", format(gross_pay, ",.2f"), sep="")


main()
