
from datetime import datetime
import smtplib
import random
import pandas

my_email = ""
password = ""

'''Check if today matches a birthday in the birthdays.csv'''
today = datetime.now()
today_tuple = (today.month, today.day)

'''pandas Dataframe and list comprehension'''
birthday_dataframe = pandas.read_csv("birthdays.csv")
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in birthday_dataframe.iterrows()}
# print(birthday_dict)

'''Check if anyone's bday'''
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!!!!\n\n{contents}")






