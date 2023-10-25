CARB_RATE = 4
FAT_RATE = 9

def main():
    fat = int(input("How many grams of fat per day: "))
    carbs = int(input("How many grams of carbs per day: "))
    total_cals = calc_cals(fat, FAT_RATE) + calc_cals(carbs, CARB_RATE)
    print("Total calories is:", total_cals)

def calc_cals(grams, type):
    return grams * type

main()