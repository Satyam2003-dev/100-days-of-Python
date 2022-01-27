student_score = input(" enter the score of student in list ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
# print(student_score)
# print(max(student_score))         #  WARNING:-  don't use max function

highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score
print(f"the highest score in the class is {highest_score}")
