import smtplib
import random
import datetime as dt

my_email='santoshkumar.skr1@gmail.com'
password='$Barney123'
to_email='santoshkumar.skr1@yahoo.com'

current = dt.datetime.now()
current_day = current.weekday()
if current_day == 1:
    with open('quotes.txt','r') as data:
        quotes = data.readlines()
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            my_email,
            to_email,
            msg=f'Subject:Motivational Quotes\n\n{random.choice(quotes)}'
        )
        connection.close()
