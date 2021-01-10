# Judging leap year program
year = int(input("Which year do you want to check? "))
"""
윤년 = 4로 나누어 떨어지되 100으로 나누어 떨어지지 않는 해, 혹은 400으로 나누어 떨어지는 해
"""

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print("Leap year.")
else:
    print("Not leap year.")