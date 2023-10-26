

def is_prime(num):
    for i in range (2,num):
        if num > 2 and num % i == 0:
            return True

def main():
    for number in range (1,101):
        if is_prime(number):
            print(number ,"is NOT prime")
        else:
            print(number, "is prime!")

main()