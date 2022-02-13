
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# # another method of reading
#
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Writing the file

# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text")

# creating new file
with open("created_file.txt", mode="w") as file:
    file.write("\nNew text")
