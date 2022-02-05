
# Day 16 - Coffee Machine
# Object Oriented Programming

from menu import Menu, MenuItem
from Coffee_Maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    is_On = True
    menu = Menu()
    coffeeMaker = CoffeeMaker()
    moneyMachine = MoneyMachine()

    while is_On:
        choice = input(f"What would you like to order? ({menu.get_items()}): ").lower()
        if choice == "off":
            is_On = False
        elif choice == "report":
            coffeeMaker.report()
            moneyMachine.report()
        else:
            drink = menu.find_drink(choice)
            if coffeeMaker.is_resource_sufficient(drink):
                if moneyMachine.make_payment(drink.cost):
                    coffeeMaker.make_coffee(drink)

main()
