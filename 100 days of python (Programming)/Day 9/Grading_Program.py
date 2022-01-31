
student_score = {
    "Harry": 95,
    "Ron": 85,
    "Hermione": 96,
    "Draco": 75,
    "Neville": 62,
}

student_grades = {}
for student in student_score:
    score = student_score[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Very Good"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)
