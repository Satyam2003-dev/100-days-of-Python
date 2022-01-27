#   Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Python Password Generator")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

#    easy level

# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
#
# for char in range(1, nr_letters + 1):
#     password += random.choice(symbols)
#
# for char in range(1, nr_letters + 1):
#     password += random.choice(numbers)
# print(password)


#   Hard Level

password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_letters + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_letters + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"your password is {password}")
