#       Body Mass Index(B.M.I.) Calculator

height = float(input("Enter your height in meter "))
weight = float(input("Enter your body weight in kg "))

bmi = round(weight / height ** 2)

if bmi <= 18:
    print(f"your BMI is {bmi}, you are Underweight")
elif bmi <= 25:
    print(f"your BMI is {bmi}, you are Normal")
elif bmi <= 30:
    print(f"your BMI is {bmi}, you are Overweight")
elif bmi <= 35:
    print(f"your BMI is {bmi}, you are Obese")
else:
    print(f"your BMI is {bmi}, you are  clinically Obese")
