import random

test_seed = int(input("create a seed number "))
random.seed(test_seed)

names_as_csv = input(" give everybody's name ")
names = names_as_csv.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items - 1)

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to pay today's meal bill of us")
