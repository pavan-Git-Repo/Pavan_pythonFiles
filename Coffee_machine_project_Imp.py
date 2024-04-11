from arts import coffee_machine
from gameData import MENU as menu
from gameData import resources

print(coffee_machine)
# print(menu)

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are sufficient are insufficient."""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
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
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. ")



turn_on_off = input("Please press 'on' to turn or 'off' to turn of the machine : ")
machine_on = None
if turn_on_off == 'on':
    machine_on = True
    print("*** Welcome to the Cafe Coffee Day ***")
    print("Machine Turned On...")
    print("Have a nice day")
elif turn_on_off == 'off':
    machine_on = False
    print("Machine Turning off...")
profit = 0
while machine_on:
    choice = input("What would you like, espresso/latte/cappuccino? : ")
    if choice == 'off':
        machine_on = False
    elif choice == 'report':
        print(f"Water:{resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])



