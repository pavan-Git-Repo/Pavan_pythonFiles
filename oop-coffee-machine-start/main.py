from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

machine_on = True

while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options} : ")
    if choice == 'off':
        machine_on = False
        print("Machine Turning Off...")
    elif choice == 'report':
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # print(drink)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # print(coffe_maker.is_resource_sufficient(drink))
            coffe_maker.make_coffee(drink)



# money_machine.report()
# coffe_maker.report()

# money_machine = MoneyMachine()
# coffe_maker = CoffeeMaker()
# menu = Menu()
#
#
#
#
# turn_on_off = input("Please press 'on' to turn or 'off' to turn of the machine : ")
# machine_on = None
# if turn_on_off == 'on':
#     machine_on = True
#     print("*** Welcome to the Cafe Coffee Day ***")
#     print("Machine Turned On...")
#     print("Have a nice day")
# elif turn_on_off == 'off':
#     machine_on = False
#     print("Machine Turning off...")
# while machine_on:
#     options = menu.get_items()
#     choice = input("What would you like, espresso/latte/cappuccino? : ")
#     if choice == 'off':
#         machine_on = False
#         print("Machine Turning Off....")
#     elif choice == 'report':
#         coffe_maker.report()
#         money_machine.report()
#     else:
#         drink_name = menu.find_drink(choice)
#         if coffe_maker.is_resource_sufficient(drink_name) and money_machine.make_payment(drink_name.cost):
#             coffe_maker.make_coffee(drink_name)


