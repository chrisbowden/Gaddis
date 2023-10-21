# Displays a rectangular patter of 8 rows by 6 stars
rows = int(input("How many rows? "))
cols = int(input("How many columns? "))

for r in range(rows):
    for c in range(cols):
        print('*', end='')
    print()
