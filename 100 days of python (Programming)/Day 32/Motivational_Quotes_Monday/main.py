
import datetime as dt
from email import message
import random
import smtplib

'''Send email'''
my_email = ""
password = ""

'''Get day of the week'''
now = dt.datetime.now()
week_day = now.weekday()

if week_day == 0:
    '''Get quotes from quote.txt'''
    with open("quotes.txt", mode='r') as file:
        all_quotes = file.readlines()
        quote_to_send = random.choice(all_quotes)
        print(quote_to_send)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Secures connection
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject: Monday Motivation\n\n{quote_to_send}")
