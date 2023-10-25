LABOUR_PER_HOUR = 35
FEET_PER_GALLON = 112
LABOUR_PER_112FEET = 8

def main():
    sq_feet = float(input("Enter the number of Sq Feet to be painted: "))
    paint_per_gallon = float(input("Enter the cost per gallon of paint: "))
    paint_required = sq_feet / FEET_PER_GALLON
    labour = sq_feet/112 * LABOUR_PER_112FEET
    paint_cost = calc_cost(paint_required, paint_per_gallon)
    labour_cost = calc_cost(labour, LABOUR_PER_HOUR)
    total = paint_cost+labour_cost

    print("The job cost will be:")
    print("Number of gallons required:", paint_required)
    print("Labour Hours Required:", labour)
    print("Paint Cost $", paint_cost, sep='')
    print("Labour Cost $", labour_cost, sep='')
    print("Total Cost $", total, sep='')
def calc_cost(num1, num2):
    return num1*num2



main()
