
print("Welcome the Roller Coaster")
height = int(input("enter your height in cm "))

if height >= 120:
    print("you can ride the Roller coaster ")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 70
        print("please pay Rupees 70")
    elif age > 12 and age <= 18:
        bill = 100
        print("Please pay rupees 100")
    elif age >=45 and age <= 55:
        bill = 0
        print("Congrats you can ride on this Roller Coaster Free")
    else:
        bill = 150
        print("Please pay Rupees 150")

    photo = input("Want to take photo? Y or N ")
    if photo == "Y" or photo == "y":
        bill += 30

    print(f"your final bill is {bill}")
else:
    print("Sorry! You can't ride the Roler Coaster, first you need to grow taller ")
