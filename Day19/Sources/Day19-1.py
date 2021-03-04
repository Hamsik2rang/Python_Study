# Send Quote on monday using smtplib
import random as rand
from datetime import datetime
import smtplib

EMAIL = "lvhi7121@gmail.com"
PASSWORD = "SECRET"
MONDAY = 1

with open("./Day19/Resources/quotes.txt", "r") as f:
    quotes = f.readlines()

    local_now = datetime.now()
    weekday = local_now.weekday()
    if weekday == MONDAY:
        with smtplib.SMTP("smtp.gmail.com") as smtp:
            smtp.starttls()
            smtp.login(user=EMAIL, password=PASSWORD)
            smtp.sendmail(
                from_addr=EMAIL,
                to_addrs="lvhi0607@naver.com",
                msg=f"Subject:This Monday's Quote\n\n{rand.choice(quotes)}",
            )
    else:
        pass
