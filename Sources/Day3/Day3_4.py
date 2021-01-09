print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Write your code below this line 👇
price_small = 15
price_medium = 20
price_large = 25
price_add_pepperoni_to_small = 2
price_add_pepperoni_to_else = 3
price_add_cheese = 1

total_price = 0

if size == "L":
    total_price = price_large
    if add_pepperoni == "Y":
        total_price += price_add_pepperoni_to_else
    if extra_cheese == "Y":
        total_price += price_add_cheese
elif size == "M":
    total_price = price_medium
    if add_pepperoni == "Y":
        total_price += price_add_pepperoni_to_else
    if extra_cheese == "Y":
        total_price += price_add_cheese
elif size == "S":
    total_price = price_small
    if add_pepperoni == "Y":
        total_price += price_add_pepperoni_to_small
    if extra_cheese == "Y":
        total_price += price_add_cheese

print(f"Your final bill is: ${total_price}")