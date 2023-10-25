GRAVITY=9.8

def falling_distance(time):
    return 0.5 * GRAVITY * time**2

def main():
    for seconds in range(1,11):
        #print(seconds)
        print(format(falling_distance(seconds), '.1f'),"m", sep='')


main()