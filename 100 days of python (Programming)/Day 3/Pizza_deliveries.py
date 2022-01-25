
print("""_               __        __ 
   ___  (_)_____ ___ _  / /  __ __/ /_
  / _ \/ /_ /_ // _ `/ / _ \/ // / __/
 / .__/_//__/__/\_,_/ /_//_/\_,_/\__/ 
/_/               """)


size = input("What size of pizza you want? S, M , L ")
pepperoni = input("Want to add Pepporoni? Y or N ")
extra_cheese = input("Want to add extra cheese? Y or N ")

bill = 0

if size == "S" or size == "s":
    bill += 100
elif size == "M" or size == "m":
    bill += 150
elif size == "L" or size == "l":
    bill += 200

if pepperoni == "Y" or pepperoni == "y":
    if size == "S" or size == "s":
        bill += 20
    else:
        bill += 30

if extra_cheese == "Y" or extra_cheese == "y":
    bill += 50


print(f"your final bill is rupees {bill}")
