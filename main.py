import random
import smtplib
import datetime as dt

my_email = "masonputney@gmail.com"
to_email = "support@itsolutionsco.com"
password = "bzrnfduvtefxfkof"

now = dt.datetime.now()
weekday = now.weekday()


def send_email():
    with open("quotes.txt") as data_txt:
        quotes = []
        for line in data_txt:
            quotes.append(line)
        random_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, to_addrs=my_email,
            msg="Subject:Monday Motivation\n\n"
                f"{random_quote}")


if weekday == 1:
    send_email()
