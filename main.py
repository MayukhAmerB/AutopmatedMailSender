import smtplib
import datetime as dt
import pandas
import random
import time
now = dt.datetime.now()
weekday = now.weekday()
my_email = "mayukhofficia@gmail.com"# Enter your mail address
password = "zpteefoprtujqyrj"
cc = []

def Quote_getter():
    # with open(r"C:\Users\MONOJYOTI\PycharmProjects\Automatedmailsender\quotes.txt") as file:
    time.sleep(1500)
    file = pandas.read_csv(r"C:\Users\MONOJYOTI\PycharmProjects\Automatedmailsender\quotes.txt")
    quote_list = file.quotes.tolist()
    quote = random.choice(quote_list)
    return quote


quote_to_send = Quote_getter()


def mail_sender():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="blackbrierpro2@gmail.com", # receiver address
                            msg=f"{cc}subject:Motivation\n\n{quote_to_send}.")


if weekday == 4:
    mail_sender()
