#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)
# print(letters)
easy_password = ""
for letter in range(0, nr_letters):
    easy_password += letters[letter]
for symbol in range(0, nr_symbols):
    easy_password += symbols[symbol]
for num in range(0, nr_numbers):
    easy_password += numbers[num]
print("This is a sequential password: ", easy_password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password = []

for letter in range(0, nr_letters):
    hard_password.append(letters[letter])
for symbol in range(0, nr_symbols):
    hard_password.append(symbols[symbol])
for num in range(0, nr_numbers):
    hard_password.append(numbers[num])
# print(hard_password)
random.shuffle(hard_password)
randomised_password = ''.join(hard_password)
print("This is a randomised password: ", randomised_password)
