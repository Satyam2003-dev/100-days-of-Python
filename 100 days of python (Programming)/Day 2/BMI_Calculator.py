#       Body Mass Index(B.M.I.) Calculator

height = input("Enter your height in meter")
weight = input("Enter your body weight in kg")

bmi = int(weight) / float(height) ** 2
bmi_int = int(bmi)

if(bmi_int <= 18):
    print(f"your BMI is {bmi_int} you are Underweight")
elif(bmi_int > 18 and bmi_int <= 25):
    print(f"your BMI is {bmi_int} you are Normal")
elif(bmi_int > 25 and bmi_int <= 30):
    print(f"your BMI is {bmi_int} you are Overweight")
else:
    print(f"your BMI is {bmi_int} you are Obese")
