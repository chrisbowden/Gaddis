# Prime number checker
# Ask user to enter a number and use a function
# check prime to determine if its prime or not
# Primes are only divisible by itself and 1

def is_prime(num):
    for i in range (2,num):
        if num % i == 0:
            return True

def main():
    my_number = int(input("What number would you like to check for primness? "))
    result = is_prime(my_number)
    if result:
        print("The number is not prime")
    else:
        print("Number is prime")

main()
