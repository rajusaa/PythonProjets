##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv with dates of persons you wish to send automated b'day wish

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import pandas as pd
import smtplib
import random

MY_EMAIL = 'santoshkumar.skr1@gmail.com'
MY_PASSWORD = '----' # fill in the password 


def sendemail(vname, vemail):
    letter_number = str(random.randint(1, 3))
    letter_file = './letter_templates/' + 'letter_' + letter_number + '.txt'
    with open(letter_file) as file:
        message = file.read()
        new_message = message.replace('[NAME]', vname.title())

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, vemail, msg=f'Subject:Happy Birthday\n\n{new_message}')


today = dt.datetime.now()
today_date = today.date()
today_month = today_date.month
today_day = today_date.day

df = pd.read_csv("birthdays.csv")
for index, row in df.iterrows():
    name = row['name']
    email = row['email']
    check_day = row['day']
    check_month = row['month']
    if check_day == today_day and check_month == today_month:
        sendemail(name, email)
