# Day 2 Project " Tip Calculator "

print("Welcome to tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("how much tip you want to give, 0% , 5% , 8% ,10% "))
people = int(input("how many people you have to split the bill "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"each person should pay {final_amount}")
