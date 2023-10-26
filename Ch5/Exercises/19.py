

def future_value(pv, rate, months):
    f_value = (1+rate)**months * pv
    return f_value

def main():
    present = float(input("What is the present value of your account: "))
    interest = float (input("What is the expected monthly interest rate: "))
    time = int(input("How many months for the investment: "))

    print ("The future value of your investment is $", future_value(present,interest,time), sep='')

main()