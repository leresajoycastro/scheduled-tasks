# 2. Check if today matches a birthday in the birthdays.csv
import pandas
import datetime as dt
import random
import smtplib
import os


MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

data = pandas.read_csv('birthdays.csv')
records = data.to_dict(orient='records')
date_today = dt.datetime.today()
year = date_today.year
month = date_today.month
day = date_today.day
for i in range(0,len(records)):
    if records[i]['month'] == month and records[i]["day"] == day:
        n = random.randint(1,3)
        with open(f"letter_templates/letter_{n}.txt") as message:
            message_body = message.read()
            message_with_name = message_body.replace("[NAME]", records[i]['name'])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=records[i]['email'],
                msg=f"Subject:Happy Birthday!\n\n{message_with_name}"
            )

