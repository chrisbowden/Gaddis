# Program asks user for length and width of two rectangles
# and displays which one is bigger

length1 = int(input("Enter the length of rectangle 1: "))
width1 = int(input("Enter the width of rectangle 1: "))
length2 = int(input("Enter the length of rectangle 2: "))
width2 = int(input("Enter the width of rectangle 2: "))

# Calculate the two areas
area1 = length1*width1
area2 = length2*width2

if area1>area2:
    print("Rectangle 1 is larger")
elif area1<area2:
    print("Rectangle 2 is larger")
else:
    print("The rectangles are the same size")
