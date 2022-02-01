

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            # the "else:" clause isn't really needed for these
            return False
        return True
    return False


# assuming proper inputs for these, i.e. months in range 1-12 else it gives error index out of range
def days_in_month(year, month):
    if year < 1:
        return "invalid input, check your input again."
    if month > 12 or month < 1:
        return "invalid input, check your input again."
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # for February in a leap year
    if month == 2 and is_leap(year):
        # avoiding hard-coding the number
        return month_days[1] + 1
    # no need for the "else:" bit here either
    return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
