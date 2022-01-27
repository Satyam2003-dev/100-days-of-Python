
student_height = input(" enter the height of student in list ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
# print(student_height)

total_height = 0
for height in student_height:
    total_height += height
# print(total_height)

no_of_students = 0
for student in student_height:
    no_of_students += 1
# print(no_of_students)

# total_height = sum(student_height)
# no_of_students = len(student_height)
avg_height = round(total_height / no_of_students)
print(f"average height = {avg_height}")

