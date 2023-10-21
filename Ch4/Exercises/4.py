speed = int(input("What is the speed of the vehicle in kph? "))
time = int(input("How many hours has it travelled? "))
print("Hour\tDistance Traveled")
print("-------------------------")
for hour in range(time):
    print(hour+1,'\t\t', (hour+1) * speed)
