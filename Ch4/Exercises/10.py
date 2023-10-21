tuition = 8000
print("Year\tTuition")
print("---------------")
for year in range(1,6):
    print(year, "\t\t", format(tuition, ',.2f'))
    tuition *= 1.03
