height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# Write your code below this line 👇
bmi = round(int(weight) / float(height) ** 2)

if 18.5 > bmi:
    print("You are underweight.")
elif 25 > bmi:
    print("You have normal weight.")
elif 30 > bmi:
    print("You are overweight.")
elif 35 > bmi:
    print("You are obese.")
else:
    print("You are cinically obese.")