

def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity**2

def main():
    m = float(input("What is the object's mass? "))
    v = float(input("What is the object's velocity? "))
    energy = kinetic_energy(m,v)
    print("The object's kinetic energy is", energy)

main()
