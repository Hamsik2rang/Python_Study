# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15? ")
)
total += total * tip_percentage / 100
people_count = int(input("How many people to split the bill? "))

answer = total / people_count
print(f"Each person should pay: {round(answer,2)}")