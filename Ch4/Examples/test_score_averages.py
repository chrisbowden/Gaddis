# This program averages test scores. It asks the user
# for the number os students

num_students = int(input("How many students do you have? "))
num_test_scores = int(input("How many test scores per student? "))

# Determine each students average score
for student in range(num_students):
    # Init the accumulator
    total = 0.0

    print("Student number", student + 1)
    print("----------------")
    for test_num in range(num_test_scores):
        print("Test number", test_num +1, end='')
        score = float(input(": "))
        total += score
    # Calc the average score
    average = total / num_test_scores

    # Display the average
    print("The average for student number", student+1, "is:", average)
    print()
