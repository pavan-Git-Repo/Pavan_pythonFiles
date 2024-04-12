

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


money = 0


while True:
    customer_choice = input("what would you like? 'espresso'/'latte'/'cappuccino'")

    penny = int(input("How many pennies?:  "))

    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickles?: "))
    quarter = int(input("How many quarters?: "))
    money = (((0.25)*quarter)+((0.1)*dime)+((0.05)*nickel)+((0.01)*penny))
    
    #print(money)
    if customer_choice=='espresso':
        if resources['water']<MENU["espresso"]['ingredients']['water'] or resources['coffee']<MENU["espresso"]['ingredients']['coffee'] :
            print("sorry we have no ingredients to make your espresso")
        else:
            if money < 1.5:
                print("Sorry thats not enough money. Money refunded")
                
            elif money >1.5:
                balance_money = money - 1.5
                print(f"please take the balance amount:{balance_money}")
                resources['water'] =resources['water']-MENU["espresso"]['ingredients']['water']
                resources['coffee']=resources["coffee"]-MENU["espresso"]['ingredients']["coffee"]
            else:
                resources['water'] =resources['water']-MENU["espresso"]['ingredients']['water']
                resources['coffee']=resources["coffee"]-MENU["espresso"]['ingredients']["coffee"]
    elif customer_choice=="latte":
        if resources['water']<MENU["latte"]['ingredients']['water'] or resources['coffee']<MENU["latte"]['ingredients']['coffee'] or resources['milk']<MENU["latte"]['ingredients']['milk'] :
            print("sorry we have no ingredients to make your latte")
        else:
            if money < 2.5:
                print("Sorry thats not enough money. Money refunded")
                
            elif money >2.5:
                balance_money = money - 2.5
                print(f"please take the balance amount:{balance_money}")
                resources['water'] =resources['water']-MENU["latte"]['ingredients']['water']
                resources['coffee']=MENU["latte"]['ingredients']['coffee']
                resources['milk']=resources['milk']-MENU["latte"]['ingredients']['milk']
            else:
                resources['water'] =resources['water']-MENU["latte"]['ingredients']['water']
                resources['coffee']=resources["coffee"]-MENU["latte"]['ingredients']["coffee"]
                resources['milk']=resources['milk']-MENU["latte"]['ingredients']['milk']
    else:
        if resources['water']<MENU["cappuccino"]['ingredients']['water'] or resources['coffee']<MENU["cappuccino"]['ingredients']['coffee'] or resources['milk']<MENU["cappuccino"]['ingredients']['milk'] :
            print("sorry we have no ingredients to make your cappuccino")
        else:
            if money < 3.0:
                print("Sorry thats not enough money. Money refunded")
                
            elif money >3.0:
                balance_money = money - 3.0
                print(f"please take the balance amount:{balance_money}")
                resources['water'] =resources['water']-MENU["cappuccino"]['ingredients']['water']
                resources['coffee']=resources['coffee']-MENU["cappuccino"]['ingredients']['coffee']
                resources['milk']=resources['milk']-MENU["cappuccino"]['ingredients']['milk']
            else:
                resources['water'] =resources['water']-MENU["cappuccino"]['ingredients']['water']
                resources['coffee']=resources["coffee"]-MENU["cappuccino"]['ingredients']["coffee"]
                resources['milk']=resources['milk']-MENU["cappuccino"]['ingredients']['milk']

                