import os
import datetime as dt
from random import choice
import smtplib

my_email = os.environ["EMAIL_ADDRESS"]
my_password= os.environ["EMAIL_PASSWORD"]

now = dt.datetime.now()
day = now.weekday()

# if day == 0::
if day < 7 and day > 0: #this will send the message every time the code is run.
        with open("quotes.txt", mode="r") as quotes_file:
            quotes = quotes_file.read()# I could have used readlines().
            quotes_list = quotes.split("\n")#and I would have had to write this line as they would already be split into a list.
            random_quote = choice(quotes_list)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email,password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="stephenpythontest2025@gmail.com",
                    msg=f"Subject:Quote\n\n{random_quote}"
                )


