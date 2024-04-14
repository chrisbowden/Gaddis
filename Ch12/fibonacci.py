# The program uses recursion to print numbers
# from the Fibonacci sequence

def main():
    print('The first 10 numbers in the')
    print('Fibonacci sequence series.')

    for number in range(1,11):
        print(fib(number))

# The fib function returns the nth number
# in the Fibonacci series

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Main
main()

