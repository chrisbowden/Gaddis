# This will compare a user's answers against the 'correct' answers list
FILENAME = "answers2.txt"
QUESTIONS = 20
PASS_MARK = 0.75
def main():
    # This list represents the correct answers
    correct = ['A','C','A','A','D','B','C','A','C','B','A','D','C','A','B','C','B','B','D','A']

    # Read in the student's answer file
    infile = open(FILENAME, "r")

    # Read in the data into a list
    answers = infile.readlines()
    infile.close()

    # Strip off each of the \n
    index = 0
    while index < len(answers):
        answers[index] = answers[index].rstrip("\n")
        index += 1

    # We now have our two lists. Let's compare them.
    # We will return a list of the incorrect answers (or the index pos)
    incorrect = compare_lists(answers, correct)

    # Now we have a list of incorrect answers, we can do the reporting
    # Pass/Fail, Num  Correct/ Incorrect, List of incorrect
    incorrect_answers = len(incorrect)
    correct_answers = QUESTIONS - incorrect_answers
    if correct_answers / QUESTIONS >= 0.75:
        print ("Congratulations you passed!")
    else:
        print("Sorry, you have failed")
    print ("These are the questions answered incorrectly:")
    print(incorrect)






def compare_lists(list1, list2):
    # Setup an index to loop through
    index = 0
    # Create the list of incorrect answers
    incorrect_response = []

    # User answers first, correct answers second
    for item in range(len(list1)):
        if list1[index] != list2[index]:
            incorrect_response.append(index+1)
        index += 1

    return incorrect_response


main()