# Calculates the percentage of males and females in  a class
males = int(input("How many males in the class? "))
females = int(input("How many females in the class? "))

total = males + females
print("The percentage of females is:", format(females/total*100, '.0f'))
print("The percentage of males is:", format(males/total*100, '.0f'))
