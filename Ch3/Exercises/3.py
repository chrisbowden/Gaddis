# Age Classifier
age = int(input("What is your age: "))

if age >= 20:
    print("You are an adult")
elif age >=13 and age <20:
    print("You are a teenager")
elif age > 1 and age < 13:
    print("You are a child")
else:
    print("You are an infant")