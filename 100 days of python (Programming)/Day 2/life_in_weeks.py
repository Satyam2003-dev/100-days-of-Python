# no of days , weeks , months , years left in your life if you live 100 years

age = input("Enter your current age ")
age_int = int(age)

years_remaining = 100 - age_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

life = f"you have {days_remaining} days  , {weeks_remaining} weeks , {months_remaining} months  , {years_remaining} years left"
print(life)
