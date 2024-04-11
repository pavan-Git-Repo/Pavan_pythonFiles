import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_images = [rock, paper, scissors]
user_choice = int(input("Please enter the input value to select the following 0-rock, 1-paper, 2-scissors: "))
computer_choice = random.randint(0, 2)
if user_choice >= 3 or user_choice < 0:
    print("You entered an invalid number, You Lose!")
else:
    print(f"Your choice is {user_choice}")
    print(game_images[user_choice])
    print(f"Computer Choice is {computer_choice}")
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("User win!")
    elif computer_choice == 0 and user_choice == 2:
        print("User Lose")
    elif user_choice > computer_choice:
        print("User Win!")
    elif computer_choice > user_choice:
        print("User Lose")
    elif user_choice == computer_choice:
        print("Its is a Draw")