total = 0
for r in range(10):
    print("Please enter number ", r+1, ": ", sep='', end='')
    number = int(input())
    total += number

print("The total of your numbers is:", total)