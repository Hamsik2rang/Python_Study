# Remain times Calculator until 90 years old
# 90살까지는 살겠지?
age = input("What is your current age?")

remain_year = 90 - int(age)

days = (remain_year) * 365
weeks = (remain_year) * 52
months = (remain_year) * 12

print(f"your remain age is {days} days, {weeks} weeks, and {months} months")
