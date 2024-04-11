 print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


step1 = input("Please enter the first step which you want to take left or right: ")

if step1 == "left":
    print("*** Congrats *** you got an access to move forward ")
    step2 = input("Please enter the second step which you want to take swin or wait: ")
    if step2 == 'wait':
        print("*** Congrats *** you got an access to move forward ")
    else:
        print(step2)
        print("You Attacked by the trout")
        print("***--- Game Over ---***")
        exit(0)
    step3 = input("Please enter the third step which door you want to open red or blue or yellow: ")
    if step3 == 'yellow':
        print("***---Congratulations---***")
        print("***---You Win!---***")
    else:
        if step3 == "red":
            print("you Burned by fire")
            print("***--- Game Over ---***")
        elif step3 == "blue":
            print("You Eaten by Beasts")
            print("***--- Game Over ---***")

else:
    print(step1)
    print("You fall into a hole")
    print("***--- Game Over ---***")