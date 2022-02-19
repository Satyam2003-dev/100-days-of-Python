
'''FileNotFOUND error'''
# with open ("a_file.txt") as file:
#     file.read()

'''Key Error'''
# a_dictionary = {"key": "value"}
# a_value = a_dictionary["non_existent_key"]

'''Index Error'''
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

'''Type Error'''
# text = "abc"
# print(text + 5)

'''try, except, else, finally'''
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     a_value = a_dictionary["non_existent_key"]
# except FileNotFoundError:
#     # if fail, create a new file
#     file = open("a_file.txt", 'w')
#     file.write("Something")
# except KeyError as error_message:
#     print("That key does not exist")
# else:
#     # If everything works!
#     content = file.read()
#     print(content)
# finally:
#     # will run no matter what happens
#     file.close()
    
'''Raise error example'''
# height = float(input("Height: "))
# weight = int(input("Weight: "))
# if height > 3:
#     # allows up to raise our own exceptions
#     raise ValueError("Human height should not be over 3 meters")
# bmi = weight / height ** 2
# print(bmi)

'''IndexError: If the user enters something that is out of range just print a default output of "Fruit pie"'''
# fruits = ["Apple", "Pear", "Orange"]
# def make_pie(index):
#     try:
#       fruit = fruits[index]
#     except IndexError:
#       print("Fruit pie")
#     else:
#       print(fruit + " pie")
# make_pie(4)

'''KeyError: Posts without any likes can be counted as 0 likes.'''
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]
total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass
print(total_likes)