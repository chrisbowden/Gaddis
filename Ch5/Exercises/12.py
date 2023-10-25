# Program takes two values, and returns the larger of the values

def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def main():
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))
    larger = max(first,second)
    print("The larger number is", larger)

main()