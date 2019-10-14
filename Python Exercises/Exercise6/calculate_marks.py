def calculate_marks(solutions, students_answers):
    id_questions = list(solutions.keys())
    ret = {}  # Dictionary to be returned
    #   Iterate from student to student
    for student in students_answers:
        mark = 0
        print("\nStudent ID: {0} ------------".format(student))
        print("Student {0} answers: {1}".format(student, students_answers[student]))
        #   Iterate through student answers
        for answer_key in students_answers[student]:
            print("Student answer to question {0}: {1}".format(answer_key, students_answers[student][answer_key]))
            if not (answer_key in id_questions):
                print(
                    "Question ID {0} is not in the answer sheet, valid IDs are: {1}".format(answer_key, id_questions))
                pass
            elif students_answers[student][answer_key] == solutions[answer_key]:
                print ("Answer to question {0} is {1}. +1".format(answer_key, students_answers[student][answer_key]))
                mark += 1
            else:
                print ("Answer to question {0} is {1}. -0.25".format(answer_key, solutions[answer_key]))
                mark -= 0.25

        print ('\nSTUDENTS\' MARKS')
        ret[student] = mark

    return ret


if __name__ == "__main__":
    """Sample main to test functionality. Compute the marks of a couple of students"""
    print(calculate_marks({1: 'a', 2: 'b'}, {1: {1: 'a', 2: 'c'}, 2: {1: 'b', 2: 'b'}}))
