'''Old way'''
# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)

'''Python Sequences: list, range, string, tuple'''

'''Using list comprehension'''
'''new_list = [new_item for item in numbers]'''
# new_list = [n+1 for n in numbers]
# print(new_list)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [num*2 for num in range(1,5)]
# print(new_list)

'''Conditional List Comprehension'''
'''new_list = [new_item for item in item_list if condition]'''
# names_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names_list = [name for name in names_list if len(name)<5]
# print(short_names_list)
# long_names_list = [name.upper() for name in names_list if len(name)>5]
# print(long_names_list)
'''only even numbers'''
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# even_numbers_list = [num for num in numbers if num%2==0]
# print(even_numbers_list)

'''result which contains the numbers that are common in both files.'''
# result = []
# with open("file1.txt") as file1_data:
#     file1 = file1_data.readlines()
# with open("file2.txt") as file2_data:
#     file2 = file2_data.readlines()
# result = [int(num) for num in file1 if num in file2]
# print(result)

"""Dictionary Comprehension"""
'''new_dict = {new_key:new_value for (key,value) in dict.item()}'''
# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_score = {student:random.randint(1,100) for student in names}
# print(students_score)
# passed_students = {student:score for (student,score) in students_score.items() if score >= 60}
# print(passed_students)

'''Takes each word in the given sentence and calculate the number of letters in each word.'''
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# sentence = sentence.split()
# print(sentence)
# result = {word:len(word) for word in sentence}
# print(result)

'''Takes each temperature in degrees Celsius and converts it into degrees Fahrenheit'''
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # (temp_c * 9/5) + 32 = temp_f
# weather_f = {day:(temp_c*9/5+32) for (day,temp_c) in weather_c.items()}
# print(weather_c)

'''Looping through dataframe'''
import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98],
}
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
'''Loop through Data Frame using iterrows()'''
for (index, row) in student_data_frame.iterrows():
    # print(row.score)
    # print(row)
    if row.student == "Angela":
        print(row)
