
word_list = ["elephant", "baboon", "camel"]

import random

choosen_word = random.choice(word_list)

print(f'the solution word is {choosen_word}')

guess = input("guess a letter: ").lower()

for letter in choosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
