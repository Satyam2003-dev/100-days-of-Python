
# import smtplib

# '''
# Gmail       smtp.gmail.com
# Hotmail     smtp.live.com
# Yahoo       smtp.yahoo.com
# '''

# # Need to modify security settings of yahoo
# my_email = "afe4ther@gmail.com"
# receiving_email = "afe4ther@yahoo.com"
# password = "fbjhaxc5"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # Transport Layer Security: secures connection
#     connection.starttls()
#     # Login and send message
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs=receiving_email, 
#                         msg="Subject:Happy Birthday!\n\nThis is the body of my email! Happy Birthday")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_the_week = now.weekday()
print(f"Datetime object type: {type(now)}")
print(f"now.year object type: {type(year)}")
print(f"Day of the week: {day_of_the_week}")

date_of_birth = dt.datetime(year=1995,month=11,day=13)
print(f"Date of Birth: {date_of_birth}")