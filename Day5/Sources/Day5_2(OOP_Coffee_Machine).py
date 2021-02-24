from Menu import Menu, MenuItem
from Coffee_Maker import CoffeeMaker
from Money_Machine import MoneyMachine


class CoffeeMachine:
    """1. print report
    2. check resources sufficient
    3. process coins
    4. check transaction successful
    5. make coffee"""

    def __init__(self):
        self.coffee_maker = CoffeeMaker()
        self.menu = Menu()
        self.money_machine = MoneyMachine()
        self.is_on = True
        self.process()

    def process(self):

        while self.is_on:
            options = self.menu.get_items()
            choice = input(f"What would you like? ({options}): ")
            choice = choice.lower()
            if choice == "off":
                self.is_on = False
            elif choice == "report":
                self.coffee_maker.report()
                self.money_machine.report()
            else:
                drink = self.menu.find_drink(choice)
                is_enough_ingredients = self.coffee_maker.is_resource_sufficient(drink)
                is_payment_successful = self.money_machine.make_payment(drink.cost)
                if is_enough_ingredients and is_payment_successful:
                    self.coffee_maker.make_coffee(drink)


coffee_machine = CoffeeMachine()