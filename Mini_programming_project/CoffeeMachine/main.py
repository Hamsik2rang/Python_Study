MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(menu_info, resources, selected_menu):
    if (
        "money" not in resources
        or resources["money"] < menu_info[selected_menu]["cost"]
    ):
        return False
    else:
        return True


def process_coins():
    pennies = int(input("How many pennies?: "))
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    return coins_to_dollars(pennies, nickles, dimes, quarters)


def coins_to_dollars(pennies, nickles, dimes, quarters):
    return round(pennies * 0.01 + nickles * 0.05 + dimes * 0.1 + quarters * 0.25, 1)


def serve_coffee(select, menu_info, resources):
    change = round(resources["money"] - menu_info[select]["cost"], 1)
    print(f"Here's ${change} in change.")
    print(f"Here's your {select}. Enjoy!")
    resources["money"] -= menu_info[select]["cost"]
    if "water" in menu_info[select]["ingredients"]:
        resources["water"] -= menu_info[select]["ingredients"]["water"]
    if "milk" in menu_info[select]["ingredients"]:
        resources["milk"] -= menu_info[select]["ingredients"]["milk"]
    if "coffee" in menu_info[select]["ingredients"]:
        resources["coffee"] -= menu_info[select]["ingredients"]["coffee"]

    round(resources["money"], 1)


while True:
    select = input("  What would you like? (espresso/latte/cappuccino): ").lower()
    if select == "off":
        break
    elif select == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        if "money" not in resources:
            resources["money"] = 0
        print(f"Money: {resources['money']}$")
        continue
    else:
        if check_resources(MENU, resources, select):
            serve_coffee(select, MENU, resources)
            continue

        print(f"Please insert coins.")
        input_coins = process_coins()
        if "money" in resources:
            resources["money"] += input_coins
        else:
            resources["money"] = input_coins

        if check_resources(MENU, resources, select):
            serve_coffee(select, MENU, resources)
        else:
            print("Sorry that's not enough money. Money refund.")
            resources["money"] = 0
