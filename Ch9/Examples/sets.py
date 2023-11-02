# Demo of various set operations
baseball = set(["Jodi", "Carmen", "Aida", "Alicia"])
basketball = set(["Eva", "Carmen", "Alicia", "Sarah"])

# Display members of the baseball set
print("The following students are on the baseball team: ")
for name in baseball:
    print(name)

# Members of the basketball team
print("The following students are on the basketball team: ")
for name in basketball:
    print(name)

# Demo intersection
print()
print("The following students play both: ")
for name in baseball.intersection(basketball):
    print(name)

# Demo Union
print()
print("The following people play either sports: ")
for name in baseball.union(basketball):
    print(name)

# Difference
print()
print("These people play baseball but not basketball")
for name in baseball.difference(basketball):
    print(name)

print()
print("These people play basketball but not baseball")
for name in basketball.difference(baseball):
    print(name)


# Symmetric Difference
print()
print("These people play one sport, but not both")
for name in baseball.symmetric_difference(basketball):
    print(name)


