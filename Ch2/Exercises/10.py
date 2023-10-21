# Program that will display required ingredients
# based on how many cookies are desired

# The following measurements are the amount required for 48 cookies
sugar_base = 1.5
butter_base = 1
flour_base = 2.75

cookies_needed = float(input("How many cookies would you like? "))
ratio = cookies_needed / 48
print("You will need the following ingredients:")
print()
print(ratio * sugar_base, "cups of sugar")
print(ratio * butter_base, "cups of butter")
print(ratio * flour_base, "cups of flour")
