CLASS_A = 20
CLASS_B = 15
CLASS_C = 10

def main():
    print("How many seats of each type were sold?")
    a = int(input("Class A: "))
    b = int(input("Class B: "))
    c = int(input("Class C: "))
    revenue = calc_seats(a, CLASS_A) + calc_seats(b, CLASS_B) + calc_seats(c, CLASS_C)
    print("Total revenue is $", revenue, sep='')

def calc_seats(num_seats, type):
    return num_seats * type

main()
