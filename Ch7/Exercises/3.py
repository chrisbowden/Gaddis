# Capture rainfall for each of the 12 months
# then display total, average and min/max entries

def main():

    rainfall = []
    print("Enter rainfall (in mm) for each month.")
    print()
    for i in range(12):
        print("Enter rainfall for Month #", i+1, ": ", sep='',end='')
        rain = float(input())
        rainfall.append(rain)


    total = 0
    for item in rainfall:
        total += item

    max_value = max(rainfall)
    min_value = min(rainfall)
    average = total / len(rainfall)

    print("The total rainfall is: ", total)
    print("The average rainfall is: ", average)
    print("The maximum rainfall is: ", max_value)
    print("The minimum rainfall is: ", min_value)

main()