# This program gets three test scores and displays
# their average. It congratulates the user if the
# score is a high score

high_score = 95

# Capture the three test scores
test1 = int(input("Enter the score for test 1:"))
test2 = int(input("Enter the score for test 2:"))
test3 = int(input("Enter the score for test 3:"))

# Calculate the average
average = (test1 + test2 + test3) / 3

# Print the average
print("The average score is", average)

# If the average is a high score,
# congratulate the user

if average >= high_score:
    print("Congratulations!")
    print("That is a great score!")
