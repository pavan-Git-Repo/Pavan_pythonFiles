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