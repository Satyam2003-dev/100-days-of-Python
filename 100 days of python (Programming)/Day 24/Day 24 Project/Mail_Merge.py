# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

# list of names
with open("./Input/Names/invited_names.txt", mode='r') as names_file:
    names_list = names_file.readlines()

# Replace [names] placeholder in letter
with open("./Input/Letters/starting_letter.txt", mode='r') as letter_file:
    letter_contents = letter_file.read()
    # print(letter_contents)
    for name in names_list:
        stripped_name = name.strip()
        # print(stripped_name)
        new_letter = letter_contents.replace(PLACEHOLDER,stripped_name)
        # print(new_letter)
        with open(f"./Output/ReadyToSend/Letter_to_{stripped_name}.txt", mode='w') as completed_letter:
            completed_letter.write(new_letter)
