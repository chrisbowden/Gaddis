rise_rate = 1.6
num_years = 25

print("Year\tRise(mm)")
print("----------------")
for year in range(num_years):
    rise = (year+1)* rise_rate
    print(year+1, "\t", format(rise, '.1f'))
    #print(i)
