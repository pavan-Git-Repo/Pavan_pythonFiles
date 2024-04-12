"""
two_digit_number = input("Type a two digit number: ")
a = int(two_digit_number[0])
b = int(two_digit_number[1])
c = a + b
print(c)
"""
"""
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
h = float(height)
w = int(weight)
person = int(w/(h**2))
print(person)
"""
"""
life_span = input("What is the current life_span? ")
age = input("What is your current age? ")
day = 365
week = 52
month = 12
years = (int(life_span)-int(age))
print(years)
months = (years*month)
days = (years*day)
weeks = (years*week)
print(f'you have {days} days, {weeks} weeks, and {months} months left.')
"""

"""
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
h = float(height)
w = int(weight)
BMI = round(w/(h**2))
if BMI<18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI>18.5 and BMI<25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI>25 and BMI<30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI>30 and BMI<35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
"""

"""
def function_validate_name(name):
    if (len(name) < 3):
        print("The name entered must be three characters long.")
    else:
        print("You've succesfully created a name!")

function_validate_name('pavan')
"""
"""
import random
from unicodedata import name
name_string = input("Give me everybody's names, separated by a coma. :-")
names = name_string.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items -1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today.")
"""

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
for fruit in fruits:

