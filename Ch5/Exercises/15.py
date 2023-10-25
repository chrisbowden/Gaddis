

def calc_average(num1,num2,num3,num4,num5):
    return (num1+num2+num3+num4+num5)/5

def determine_grade(grade):
    if grade >=90:
        letter_grade = "A"
    elif grade >=80:
        letter_grade = "B"
    elif grade >=70:
        letter_grade = "C"
    elif grade >=60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade

def main():
    print("Enter your 5 test scores:")
    score1 = int(input("Test 1 Score: "))
    score2 = int(input("Test 2 Score: "))
    score3 = int(input("Test 3 Score: "))
    score4 = int(input("Test 4 Score: "))
    score5 = int(input("Test 5 Score: "))

    average = calc_average(score1,score2,score3,score4, score5)

    print("Your average score is", average)
    print("Your grade is", determine_grade(average))

main()