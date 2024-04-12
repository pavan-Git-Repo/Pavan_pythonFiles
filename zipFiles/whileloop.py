i = 0
while(i<3):
    print("Hello world")
    i+=1
travelling = input("Yes or No:")
while travelling == 'yes':
    num = int(input("number of people travelling: "))
    for num in range(1,num+1):
        name = input("Name:")
        age = input("Age:")
        sex = input("male or female:")
        print(name)
        print(age)
        print(sex)
    travelling = input("Oops! forgot someone")

i = "python"
j = 1
while j<2:
    for x in i:
        print(j,x)
        j = j+1
        if x =='o':
            break
import random
from random import randint

random_number = random.randint(1,101)

number_of_guesses = 5
guess = 0
easy = 10
hard = 5
while number_of_guesses>guess:
    user_guess = int(input(''))  
    if user_guess>random_number:
      print("Too high")
      number_of_guesses-1
    elif user_guess<random_number:
      print("Too low")
      number_of_guesses-1
    else:
      print(random_number)
      number_of_guesses-1
    while number_of_guesses==0:
        break

