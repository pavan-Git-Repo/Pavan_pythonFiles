
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu_obj=Menu()
money_obj=MoneyMachine()
coffee_make = CoffeeMaker()


ingredients_report = coffee_make.report()


#print(resources)
while True:
    user_selection=input("What do you want "+menu_obj.get_items())
    if user_selection=="off":
        print("Turn off machine")
        break
    elif user_selection=="report":
        coffee_make.report()
        money_obj.report()

    else:
        menu_item_selected=menu_obj.find_drink(user_selection)
        if coffee_make.is_resource_sufficient(menu_item_selected):
            coffee_make.make_coffee(menu_item_selected)
        else:
            print("sorry we can't make your coffee")
            




