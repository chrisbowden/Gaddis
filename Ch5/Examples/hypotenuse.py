import math

def main():
    # Get the length of the triangle's two sides
    a = float(input("Enter the length of side A: "))
    b = float(input("Enter the length of side B: "))

    # Calc the hypotenuse
    c = math.hypot(a,b)

    print("The length of the hypotenuse is", c)

main()