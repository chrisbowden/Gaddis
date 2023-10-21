# Display the conversion of Celius to Farenheit temps
# for 0 through 20 using loops

print("Celcius\tFahrenheit")
print("------------------")
for c_temp in range(21):
    f_temp = (9/5 * c_temp) + 32
    print(c_temp,"\t\t", format(f_temp, '.1f'))
