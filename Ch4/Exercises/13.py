rows = 7
cols = 7

for row in range(rows, 0, -1):
    for col in range(row):
        print("*", end='')
    print()