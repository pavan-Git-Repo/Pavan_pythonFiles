### Cofee Data ###

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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_suffecient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is Enough {item}. ")
            is_enough = False
    return is_enough

def is_transaction_succesfull(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change. ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert Coins.")
    total = int(input("How many Quarters?: ")) * 0.25
    total += int(input("How many Dimes?: ")) * 0.1
    total += int(input("How many Nickels?: ")) * 0.05
    total += int(input("How many Pennies?: ")) * 0.01
    return total



def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. ")
    print("Thanks For Choosing our Cafe......")



turn_on_off = input("Please press 'on' to turn on the machine or 'off' to turn off the Machine: ")
machine_on = True
if turn_on_off == 'on':
    machine_on = True
    print("****Welcome to Cafe Coffe Day****")
    print("    Machine Turning on...    ")
    print("    Have a Nice Day.      ")
elif turn_on_off == 'off':
    machine_on = False
    print("Machine Turning Off....")
profit = 0
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    # print(MENU[choice])
    # ingredients = MENU[choice]['ingredients']
    # print(ingredients)
    if choice == 'off':
        machine_on = False
        print("    Machine Turning Off..... ")
    elif choice == 'report':
        print(f"Water: {resources['water']}ml.")
        print(f"Milk: {resources['milk']}ml. ")
        print(f"Coffee: {resources['coffee']}g. ")
        print(f"Money: ${profit} ")
    else:
        drink = MENU[choice]
        if is_resource_suffecient(drink['ingredients']):
            print(drink['ingredients'])
            payment = process_coins()
            if is_transaction_succesfull(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])






